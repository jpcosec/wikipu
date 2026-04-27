"""Energy calculation and reporting owned by wikipu."""

from __future__ import annotations

import datetime
import json
from collections import Counter
from pathlib import Path
from typing import Any, Callable

import networkx as nx
import numpy as np

from wiki_compiler.contracts import EnergyReport, SystemicEnergy


JACCARD_THRESHOLD = 0.7
BOILERPLATE_THRESHOLD = 0.85
FILE_LINE_THRESHOLD = 300
FUNCTION_STATEMENT_THRESHOLD = 30
DRIFT_PENALTY_WEIGHT = 5.0
FFT_ENERGY_WEIGHT = 10.0


def tokenize(text: str) -> set[str]:
    """Convert text to normalized tokens for Jaccard comparison."""
    if not text:
        return set()
    return {token for token in text.lower().split() if len(token) > 2}


def calculate_fft_metrics(
    project_root: Path, face_analyzer_cls: type[Any] | None = None
) -> dict[str, float | int]:
    """Calculate FFT-based metrics for code and wiki analysis."""
    if face_analyzer_cls is None:
        return {
            "so": 0.0,
            "corr": 0.0,
            "complexity": 0.0,
            "coherence": 0.0,
            "within_corr": 0.0,
            "code_count": 0,
            "wiki_count": 0,
        }

    analyzer = face_analyzer_cls(preprocess="zscore")

    code_files = [
        file_path
        for file_path in (project_root / "src").rglob("*.py")
        if "__pycache__" not in str(file_path)
    ]
    wiki_files = list((project_root / "wiki").rglob("*.md"))

    code_spectra = {}
    for file_path in code_files:
        try:
            text = file_path.read_text(encoding="utf-8")
            if len(text) > 200:
                code_spectra[file_path.name] = analyzer.analyze_text(text)
        except Exception:
            continue

    wiki_spectra = {}
    for file_path in wiki_files:
        try:
            text = file_path.read_text(encoding="utf-8")
            if len(text) > 200:
                wiki_spectra[file_path.name] = analyzer.analyze_text(text)
        except Exception:
            continue

    if not code_spectra or not wiki_spectra:
        return {
            "so": 0.0,
            "corr": 0.0,
            "complexity": 0.0,
            "coherence": 0.0,
            "within_corr": 0.0,
            "code_count": len(code_spectra),
            "wiki_count": len(wiki_spectra),
        }

    code_vals = list(code_spectra.values())
    wiki_vals = list(wiki_spectra.values())

    cross_sos: list[float] = []
    cross_corrs: list[float] = []
    for code_spectrum in code_vals[:15]:
        for wiki_spectrum in wiki_vals[:15]:
            metrics = analyzer.compare_spectra(code_spectrum, wiki_spectrum)
            cross_sos.append(metrics.so)
            cross_corrs.append(metrics.corr)

    within_sos: list[float] = []
    within_corrs: list[float] = []
    for first_index in range(min(20, len(code_vals))):
        for second_index in range(first_index + 1, min(20, len(code_vals))):
            metrics = analyzer.compare_spectra(
                code_vals[first_index], code_vals[second_index]
            )
            within_sos.append(metrics.so)
            within_corrs.append(metrics.corr)

    avg_code = analyzer.average_spectrum(code_vals)
    powers = avg_code[1]
    complexity = float(np.std(powers[: len(powers) // 4])) if len(powers) > 4 else 0.0

    return {
        "so": float(np.mean(cross_sos)) if cross_sos else 0.0,
        "corr": float(np.mean(cross_corrs)) if cross_corrs else 0.0,
        "coherence": float(np.mean(within_sos)) if within_sos else 0.0,
        "within_corr": float(np.mean(within_corrs)) if within_corrs else 0.0,
        "complexity": complexity,
        "code_count": len(code_spectra),
        "wiki_count": len(wiki_spectra),
    }


def jaccard_similarity(set1: set[str], set2: set[str]) -> float:
    """Calculate Jaccard similarity between two sets."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def detect_redundant_nodes(graph_data: dict[str, Any]) -> tuple[int, float]:
    """Detect semantically redundant nodes using Jaccard similarity on intents."""
    nodes = graph_data.get("nodes", [])

    intents: dict[str, str] = {}
    for node in nodes:
        node_id = node.get("id", "")
        if node_id.startswith("doc:wiki/"):
            semantics = node.get("schema", {}).get("semantics", {})
            intent = semantics.get("intent") if semantics else None
            if intent:
                intents[node_id] = intent

    if len(intents) < 2:
        return 0, 0.0

    redundant_count = 0
    token_sets = {node_id: tokenize(text) for node_id, text in intents.items()}
    node_ids = list(token_sets.keys())

    for index, left_id in enumerate(node_ids):
        for right_id in node_ids[index + 1 :]:
            similarity = jaccard_similarity(token_sets[left_id], token_sets[right_id])
            if similarity > JACCARD_THRESHOLD:
                redundant_count += 1

    all_tokens: list[str] = []
    for tokens in token_sets.values():
        all_tokens.extend(tokens)

    token_freq = Counter(all_tokens)
    total_tokens = sum(token_freq.values())
    boilerplate_tokens = sum(
        count for _, count in token_freq.items() if count > len(token_sets) * 0.5
    )
    boilerplate_ratio = boilerplate_tokens / total_tokens if total_tokens > 0 else 0.0

    return redundant_count, boilerplate_ratio


def detect_long_files_and_functions(project_root: Path) -> tuple[int, int]:
    """Detect files exceeding line thresholds and functions exceeding statement thresholds."""
    long_files = 0
    complex_functions = 0

    src_dir = project_root / "src"
    if not src_dir.exists():
        return 0, 0

    for py_file in src_dir.rglob("*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
            lines = content.splitlines()

            if len(lines) > FILE_LINE_THRESHOLD:
                long_files += 1

            in_function = False
            statement_count = 0
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("def ") or stripped.startswith("async def "):
                    if in_function and statement_count > FUNCTION_STATEMENT_THRESHOLD:
                        complex_functions += 1
                    in_function = True
                    statement_count = 0
                elif in_function and stripped and not stripped.startswith("#"):
                    statement_count += 1

            if in_function and statement_count > FUNCTION_STATEMENT_THRESHOLD:
                complex_functions += 1
        except (UnicodeDecodeError, OSError):
            continue

    return long_files, complex_functions


def detect_code_doc_drift(project_root: Path) -> int:
    """Detect drift between documented intent and actual code behavior."""
    graph_path = project_root / "knowledge_graph.json"
    if not graph_path.exists():
        return 0

    with graph_path.open("r", encoding="utf-8") as file_handle:
        graph_data = json.load(file_handle)

    drift_count = 0
    nodes = graph_data.get("nodes", [])
    for node in nodes:
        node_id = node.get("id", "")
        if not node_id.startswith("doc:wiki/"):
            continue

        semantics = node.get("schema", {}).get("semantics", {})
        intent = semantics.get("intent") if semantics else None
        if not intent:
            continue

        wiki_name = node_id.replace("doc:wiki/", "")
        source_file = None
        for py_file in (project_root / "src").rglob("*.py"):
            if py_file.stem in (
                wiki_name.replace(".md", ""),
                wiki_name.replace("_", ""),
            ):
                source_file = py_file
                break

        if not source_file:
            continue

        try:
            content = source_file.read_text(encoding="utf-8")
            has_docstring = '"""' in content or "'''" in content
            intent_lower = intent.lower()
            expects_return = any(
                word in intent_lower for word in ["return", "result", "output"]
            )
            expects_save = any(
                word in intent_lower for word in ["save", "write", "store"]
            )
            has_return = "return " in content
            has_write = any(word in content for word in ["write(", "save(", "dump("])

            if expects_return and not has_return:
                drift_count += 1
            if expects_save and not has_write:
                drift_count += 1
            if not has_docstring and len(intent) > 50:
                drift_count += 1
        except (UnicodeDecodeError, OSError):
            continue

    return drift_count


def calculate_systemic_energy(
    graph: nx.DiGraph,
    project_root: Path,
    audit_runner: Callable[[nx.DiGraph], Any] | None = None,
    status_builder: Callable[..., dict[str, object]] | None = None,
    face_analyzer_cls: type[Any] | None = None,
) -> SystemicEnergy:
    """Calculate systemic energy from structural and operational signals."""
    node_count = graph.number_of_nodes()
    edge_count = graph.number_of_edges()

    violations = 0
    if audit_runner is not None:
        audit_report = audit_runner(graph)
        violations = len(audit_report.findings)

    status = {"perturbations": [], "open_gates": []}
    if status_builder is not None:
        status = status_builder(graph_path=None, project_root=project_root, graph=graph)
    perturbations = status.get("perturbations", [])
    open_gates = len(status.get("open_gates", []))

    agent_violations = 0
    violations_log = project_root / "desk/agent_violations.log"
    if violations_log.exists():
        with violations_log.open("r", encoding="utf-8") as file_handle:
            agent_violations = sum(1 for line in file_handle if line.strip())

    uncommitted = 0
    for perturbation in perturbations:
        if perturbation.get("type") in ("modified_node", "untracked_raw", "staged"):
            uncommitted += 1

    graph_path = project_root / "knowledge_graph.json"
    redundant_nodes = 0
    boilerplate_ratio = 0.0
    if graph_path.exists():
        with graph_path.open("r", encoding="utf-8") as file_handle:
            graph_data = json.load(file_handle)
        redundant_nodes, boilerplate_ratio = detect_redundant_nodes(graph_data)

    long_files, complex_functions = detect_long_files_and_functions(project_root)
    drift_flags = detect_code_doc_drift(project_root)
    fft_metrics = calculate_fft_metrics(project_root, face_analyzer_cls)

    abstraction_energy = long_files * 5.0 + complex_functions * 3.0
    drift_energy = drift_flags * DRIFT_PENALTY_WEIGHT
    structural_energy = redundant_nodes * 10.0 + boilerplate_ratio * 50.0
    node_energy = node_count * 0.1
    edge_energy = edge_count * 0.02
    violation_energy = violations * 10.0
    perturbation_energy = len(perturbations) * 5.0
    gate_energy = open_gates * 20.0
    uncommitted_energy = uncommitted * 50.0
    agent_violation_energy = agent_violations * 25.0

    fft_so = float(fft_metrics.get("so", 0.5))
    fft_corr = float(fft_metrics.get("corr", 0.0))
    fft_coherence = float(fft_metrics.get("coherence", 0.5))
    fft_complexity = float(fft_metrics.get("complexity", 0.0))
    fft_energy = (1 - fft_so) * 5.0 + abs(fft_corr) * 2.0 + fft_complexity * 0.1

    total_score = (
        structural_energy
        + abstraction_energy
        + drift_energy
        + node_energy
        + edge_energy
        + violation_energy
        + perturbation_energy
        + gate_energy
        + uncommitted_energy
        + agent_violation_energy
        + fft_energy
    )

    return SystemicEnergy(
        energy_score=total_score,
        node_count=node_count,
        edge_count=edge_count,
        compliance_violations=violations,
        perturbations=len(perturbations),
        open_gates=open_gates,
        agent_violations=agent_violations,
        redundant_nodes=redundant_nodes,
        boilerplate_ratio=boilerplate_ratio,
        long_files=long_files,
        complex_functions=complex_functions,
        drift_flags=drift_flags,
        structural_energy=structural_energy,
        abstraction_energy=abstraction_energy,
        violation_energy=violation_energy,
        perturbation_energy=perturbation_energy + gate_energy,
        agent_violation_energy=agent_violation_energy,
        fft_code_wiki_so=fft_so,
        fft_code_wiki_corr=fft_corr,
        fft_code_within_so=fft_coherence,
        fft_code_within_corr=float(fft_metrics.get("within_corr", 0.0)),
        fft_complexity_score=fft_complexity,
        fft_energy=fft_energy,
    )


def run_energy_audit(
    graph: nx.DiGraph,
    project_root: Path,
    audit_runner: Callable[[nx.DiGraph], Any] | None = None,
    status_builder: Callable[..., dict[str, object]] | None = None,
    face_analyzer_cls: type[Any] | None = None,
) -> EnergyReport:
    """Produce a full energy report."""
    current = calculate_systemic_energy(
        graph,
        project_root,
        audit_runner=audit_runner,
        status_builder=status_builder,
        face_analyzer_cls=face_analyzer_cls,
    )
    return EnergyReport(
        timestamp=datetime.datetime.now().isoformat(),
        current_energy=current,
        delta=0.0,
    )


__all__ = [
    "BOILERPLATE_THRESHOLD",
    "DRIFT_PENALTY_WEIGHT",
    "FFT_ENERGY_WEIGHT",
    "FILE_LINE_THRESHOLD",
    "FUNCTION_STATEMENT_THRESHOLD",
    "JACCARD_THRESHOLD",
    "calculate_fft_metrics",
    "calculate_systemic_energy",
    "detect_code_doc_drift",
    "detect_long_files_and_functions",
    "detect_redundant_nodes",
    "jaccard_similarity",
    "run_energy_audit",
    "tokenize",
]
