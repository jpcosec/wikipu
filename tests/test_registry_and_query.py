from __future__ import annotations
import networkx as nx
import pytest
from wiki_compiler.contracts import (
    ComplianceFacet, IOFacet, KnowledgeNode, SemanticFacet, SystemIdentity,
)
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.registry import FacetRegistry, FacetSpec, FieldSpec
from wiki_compiler.query_language import (
    FieldCondition, FacetFilter, GraphScope, StructuredQuery,
)
from wiki_compiler.query_executor import execute_query


def make_node(node_id: str, node_type: str = "file", **kwargs) -> KnowledgeNode:
    return KnowledgeNode(
        identity=SystemIdentity(node_id=node_id, node_type=node_type),
        **kwargs,
    )


def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:
    graph = nx.DiGraph()
    for node in nodes:
        add_knowledge_node(graph, node)
    return graph


# --- Registry tests ---

def test_registry_stores_and_retrieves_facet_spec() -> None:
    registry = FacetRegistry()
    spec = FacetSpec(
        facet_name="compliance",
        question="How complete and rule-compliant is this node?",
        applies_to={"file", "code_construct"},
        fields=[FieldSpec(name="status", type="str", nullable=False)],
    )
    registry.register_spec(spec)
    assert registry.get_spec("compliance") == spec


def test_registry_lists_all_registered_facet_names() -> None:
    registry = FacetRegistry()
    registry.register_spec(FacetSpec(
        facet_name="semantics",
        question="What does this node do?",
        applies_to={"file"},
        fields=[],
    ))
    registry.register_spec(FacetSpec(
        facet_name="compliance",
        question="How complete and rule-compliant is this node?",
        applies_to={"file"},
        fields=[],
    ))
    assert set(registry.facet_names) == {"semantics", "compliance"}


# --- Single-facet query tests ---

def test_execute_query_filters_by_compliance_status() -> None:
    graph = make_graph(
        make_node("file:src/a.py", compliance=ComplianceFacet(status="planned", failing_standards=[])),
        make_node("file:src/b.py", compliance=ComplianceFacet(status="implemented", failing_standards=[])),
    )
    query = StructuredQuery(
        filters=[FacetFilter(
            facet="compliance",
            conditions=[FieldCondition(field="status", op="eq", value="planned")],
        )]
    )
    results = execute_query(graph, query)
    assert len(results) == 1
    assert results[0].identity.node_id == "file:src/a.py"


def test_execute_query_filters_by_null_field() -> None:
    graph = make_graph(
        make_node("file:src/a.py", semantics=SemanticFacet(intent="A", raw_docstring=None)),
        make_node("file:src/b.py", semantics=SemanticFacet(intent="B", raw_docstring="Has one.")),
    )
    query = StructuredQuery(
        filters=[FacetFilter(
            facet="semantics",
            conditions=[FieldCondition(field="raw_docstring", op="is_null")],
        )]
    )
    results = execute_query(graph, query)
    assert len(results) == 1
    assert results[0].identity.node_id == "file:src/a.py"


# --- Compound query tests ---

def test_execute_query_intersects_two_facet_filters() -> None:
    graph = make_graph(
        make_node(
            "file:src/a.py",
            compliance=ComplianceFacet(status="planned", failing_standards=[]),
            semantics=SemanticFacet(intent="A", raw_docstring=None),
        ),
        make_node(
            "file:src/b.py",
            compliance=ComplianceFacet(status="planned", failing_standards=[]),
            semantics=SemanticFacet(intent="B", raw_docstring="Present."),
        ),
        make_node(
            "file:src/c.py",
            compliance=ComplianceFacet(status="implemented", failing_standards=[]),
            semantics=SemanticFacet(intent="C", raw_docstring=None),
        ),
    )
    query = StructuredQuery(
        filters=[
            FacetFilter(facet="compliance", conditions=[
                FieldCondition(field="status", op="eq", value="planned"),
            ]),
            FacetFilter(facet="semantics", conditions=[
                FieldCondition(field="raw_docstring", op="is_null"),
            ]),
        ]
    )
    results = execute_query(graph, query)
    assert len(results) == 1
    assert results[0].identity.node_id == "file:src/a.py"


# --- Graph scope tests ---

def test_execute_query_scopes_to_descendants() -> None:
    from wiki_compiler.contracts import Edge
    parent = make_node("dir:src/translator", node_type="directory", edges=[
        Edge(target_id="file:src/translator/a.py", relation_type="contains"),
    ])
    child = make_node(
        "file:src/translator/a.py",
        compliance=ComplianceFacet(status="planned", failing_standards=[]),
    )
    other = make_node(
        "file:src/other/b.py",
        compliance=ComplianceFacet(status="planned", failing_standards=[]),
    )
    graph = make_graph(parent, child, other)
    query = StructuredQuery(
        filters=[FacetFilter(facet="compliance", conditions=[
            FieldCondition(field="status", op="eq", value="planned"),
        ])],
        scope=GraphScope(descendant_of="dir:src/translator"),
    )
    results = execute_query(graph, query)
    node_ids = {r.identity.node_id for r in results}
    assert "file:src/translator/a.py" in node_ids
    assert "file:src/other/b.py" not in node_ids
