"""
Builds the Knowledge Graph by scanning Markdown wiki nodes and Python source code.
It orchestrates the multi-phase compilation: directory skeleton, node ingestion, and facet injection.
"""

from __future__ import annotations

import json
import inspect
import os
import re
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import yaml

from .contracts import (
    ComplianceFacet,
    Edge,
    KnowledgeNode,
    SemanticFacet,
    SystemIdentity,
)
from .facet_injectors import ADRInjector, TestMapInjector
from .graph_utils import add_knowledge_node, load_knowledge_node, save_graph
from .node_templates import (
    build_default_template_registry,
    extract_abstract,
    validate_template_sections,
)
from .perception import attach_git_facets
from .registry import InjectionContext
from .scanner import scan_python_sources


TRANSCLUSION_REGEX = re.compile(r"!\[\[(.*?)\]\]")
FRONTMATTER_REGEX = re.compile(r"\A---\s*\n(.*?)\n---(\s*\n|$)", re.DOTALL)
COMPLIANT_STATUSES = {"implemented", "tested", "exempt"}


@dataclass(frozen=True)
class BuildResult:
    """
    Encapsulates the outcome of a Knowledge Graph build process.
    """

    graph_path: Path
    baseline_path: Path
    compliance_score: float
    baseline_updated: bool
    baseline_regressed: bool


def build_wiki(
    source_dir: Path,
    graph_path: Path,
    *,
    dest_dir: Path | None = None,
    project_root: Path | None = None,
    code_roots: list[Path] | None = None,
    baseline_path: Path | None = None,
    update_baseline: bool = False,
    attach_git_facets: bool = False,
    run_facet_injectors: bool = False,
) -> BuildResult:
    """
    Orchestrates the full Knowledge Graph build, including scanning and facet injection.
    """
    root = project_root or Path.cwd()
    graph = nx.DiGraph()

    # Phase 2: file + code nodes with facets
    files_index = index_markdown_files(source_dir)
    for markdown_path in sorted(source_dir.rglob("*.md")):
        node, raw_markdown = parse_markdown_node(markdown_path)
        if dest_dir is not None:
            compile_markdown_node(
                markdown_path=markdown_path,
                source_dir=source_dir,
                dest_dir=dest_dir,
                raw_markdown=raw_markdown,
                files_index=files_index,
            )
        if node is not None:
            for transclusion_target in extract_transclusions(raw_markdown, files_index):
                node.edges.append(
                    Edge(target_id=transclusion_target, relation_type="transcludes")
                )
            add_knowledge_node(graph, node)

    from .scanner import scan_codebase

    for node in scan_codebase(
        project_root=root,
        source_roots=code_roots or [root / "src"],
        wikiignore_path=root / ".wikiignore",
    ):
        add_knowledge_node(graph, node)
    infer_reference_documents_edges(graph)

    # Phase 2b: facet injector passes
    if run_facet_injectors:
        ctx = InjectionContext(
            project_root=root,
            adr_dir=root / "wiki" / "adrs",
            tests_dir=root / "tests",
        )
        for injector in [ADRInjector(), TestMapInjector()]:
            for node_id in list(graph.nodes):
                node = load_knowledge_node(graph, node_id)
                enriched = injector.inject(node, ctx)
                add_knowledge_node(graph, enriched)

    if attach_git_facets:
        attach_git_facets(graph, root)

    save_graph(graph, graph_path)
    score = calculate_compliance_score(graph)
    baseline_file = baseline_path or Path(".compliance_baseline.json")
    baseline_updated, baseline_regressed = update_compliance_baseline(
        baseline_file,
        score,
        update_baseline=update_baseline,
    )
    return BuildResult(
        graph_path=graph_path,
        baseline_path=baseline_file,
        compliance_score=score,
        baseline_updated=baseline_updated,
        baseline_regressed=baseline_regressed,
    )


