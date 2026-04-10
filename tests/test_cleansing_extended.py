from __future__ import annotations
from pathlib import Path
import json
import networkx as nx
import pytest
from wiki_compiler.cleanser import (
    detect_cleansing_candidates, 
    apply_cleansing_proposal,
    CleansingProposal
)
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity, Edge, ComplianceFacet
from wiki_compiler.graph_utils import add_knowledge_node, save_graph

def test_apply_destroy(tmp_path: Path):
    file_path = tmp_path / "wiki/old.md"
    file_path.parent.mkdir(parents=True)
    file_path.write_text("content")
    
    proposal = CleansingProposal(
        node_id="doc:wiki/old.md",
        operation="destroy",
        rationale="stale",
        affected_nodes=["doc:wiki/old.md"]
    )
    
    apply_cleansing_proposal(proposal, tmp_path)
    assert not file_path.exists()

def test_apply_relocate(tmp_path: Path):
    old_path = tmp_path / "wiki/misplaced.md"
    old_path.parent.mkdir(parents=True)
    old_path.write_text('---\nidentity:\n  node_id: "doc:wiki/misplaced.md"\n---')
    
    new_node_id = "doc:wiki/concepts/misplaced.md"
    proposal = CleansingProposal(
        node_id="doc:wiki/misplaced.md",
        operation="relocate",
        rationale="wrong folder",
        affected_nodes=["doc:wiki/misplaced.md", new_node_id]
    )
    
    apply_cleansing_proposal(proposal, tmp_path)
    
    new_path = tmp_path / "wiki/concepts/misplaced.md"
    assert new_path.exists()
    assert not old_path.exists()
    assert f'node_id: "{new_node_id}"' in new_path.read_text()

def test_detect_misplaced_folder(tmp_path: Path):
    graph = nx.DiGraph()
    # Concept node in wiki/ (not wiki/concepts/)
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/oops.md", node_type="concept")
    ))
    graph_path = tmp_path / "graph.json"
    save_graph(graph, graph_path)
    
    report = detect_cleansing_candidates(graph_path)
    assert any(p.operation == "relocate" and "wiki/concepts/" in p.rationale for p in report.proposals)

def test_detect_stale_config(tmp_path: Path):
    graph = nx.DiGraph()
    # Config file node
    graph.add_node("file:config.json", type="file")
    # No incoming edges
    
    graph_path = tmp_path / "graph.json"
    save_graph(graph, graph_path)
    
    report = detect_cleansing_candidates(graph_path)
    assert any(p.node_id == "file:config.json" and p.operation == "destroy" for p in report.proposals)

def test_detect_orphaned_test(tmp_path: Path):
    graph = nx.DiGraph()
    # Test file node
    graph.add_node("file:tests/test_foo.py", type="file")
    # No 'covers' edge
    
    graph_path = tmp_path / "graph.json"
    save_graph(graph, graph_path)
    
    report = detect_cleansing_candidates(graph_path)
    assert any(p.node_id == "file:tests/test_foo.py" and p.operation == "destroy" for p in report.proposals)
