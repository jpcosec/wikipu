"""
Minimal Energy (ID-2) calculation and reporting.
"""

from __future__ import annotations

import datetime
from pathlib import Path
from collections import Counter

from .contracts import SystemicEnergy, EnergyReport
from .perception import build_status_report
from .auditor import run_audit
import networkx as nx


JACCARD_THRESHOLD = 0.7
BOILERPLATE_THRESHOLD = 0.85
FILE_LINE_THRESHOLD = 300
FUNCTION_STATEMENT_THRESHOLD = 30
DRIFT_PENALTY_WEIGHT = 5.0


def tokenize(text: str) -> set[str]:
    """Convert text to set of normalized tokens for Jaccard comparison."""
    if not text:
        return set()
    tokens = text.lower().split()
    return set(t for t in tokens if len(t) > 2)


def jaccard_similarity(set1: set[str], set2: set[str]) -> float:
    """Calculate Jaccard similarity between two sets."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def detect_redundant_nodes(graph_data: dict) -> tuple[int, float]:
    """
    Detect semantically redundant nodes using Jaccard similarity on intents.
    Returns (redundant_count, boilerplate_ratio).
    """
    nodes = graph_data.get("nodes", [])

    # Extract intents from wiki nodes
    intents: dict[str, str] = {}
    for node in nodes:
        node_id = node.get("id", "")
        if node_id.startswith("doc:wiki/"):
            sem = node.get("schema", {}).get("semantics", {})
            intent = sem.get("intent") if sem else None
            if intent:
                intents[node_id] = intent

    if len(intents) < 2:
        return 0, 0.0

    # Calculate pairwise Jaccard similarities
    redundant_count = 0
    token_sets = {nid: tokenize(txt) for nid, txt in intents.items()}
    node_ids = list(token_sets.keys())

    for i, id1 in enumerate(node_ids):
        for id2 in node_ids[i + 1 :]:
            sim = jaccard_similarity(token_sets[id1], token_sets[id2])
            if sim > JACCARD_THRESHOLD:
                redundant_count += 1

    # Calculate boilerplate ratio (template repetition without new truth)
    # Count common tokens across all intents
    all_tokens = []
    for tokens in token_sets.values():
        all_tokens.extend(tokens)

    token_freq = Counter(all_tokens)
    total_tokens = sum(token_freq.values())

    # High frequency tokens are likely boilerplate
    boilerplate_tokens = sum(
        c for t, c in token_freq.items() if c > len(token_sets) * 0.5
    )

    boilerplate_ratio = boilerplate_tokens / total_tokens if total_tokens > 0 else 0.0

    return redundant_count, boilerplate_ratio


def detect_long_files_and_functions(project_root: Path) -> tuple[int, int]:
    """
    Detect files exceeding line threshold and functions exceeding statement threshold.
    Returns (long_file_count, complex_function_count).
    """
    long_files = 0
    complex_functions = 0

    src_dir = project_root / "src"
    if not src_dir.exists():
        return 0, 0

    for py_file in src_dir.rglob("*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
            lines = content.splitlines()

            # Check file length
            if len(lines) > FILE_LINE_THRESHOLD:
                long_files += 1

            # Count function definitions and check complexity
            in_function = False
            statement_count = 0
            for line in lines:
                stripped = line.strip()
                # Detect function/method definitions
                if stripped.startswith("def ") or stripped.startswith("async def "):
                    # Previous function ended
                    if in_function and statement_count > FUNCTION_STATEMENT_THRESHOLD:
                        complex_functions += 1
                    in_function = True
                    statement_count = 0
                elif in_function and stripped and not stripped.startswith("#"):
                    # Count non-empty, non-comment lines as statements
                    statement_count += 1

            # Check last function
            if in_function and statement_count > FUNCTION_STATEMENT_THRESHOLD:
                complex_functions += 1

        except (UnicodeDecodeError, OSError):
            continue

    return long_files, complex_functions


def detect_code_doc_drift(project_root: Path) -> int:
    """
    Detect drift between documented intent and actual code behavior.
    Returns count of drift violations.
    """
    import json

    drift_count = 0
    graph_path = project_root / "knowledge_graph.json"

    if not graph_path.exists():
        return 0

    with open(graph_path, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    nodes = graph_data.get("nodes", [])

    for node in nodes:
        node_id = node.get("id", "")

        # Only check wiki nodes with intent
        if not node_id.startswith("doc:wiki/"):
            continue

        sem = node.get("schema", {}).get("semantics", {})
        intent = sem.get("intent") if sem else None
        if not intent:
            continue

        # Check for corresponding code file
        # Wiki node name to source file mapping
        wiki_name = node_id.replace("doc:wiki/", "")
        source_name = wiki_name.replace(".md", ".py")

        # Look for matching source file in src/
        src_dir = project_root / "src"
        source_file = None
        for py_file in src_dir.rglob("*.py"):
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

            # Check for docstring
            has_docstring = '"""' in content or "'''" in content

            # Check if intent mentions certain keywords
            intent_lower = intent.lower()
            expects_return = any(
                w in intent_lower for w in ["return", "result", "output"]
            )
            expects_save = any(w in intent_lower for w in ["save", "write", "store"])

            # Check actual behavior from AST
            has_return = "return " in content
            has_write = any(w in content for w in ["write(", "save(", "dump("])

            # Flag drift: documented but not present, or vice versa
            if expects_return and not has_return:
                drift_count += 1
            if expects_save and not has_write:
                drift_count += 1
            if not has_docstring and len(intent) > 50:
                # No docstring but long intent - likely drifted
                drift_count += 1

        except (UnicodeDecodeError, OSError):
            continue

    return drift_count


