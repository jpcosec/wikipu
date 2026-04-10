from __future__ import annotations
import json
from pathlib import Path
import networkx as nx
import pytest
from wiki_compiler.perception import build_status_report, classify_perturbation
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity, GitFacet
from wiki_compiler.graph_utils import add_knowledge_node, save_graph
from wiki_compiler.gates import add_gate

def test_classify_perturbation():
    assert classify_perturbation("modified_node", "doc:wiki/foo.md") == "rebuild_graph"
    assert classify_perturbation("modified_node", "file:src/main.py") == "rebuild_graph_and_audit"
    assert classify_perturbation("untracked_raw", "raw/note.md") == "ingest_raw_source"

def test_build_status_report_with_gates(tmp_path: Path):
    # Setup graph with one tracked node
    graph = nx.DiGraph()
    node = KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/test.md", node_type="concept"),
        git=GitFacet(blob_sha="old-sha", status="tracked")
    )
    add_knowledge_node(graph, node)
    graph_path = tmp_path / "knowledge_graph.json"
    save_graph(graph, graph_path)
    
    # Create the file on disk so it exists but sha differs (if we had git)
    # Since we use subprocess 'git hash-object', this test might be tricky without a real git repo.
    # But we can at least test the gate perception part.
    
    gates_path = tmp_path / "desk/Gates.md"
    gates_path.parent.mkdir(parents=True)
    add_gate(gates_path, "desk/proposals/p1.md", "test gate")
    
    # Mock untracked raw
    raw_file = tmp_path / "raw/new.md"
    raw_file.parent.mkdir(exist_ok=True)
    raw_file.write_text("content")
    
    # Note: build_status_report calls 'git' commands. 
    # In this environment, we might need to mock them or just verify the gate logic.
    report = build_status_report(graph_path, tmp_path)
    
    assert "open_gates" in report
    assert len(report["open_gates"]) == 1
    assert report["open_gates"][0]["gate_id"] == "gate-001"
    
    # Verify perturbations include the gate
    p_types = [p["type"] for p in report["perturbations"]]
    assert "open_gate" in p_types