def build_directory_skeleton(root: Path, project_root: Path) -> list[KnowledgeNode]:
    """Emit one directory node per directory under root, with contains edges to children."""
    from .scanner import load_wikiignore_rules, match_ignore_reason

    nodes: list[KnowledgeNode] = []
    ignore_rules = load_wikiignore_rules(project_root / ".wikiignore")

    all_paths = list([root] + sorted(d for d in root.rglob("*") if d.is_dir()))

    path_set = {p.resolve() for p in all_paths}

    for dirpath in all_paths:
        rel = dirpath.relative_to(project_root).as_posix()
        if match_ignore_reason(rel, ignore_rules):
            continue
        children = []
        try:
            for c in dirpath.iterdir():
                if c.resolve() in path_set:
                    children.append(c)
                elif c.is_file():
                    children.append(c)
        except PermissionError:
            pass
        edges = [
            Edge(
                target_id=f"{'dir' if c.is_dir() else 'file'}:{c.relative_to(project_root).as_posix()}",
                relation_type="contains",
            )
            for c in sorted(children)
        ]
        nodes.append(
            KnowledgeNode(
                identity=SystemIdentity(node_id=f"dir:{rel}", node_type="directory"),
                edges=edges,
                compliance=ComplianceFacet(status="implemented", failing_standards=[]),
            )
        )
    return nodes


def index_markdown_files(source_dir: Path) -> dict[str, Path]:
    """
    Creates a mapping of markdown filename stems to their absolute paths.
    """
    return {filepath.stem: filepath for filepath in source_dir.rglob("*.md")}


def parse_markdown_node(filepath: Path) -> tuple[KnowledgeNode | None, str]:
    """
    Parses a markdown file to extract its KnowledgeNode representation and raw content.
    """
    content = inspect.cleandoc(filepath.read_text(encoding="utf-8")) + "\n"
    yaml_match = FRONTMATTER_REGEX.search(content)
    if not yaml_match:
        return None, content
    raw_markdown = content[yaml_match.end() :].lstrip("\n")
    node_data = yaml.safe_load(yaml_match.group(1)) or {}
    validated_node = KnowledgeNode.model_validate(node_data)

    # Wiki Construction: Extract abstract as intent
    abstract = extract_abstract(content)
    if validated_node.semantics is None:
        validated_node.semantics = SemanticFacet(
            intent=abstract or extract_heading(raw_markdown), raw_docstring=None
        )
    elif abstract:
        validated_node.semantics.intent = abstract

    # Wiki Construction: Template compliance
    registry = build_default_template_registry()
    missing_sections = validate_template_sections(
        validated_node.identity.node_type, content, registry
    )

    if validated_node.compliance is None:
        validated_node.compliance = ComplianceFacet(
            status="implemented", failing_standards=missing_sections
        )
    else:
        validated_node.compliance.failing_standards.extend(missing_sections)

    return validated_node, raw_markdown


def extract_heading(markdown: str) -> str:
    """
    Extracts the first top-level heading from a markdown string.
    """
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ")
    return "Wiki node"


def extract_transclusions(markdown: str, files_index: dict[str, Path]) -> list[str]:
    """
    Identifies and resolves wiki-style transclusions in markdown content.
    """
    targets: list[str] = []
    for match in TRANSCLUSION_REGEX.finditer(markdown):
        target_name = match.group(1)
        target_path = files_index.get(target_name)
        if target_path is None:
            continue
        targets.append(f"doc:{target_path.as_posix()}")
    return targets


def compile_markdown_node(
    *,
    markdown_path: Path,
    source_dir: Path,
    dest_dir: Path,
    raw_markdown: str,
    files_index: dict[str, Path],
) -> None:
    """Writes a compiled markdown copy with wiki transclusions rendered as links."""
    compiled_path = dest_dir / markdown_path.relative_to(source_dir)
    compiled_path.parent.mkdir(parents=True, exist_ok=True)
    compiled_path.write_text(
        render_compiled_markdown(
            markdown=raw_markdown,
            output_dir=compiled_path.parent,
            source_dir=source_dir,
            dest_dir=dest_dir,
            files_index=files_index,
        ),
        encoding="utf-8",
    )


