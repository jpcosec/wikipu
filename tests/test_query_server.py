"""
Tests for the query_server REPL loop and submit_topology_proposal tool.
"""
from __future__ import annotations

import io
import json
import tempfile
from pathlib import Path

import networkx as nx
import pytest

from wiki_compiler.contracts import (
    ComplianceFacet,
    IOFacet,
    KnowledgeNode,
    SemanticFacet,
    SystemIdentity,
)
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.query_server import serve_structured_queries
from wiki_compiler.validator import submit_topology_proposal


# --- Helpers ---

def make_node(node_id: str, node_type: str = "file", **kwargs) -> KnowledgeNode:
    return KnowledgeNode(
        identity=SystemIdentity(node_id=node_id, node_type=node_type),
        **kwargs,
    )


def write_graph(graph: nx.DiGraph, path: Path) -> None:
    from networkx.readwrite import json_graph
    path.write_text(
        json.dumps(json_graph.node_link_data(graph)),
        encoding="utf-8",
    )


def run_server(graph_path: Path, *query_dicts: dict) -> list[dict]:
    """Feeds query dicts to serve_structured_queries and returns parsed responses."""
    lines = "\n".join(json.dumps(q) for q in query_dicts) + "\n"
    input_stream = io.StringIO(lines)
    output_stream = io.StringIO()
    serve_structured_queries(graph_path, input_stream=input_stream, output_stream=output_stream)
    output_stream.seek(0)
    return [json.loads(line) for line in output_stream if line.strip()]


# --- Tests: serve_structured_queries ---

def test_valid_query_returns_matching_nodes(tmp_path: Path) -> None:
    """A well-formed StructuredQuery filters the graph and returns matching nodes."""
    graph = nx.DiGraph()
    add_knowledge_node(
        graph,
        make_node("file:a.py", compliance=ComplianceFacet(status="planned", failing_standards=[])),
    )
    add_knowledge_node(
        graph,
        make_node("file:b.py", compliance=ComplianceFacet(status="implemented", failing_standards=[])),
    )
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    query = {
        "filters": [
            {
                "facet": "compliance",
                "conditions": [{"field": "status", "op": "eq", "value": "planned"}],
            }
        ]
    }
    responses = run_server(graph_path, query)

    assert len(responses) == 1
    response = responses[0]
    assert "nodes" in response
    node_ids = [n["identity"]["node_id"] for n in response["nodes"]]
    assert node_ids == ["file:a.py"]


def test_invalid_json_returns_error_response(tmp_path: Path) -> None:
    """Malformed JSON on stdin produces an error JSON response, not a crash."""
    graph = nx.DiGraph()
    add_knowledge_node(graph, make_node("file:x.py"))
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    bad_input = io.StringIO("this is not json\n")
    output = io.StringIO()
    serve_structured_queries(graph_path, input_stream=bad_input, output_stream=output)
    output.seek(0)
    responses = [json.loads(line) for line in output if line.strip()]

    assert len(responses) == 1
    assert "error" in responses[0]
    assert "Invalid JSON" in responses[0]["error"]


def test_invalid_structured_query_schema_returns_error(tmp_path: Path) -> None:
    """Valid JSON that doesn't conform to StructuredQuery schema returns an error response."""
    graph = nx.DiGraph()
    add_knowledge_node(graph, make_node("file:x.py"))
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    bad_query = {"filters": "not a list"}  # should be a list
    responses = run_server(graph_path, bad_query)

    assert len(responses) == 1
    assert "error" in responses[0]


def test_empty_graph_returns_empty_nodes(tmp_path: Path) -> None:
    """Query against an empty graph returns an empty nodes list."""
    graph = nx.DiGraph()
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    query = {"filters": []}
    responses = run_server(graph_path, query)

    assert responses[0]["nodes"] == []


def test_multiple_queries_processed_in_sequence(tmp_path: Path) -> None:
    """Multiple lines are each processed independently."""
    graph = nx.DiGraph()
    add_knowledge_node(
        graph,
        make_node("file:a.py", compliance=ComplianceFacet(status="planned", failing_standards=[])),
    )
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    query = {
        "filters": [
            {"facet": "compliance", "conditions": [{"field": "status", "op": "eq", "value": "planned"}]}
        ]
    }
    responses = run_server(graph_path, query, query)  # same query twice
    assert len(responses) == 2
    for r in responses:
        assert "nodes" in r


# --- Tests: submit_topology_proposal ---

def _write_proposal(path: Path, **overrides) -> None:
    base = {
        "proposed_module_name": "test_module",
        "intent": "A test module.",
        "glossary_terms_used": [],
        "proposed_inputs": [],
        "proposed_outputs": [],
    }
    base.update(overrides)
    path.write_text(json.dumps(base), encoding="utf-8")


def test_submit_topology_proposal_valid_returns_true(tmp_path: Path) -> None:
    """A well-formed proposal with no collisions returns valid=True."""
    graph = nx.DiGraph()
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    proposal_path = tmp_path / "proposal.json"
    _write_proposal(proposal_path)

    result = submit_topology_proposal(str(proposal_path), str(graph_path))

    assert result["valid"] is True
    assert result["proposal_id"] == "test_module"
    assert isinstance(result["issues"], list)


def test_submit_topology_proposal_io_collision_returns_false(tmp_path: Path) -> None:
    """A proposal that collides with an existing node's I/O port returns valid=False."""
    graph = nx.DiGraph()
    add_knowledge_node(
        graph,
        make_node(
            "file:existing.py",
            io_ports=[IOFacet(medium="disk", path_template="output/data.json")],
        ),
    )
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    proposal_path = tmp_path / "proposal.json"
    _write_proposal(
        proposal_path,
        proposed_outputs=[{"medium": "disk", "path_template": "output/data.json"}],
    )

    result = submit_topology_proposal(str(proposal_path), str(graph_path))

    assert result["valid"] is False
    assert result["proposal_id"] == "test_module"
    assert len(result["issues"]) > 0


def test_submit_topology_proposal_returns_proposal_id(tmp_path: Path) -> None:
    """The proposal_id in the result matches proposed_module_name."""
    graph = nx.DiGraph()
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    proposal_path = tmp_path / "proposal.json"
    _write_proposal(proposal_path, proposed_module_name="my_unique_module")

    result = submit_topology_proposal(str(proposal_path), str(graph_path))

    assert result["proposal_id"] == "my_unique_module"
