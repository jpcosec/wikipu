"""
Tests for the query CLI commands.
"""
from __future__ import annotations

import json
from pathlib import Path

import networkx as nx
import pytest

from wiki_compiler.contracts import (
    ComplianceFacet,
    KnowledgeNode,
    SystemIdentity,
)
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.query_server import query_main


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


# --- Tests ---

def test_query_cli_issues_flags(tmp_path: Path, capsys) -> None:
    """Tests the --issues, --gaps, and --unimplemented flags for the query command."""
    graph = nx.DiGraph()
    add_knowledge_node(
        graph,
        make_node("issue:plan_docs/issues/gaps/01-a.md", node_type="doc_standard"),
    )
    add_knowledge_node(
        graph,
        make_node("issue:plan_docs/issues/unimplemented/01-b.md", node_type="doc_standard"),
    )
    add_knowledge_node(
        graph,
        make_node("file:a.py", node_type="file"),
    )
    graph_path = tmp_path / "graph.json"
    write_graph(graph, graph_path)

    # Test --issues
    query_main(graph_path, query_type=None, issues=True)
    captured = capsys.readouterr()
    result = json.loads(captured.out)
    assert len(result["nodes"]) == 2
    assert {n["identity"]["node_id"] for n in result["nodes"]} == {
        "issue:plan_docs/issues/gaps/01-a.md",
        "issue:plan_docs/issues/unimplemented/01-b.md",
    }

    # Test --gaps
    query_main(graph_path, query_type=None, gaps=True)
    captured = capsys.readouterr()
    result = json.loads(captured.out)
    assert len(result["nodes"]) == 1
    assert result["nodes"][0]["identity"]["node_id"] == "issue:plan_docs/issues/gaps/01-a.md"

    # Test --unimplemented
    query_main(graph_path, query_type=None, unimplemented=True)
    captured = capsys.readouterr()
    result = json.loads(captured.out)
    assert len(result["nodes"]) == 1
    assert result["nodes"][0]["identity"]["node_id"] == "issue:plan_docs/issues/unimplemented/01-b.md"
