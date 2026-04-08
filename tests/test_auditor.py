from __future__ import annotations
import networkx as nx
import pytest
from wiki_compiler.auditor import (
    ComplianceViolationsCheck,
    MissingDocstringsCheck,
    OrphanedPlansCheck,
    StaleEdgesCheck,
    UndocumentedCodeCheck,
    UntypedIOCheck,
    run_audit,
)
from wiki_compiler.contracts import (
    AuditFinding, ComplianceFacet, Edge, IOFacet,
    KnowledgeNode, SemanticFacet, SystemIdentity,
)
from wiki_compiler.graph_utils import add_knowledge_node


def make_node(node_id: str, node_type: str = "file", **kwargs) -> KnowledgeNode:
    return KnowledgeNode(
        identity=SystemIdentity(node_id=node_id, node_type=node_type), **kwargs
    )


def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:
    graph = nx.DiGraph()
    for node in nodes:
        add_knowledge_node(graph, node)
    return graph


def test_undocumented_code_check_has_correct_metadata() -> None:
    check = UndocumentedCodeCheck()
    assert check.related_facet == "semantics"
    assert check.question


def test_undocumented_code_detects_file_with_no_documents_edge() -> None:
    graph = make_graph(make_node("file:src/foo.py"))
    findings = UndocumentedCodeCheck().run(graph)
    assert any(f.node_id == "file:src/foo.py" for f in findings)


def test_undocumented_code_passes_when_documents_edge_exists() -> None:
    graph = make_graph(
        make_node("file:src/foo.py"),
        make_node("doc:wiki/foo.md", node_type="doc_standard", edges=[
            Edge(target_id="file:src/foo.py", relation_type="documents"),
        ]),
    )
    findings = UndocumentedCodeCheck().run(graph)
    assert not any(f.node_id == "file:src/foo.py" for f in findings)


def test_missing_docstrings_detects_null_raw_docstring() -> None:
    graph = make_graph(make_node(
        "file:src/bar.py",
        semantics=SemanticFacet(intent="Bar.", raw_docstring=None),
    ))
    findings = MissingDocstringsCheck().run(graph)
    assert any(f.node_id == "file:src/bar.py" for f in findings)


def test_missing_docstrings_passes_when_docstring_present() -> None:
    graph = make_graph(make_node(
        "file:src/bar.py",
        semantics=SemanticFacet(intent="Bar.", raw_docstring="Bar module."),
    ))
    findings = MissingDocstringsCheck().run(graph)
    assert not any(f.node_id == "file:src/bar.py" for f in findings)


def test_untyped_io_detects_port_without_schema_ref() -> None:
    graph = make_graph(make_node(
        "file:src/writer.py",
        io_ports=[IOFacet(medium="disk", path_template="data/out.json", schema_ref=None)],
    ))
    findings = UntypedIOCheck().run(graph)
    assert any(f.node_id == "file:src/writer.py" for f in findings)


def test_compliance_violations_detects_failing_standards() -> None:
    graph = make_graph(make_node(
        "file:src/sloppy.py",
        compliance=ComplianceFacet(
            status="implemented",
            failing_standards=["00_house_rules#docstrings"],
        ),
    ))
    findings = ComplianceViolationsCheck().run(graph)
    assert any(f.node_id == "file:src/sloppy.py" for f in findings)


def test_stale_edges_detects_missing_target() -> None:
    graph = make_graph(make_node(
        "doc:wiki/foo.md", node_type="doc_standard",
        edges=[Edge(target_id="file:src/gone.py", relation_type="documents")],
    ))
    findings = StaleEdgesCheck().run(graph)
    assert any(f.node_id == "doc:wiki/foo.md" for f in findings)
    assert any("file:src/gone.py" in f.detail for f in findings)


def test_orphaned_plans_detects_future_docs_with_no_code_edge() -> None:
    graph = make_graph(make_node("doc:future_docs/feature_x.md", node_type="concept"))
    findings = OrphanedPlansCheck().run(graph)
    assert any(f.node_id == "doc:future_docs/feature_x.md" for f in findings)


def test_run_audit_aggregates_all_checks() -> None:
    graph = make_graph(make_node("file:src/undoc.py"))
    report = run_audit(graph)
    assert "undocumented_code" in report.summary
    assert report.summary["undocumented_code"] >= 1
