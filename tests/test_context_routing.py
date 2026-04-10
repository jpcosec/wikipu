from __future__ import annotations
import networkx as nx
from pathlib import Path
import pytest
from wiki_compiler.context import get_context_bundle, ContextRequest
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity, SemanticFacet
from wiki_compiler.graph_utils import add_knowledge_node, save_graph

def test_context_routing_by_relation(tmp_path: Path):
    graph = nx.DiGraph()
    # Seed
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/seed.md", node_type="concept")
    ))
    # Ancestor (dependency)
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/ancestor.md", node_type="concept")
    ))
    # Descendant (dependent)
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/descendant.md", node_type="concept")
    ))
    
    graph.add_edge("doc:wiki/ancestor.md", "doc:wiki/seed.md", relation_type="depends_on")
    graph.add_edge("doc:wiki/seed.md", "doc:wiki/descendant.md", relation_type="depends_on")
    
    graph_path = tmp_path / "graph.json"
    save_graph(graph, graph_path)
    
    request = ContextRequest(node_ids=["doc:wiki/seed.md"], depth=1)
    bundle = get_context_bundle(graph_path, request)
    
    # Verify scoring and rationale
    node_map = {n.identity.node_id: n for n in bundle.nodes}
    assert "doc:wiki/seed.md" in node_map
    assert bundle.scores["doc:wiki/seed.md"] == 1.0
    
    assert "doc:wiki/ancestor.md" in node_map
    assert bundle.scores["doc:wiki/ancestor.md"] == 0.8
    assert "ancestor" in bundle.rationale["doc:wiki/ancestor.md"]
    
    assert "doc:wiki/descendant.md" in node_map
    assert bundle.scores["doc:wiki/descendant.md"] == 0.6
    assert "descendant" in bundle.rationale["doc:wiki/descendant.md"]
