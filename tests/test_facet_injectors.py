from __future__ import annotations
from pathlib import Path
import networkx as nx
import pytest
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity
from wiki_compiler.facet_injectors import ADRInjector, TestMapInjector
from wiki_compiler.graph_utils import add_knowledge_node, load_knowledge_node
from wiki_compiler.registry import InjectionContext


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def make_graph(*node_ids: str) -> nx.DiGraph:
    graph = nx.DiGraph()
    for node_id in node_ids:
        node_type = "doc_standard" if node_id.startswith("doc:") else "file"
        add_knowledge_node(graph, KnowledgeNode(
            identity=SystemIdentity(node_id=node_id, node_type=node_type)
        ))
    return graph


def test_adr_injector_has_correct_spec() -> None:
    injector = ADRInjector()
    assert injector.spec.facet_name == "adr"
    assert injector.spec.question  # must be non-empty


def test_adr_injector_populates_adr_from_frontmatter(tmp_path: Path) -> None:
    write(tmp_path / "wiki/adrs/001_pydantic.md", """
---
identity:
  node_id: "doc:wiki/adrs/001_pydantic.md"
  node_type: "doc_standard"
adr:
  decision_id: "001"
  status: "accepted"
  context_summary: "Use Pydantic for all I/O contracts."
edges: []
---
# ADR 001
""")
    graph = make_graph("doc:wiki/adrs/001_pydantic.md")
    ctx = InjectionContext(project_root=tmp_path, adr_dir=tmp_path / "wiki/adrs")

    injector = ADRInjector()
    for node_id in list(graph.nodes):
        node = load_knowledge_node(graph, node_id)
        enriched = injector.inject(node, ctx)
        add_knowledge_node(graph, enriched)

    node = load_knowledge_node(graph, "doc:wiki/adrs/001_pydantic.md")
    assert node.adr is not None
    assert node.adr.decision_id == "001"
    assert node.adr.status == "accepted"


def test_adr_injector_skips_node_without_adr_frontmatter(tmp_path: Path) -> None:
    write(tmp_path / "wiki/adrs/002_plain.md", """
---
identity:
  node_id: "doc:wiki/adrs/002_plain.md"
  node_type: "doc_standard"
edges: []
---
""")
    graph = make_graph("doc:wiki/adrs/002_plain.md")
    ctx = InjectionContext(project_root=tmp_path, adr_dir=tmp_path / "wiki/adrs")
    injector = ADRInjector()
    node = load_knowledge_node(graph, "doc:wiki/adrs/002_plain.md")
    enriched = injector.inject(node, ctx)
    assert enriched.adr is None


def test_test_map_injector_has_correct_spec() -> None:
    injector = TestMapInjector()
    assert injector.spec.facet_name == "test_map"
    assert injector.spec.question


def test_test_map_injector_links_test_imports_to_source_node(tmp_path: Path) -> None:
    write(tmp_path / "tests/test_scanner.py", """
from wiki_compiler.scanner import scan_python_sources
def test_something():
    pass
""")
    # Need to create the actual source file so _module_to_node_id finds it
    write(tmp_path / "src/wiki_compiler/scanner.py", "def scan_python_sources(): pass")
    
    graph = make_graph("file:src/wiki_compiler/scanner.py")
    ctx = InjectionContext(project_root=tmp_path, tests_dir=tmp_path / "tests")
    injector = TestMapInjector()
    for node_id in list(graph.nodes):
        node = load_knowledge_node(graph, node_id)
        enriched = injector.inject(node, ctx)
        add_knowledge_node(graph, enriched)

    node = load_knowledge_node(graph, "file:src/wiki_compiler/scanner.py")
    assert node.test_map is not None
    assert node.test_map.test_type == "unit"
