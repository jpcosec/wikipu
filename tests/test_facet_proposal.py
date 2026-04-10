from __future__ import annotations
import json
from pathlib import Path
import networkx as nx
import pytest
from wiki_compiler.contracts import (
    ComplianceFacet, FacetOrthogonalityReport, FacetProposal,
    KnowledgeNode, SemanticFacet, SystemIdentity,
)
from wiki_compiler.facet_validator import validate_facet_proposal
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.query_language import FacetFilter, FieldCondition, StructuredQuery
from wiki_compiler.registry import FacetRegistry, FacetSpec, FieldSpec, build_default_registry


def make_graph(*nodes: KnowledgeNode) -> nx.DiGraph:
    graph = nx.DiGraph()
    for node in nodes:
        add_knowledge_node(graph, node)
    return graph


def make_node(node_id: str, **kwargs) -> KnowledgeNode:
    return KnowledgeNode(
        identity=SystemIdentity(node_id=node_id, node_type="file"), **kwargs
    )


# --- Question collision ---

def test_rejects_question_that_overlaps_existing_facet(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = nx.DiGraph()
    proposal = FacetProposal(
        proposed_facet_name="doc_summary",
        question="What does this node do and why?",   # overlaps SemanticFacet
        applies_to=["file"],
        proposed_fields=[{"name": "summary", "type": "str"}],
        attempted_query=None,
    )
    report = validate_facet_proposal(
        proposal=proposal,
        registry=registry,
        graph=graph,
        state_path=tmp_path / "state.json",
    )
    assert report.is_orthogonal is False
    assert any(s.facet_name == "semantics" for s in report.colliding_facets)
    assert report.attempts_remaining == 2


def test_accepts_question_with_no_overlap(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = nx.DiGraph()
    proposal = FacetProposal(
        proposed_facet_name="model_usage",
        question="Which AI models does this node invoke?",
        applies_to=["file", "code_construct"],
        proposed_fields=[{"name": "model_name", "type": "str"}],
        attempted_query=None,
    )
    report = validate_facet_proposal(
        proposal=proposal,
        registry=registry,
        graph=graph,
        state_path=tmp_path / "state.json",
    )
    assert report.is_orthogonal is True
    assert report.attempts_remaining == 3


# --- Field collision ---

def test_rejects_proposed_field_that_already_exists(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = nx.DiGraph()
    proposal = FacetProposal(
        proposed_facet_name="custom_status",
        question="What is the deployment stage of this node?",
        applies_to=["file"],
        proposed_fields=[{"name": "status", "type": "str"}],  # status exists in compliance
        attempted_query=None,
    )
    report = validate_facet_proposal(
        proposal=proposal,
        registry=registry,
        graph=graph,
        state_path=tmp_path / "state.json",
    )
    assert report.is_orthogonal is False
    assert report.field_collisions  # list of (field_name, existing_facet_name)
    assert any("status" in str(c) for c in report.field_collisions)


# --- Compound answerability ---

def test_rejects_when_attempted_query_returns_results(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = make_graph(make_node(
        "file:src/a.py",
        compliance=ComplianceFacet(status="planned", failing_standards=[]),
    ))
    # Proposer tries to answer "which nodes are not started yet?"
    # and their own query already works → information already in graph
    attempted_query_obj = StructuredQuery(filters=[
        FacetFilter(facet="compliance", conditions=[
            FieldCondition(field="status", op="eq", value="planned"),
        ]),
    ])
    attempted_query = attempted_query_obj.model_dump()
    proposal = FacetProposal(
        proposed_facet_name="not_started",
        question="Which nodes have not been started yet?",
        applies_to=["file"],
        proposed_fields=[{"name": "not_started", "type": "bool"}],
        attempted_query=attempted_query,
    )
    report = validate_facet_proposal(
        proposal=proposal,
        registry=registry,
        graph=graph,
        state_path=tmp_path / "state.json",
    )
    assert report.is_orthogonal is False
    assert report.query_already_answered is True
    assert "StructuredQuery" in (report.resolution_suggestion or "")


def test_accepts_when_attempted_query_returns_nothing(tmp_path: Path) -> None:
    registry = build_default_registry()
    # Graph has no nodes with model_usage facet — information genuinely absent
    graph = make_graph(make_node("file:src/a.py"))
    attempted_query_obj = StructuredQuery(filters=[
        FacetFilter(facet="model_usage", conditions=[
            FieldCondition(field="model_name", op="is_not_null"),
        ]),
    ])
    attempted_query = attempted_query_obj.model_dump()
    proposal = FacetProposal(
        proposed_facet_name="model_usage",
        question="Which AI models does this node invoke?",
        applies_to=["file"],
        proposed_fields=[{"name": "model_name", "type": "str"}],
        attempted_query=attempted_query,
    )
    report = validate_facet_proposal(
        proposal=proposal,
        registry=registry,
        graph=graph,
        state_path=tmp_path / "state.json",
    )
    assert report.is_orthogonal is True


# --- Attempt tracking ---

def test_attempt_counter_decrements_on_failure(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = nx.DiGraph()
    state_path = tmp_path / "state.json"
    proposal = FacetProposal(
        proposed_facet_name="doc_summary",
        question="What does this node do?",
        applies_to=["file"],
        proposed_fields=[],
        attempted_query=None,
    )
    report1 = validate_facet_proposal(proposal, registry, graph, state_path)
    report2 = validate_facet_proposal(proposal, registry, graph, state_path)
    assert report1.attempts_remaining == 2
    assert report2.attempts_remaining == 1


def test_attempt_counter_resets_on_success(tmp_path: Path) -> None:
    registry = build_default_registry()
    graph = nx.DiGraph()
    state_path = tmp_path / "state.json"
    proposal = FacetProposal(
        proposed_facet_name="model_usage",
        question="Which AI models does this node invoke?",
        applies_to=["file"],
        proposed_fields=[{"name": "model_name", "type": "str"}],
        attempted_query=None,
    )
    report = validate_facet_proposal(proposal, registry, graph, state_path)
    assert report.is_orthogonal is True
    assert report.attempts_remaining == 3
