from __future__ import annotations
import json
import networkx as nx
from pathlib import Path
import pytest
from wiki_compiler.context import get_context_bundle, ContextRequest
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity, SemanticFacet
from wiki_compiler.graph_utils import add_knowledge_node, save_graph

def test_get_context_bundle_contract(tmp_path: Path):
    graph = nx.DiGraph()
    # Node 1
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/a.md", node_type="concept"),
        semantics=SemanticFacet(intent="Intent A", raw_docstring=None)
    ))
    # Node 2
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/b.md", node_type="concept"),
        semantics=SemanticFacet(intent="Intent B", raw_docstring=None)
    ))
    graph.add_edge("doc:wiki/a.md", "doc:wiki/b.md", relation_type="depends_on")
    
    graph_path = tmp_path / "graph.json"
    save_graph(graph, graph_path)
    
    request = ContextRequest(node_ids=["doc:wiki/a.md"], depth=1)
    bundle = get_context_bundle(graph_path, request)
    
    assert len(bundle.nodes) == 2
    assert any(n.identity.node_id == "doc:wiki/a.md" for n in bundle.nodes)
    assert any(n.identity.node_id == "doc:wiki/b.md" for n in bundle.nodes)
    assert len(bundle.edges) == 1
    assert bundle.edges[0].target_id == "doc:wiki/b.md"
    assert bundle.rationale["doc:wiki/a.md"] == "direct_match"
    assert bundle.rationale["doc:wiki/b.md"] == "descendant_of_doc:wiki/a.md"