def render_compiled_markdown(
    markdown: str,
    output_dir: Path,
    source_dir: Path,
    dest_dir: Path,
    files_index: dict[str, Path],
) -> str:
    """Converts wiki transclusions into relative markdown links for compiled output."""

    def replacement(match: re.Match[str]) -> str:
        target_name = match.group(1)
        target_path = files_index.get(target_name)
        if target_path is None:
            return match.group(0)
        compiled_target = dest_dir / target_path.relative_to(source_dir)
        relative = os.path.relpath(compiled_target, output_dir).replace(os.sep, "/")
        return f"[See {target_name}]({relative})"

    compiled = TRANSCLUSION_REGEX.sub(replacement, markdown).strip()
    return compiled + "\n"


def infer_reference_documents_edges(graph: nx.DiGraph) -> None:
    """Adds inferred `documents` edges from wiki reference pages to code nodes."""
    file_candidates = build_reference_file_candidates(graph)
    for node_id in sorted(graph.nodes):
        if not node_id.startswith("doc:wiki/reference/"):
            continue
        stem = Path(node_id.removeprefix("doc:")).stem
        matched_file = match_reference_file(stem, file_candidates)
        if matched_file is None:
            continue
        target_ids = [matched_file]
        target_ids.extend(sorted(code_nodes_for_file(graph, matched_file)))
        add_documents_edges(graph, node_id, target_ids)


def build_reference_file_candidates(graph: nx.DiGraph) -> dict[str, list[str]]:
    """Indexes file nodes by stem for wiki reference auto-linking."""
    candidates: dict[str, list[str]] = {}
    for node_id, data in graph.nodes(data=True):
        if data.get("type") != "file" or not node_id.startswith("file:src/"):
            continue
        stem = Path(node_id.removeprefix("file:")).stem
        candidates.setdefault(stem, []).append(node_id)
    return candidates


def match_reference_file(stem: str, candidates: dict[str, list[str]]) -> str | None:
    """Returns the single best file match for a reference page stem."""
    matches = candidates.get(stem, [])
    if len(matches) == 1:
        return matches[0]
    preferred = [
        node_id for node_id in matches if node_id.startswith("file:src/wiki_compiler/")
    ]
    if len(preferred) == 1:
        return preferred[0]
    return None


def code_nodes_for_file(graph: nx.DiGraph, file_node_id: str) -> list[str]:
    """Returns code construct node ids contained by a file node."""
    file_prefix = f"code:{file_node_id.removeprefix('file:')}:"
    return [
        node_id
        for node_id, data in graph.nodes(data=True)
        if data.get("type") == "code_construct" and node_id.startswith(file_prefix)
    ]


def add_documents_edges(
    graph: nx.DiGraph, source_id: str, target_ids: list[str]
) -> None:
    """Persists inferred documentation edges onto both the graph and source node schema."""
    node = load_knowledge_node(graph, source_id)
    existing_targets = {
        edge.target_id for edge in node.edges if edge.relation_type == "documents"
    }
    changed = False
    for target_id in target_ids:
        if target_id in existing_targets:
            continue
        node.edges.append(Edge(target_id=target_id, relation_type="documents"))
        existing_targets.add(target_id)
        changed = True
    if changed:
        add_knowledge_node(graph, node)


def calculate_compliance_score(graph: nx.DiGraph) -> float:
    """
    Computes the percentage of nodes that meet implementation or testing standards.
    """
    statuses = [
        data.get("status")
        for _, data in graph.nodes(data=True)
        if data.get("status") not in {None, "unknown"}
    ]
    if not statuses:
        return 100.0
    compliant = sum(1 for status in statuses if status in COMPLIANT_STATUSES)
    return round((compliant / len(statuses)) * 100, 2)


def update_compliance_baseline(
    baseline_path: Path,
    score: float,
    *,
    update_baseline: bool,
) -> tuple[bool, bool]:
    """
    Updates or checks the current compliance score against a persistent baseline.
    """
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    if not baseline_path.exists() or update_baseline:
        write_baseline(baseline_path, score)
        return True, False
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    regressed = score < float(baseline.get("score", score))
    return False, regressed


def write_baseline(baseline_path: Path, score: float) -> None:
    """
    Writes the compliance score to a JSON baseline file.
    """
    payload = {"score": score}
    baseline_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