def calculate_systemic_energy(graph: nx.DiGraph, project_root: Path) -> SystemicEnergy:
    """
    Calculates the systemic energy score based on redundancy heuristic.

    Heuristic:
    Energy = (Redundancy * 10) + (BoilerplateRatio * 50) + (Violations * 10) + (Perturbations * 5) + (Gates * 20)

    Replaces raw node/edge count with semantic quality metrics.
    """
    node_count = graph.number_of_nodes()
    edge_count = graph.number_of_edges()

    # Get audit findings for violation count
    audit_report = run_audit(graph)
    violations = len(audit_report.findings)

    # Get status report for perturbations and gates
    status = build_status_report(
        graph_path=None, project_root=project_root, graph=graph
    )
    perturbations = status.get("perturbations", [])
    open_gates = len(status.get("open_gates", []))

    # Read agent violations
    agent_violations = 0
    violations_log = project_root / "desk/agent_violations.log"
    if violations_log.exists():
        with open(violations_log, "r", encoding="utf-8") as f:
            agent_violations = sum(1 for line in f if line.strip())

    # Check for uncommitted changes (highest energy state)
    uncommitted = 0
    for p in perturbations:
        if p.get("type") in ("modified_node", "untracked_raw", "staged"):
            uncommitted += 1

    # Calculate redundancy metrics from graph JSON
    import json

    graph_path = project_root / "knowledge_graph.json"
    redundant_nodes = 0
    boilerplate_ratio = 0.0

    if graph_path.exists():
        with open(graph_path, "r", encoding="utf-8") as f:
            graph_data = json.load(f)
        redundant_nodes, boilerplate_ratio = detect_redundant_nodes(graph_data)

    # Detect long files and complex functions
    long_files, complex_functions = detect_long_files_and_functions(project_root)

    # Detect code-doc drift
    drift_flags = detect_code_doc_drift(project_root)

    # Abstraction penalties
    long_file_penalty = long_files * 5.0
    complex_function_penalty = complex_functions * 3.0
    abstraction_energy = long_file_penalty + complex_function_penalty

    # Drift penalty
    drift_energy = drift_flags * DRIFT_PENALTY_WEIGHT

    # Redundancy-based energy (replaces raw node/edge count)
    redundancy_energy = redundant_nodes * 10.0
    boilerplate_energy = boilerplate_ratio * 50.0
    structural_energy = redundancy_energy + boilerplate_energy

    # Legacy component (kept for baseline comparison)
    node_energy = node_count * 0.1  # Reduced weight
    edge_energy = edge_count * 0.02

    violation_energy = violations * 10.0
    perturbation_energy = len(perturbations) * 5.0
    gate_energy = open_gates * 20.0
    uncommitted_energy = uncommitted * 50.0  # Maximum entropy - uncommitted changes
    agent_violation_energy = agent_violations * 25.0

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
    )


def run_energy_audit(graph: nx.DiGraph, project_root: Path) -> EnergyReport:
    """Produces a full energy report."""
    current = calculate_systemic_energy(graph, project_root)

    return EnergyReport(
        timestamp=datetime.datetime.now().isoformat(),
        current_energy=current,
        delta=0.0,  # Baseline comparison TODO
    )
