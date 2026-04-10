from __future__ import annotations
import networkx as nx
from pathlib import Path
import pytest
from wiki_compiler.context import get_context_bundle, ContextRequest
from wiki_compiler.contracts import KnowledgeNode, SystemIdentity
from wiki_compiler.graph_utils import add_knowledge_node, save_graph

def test_get_context_bundle_prose_hydration(tmp_path: Path):
    # 1. Create a wiki file
    wiki_dir = tmp_path / "wiki"
    wiki_dir.mkdir()
    doc_path = wiki_dir / "about.md"
    doc_path.write_text("""---
identity:
  node_id: "doc:wiki/about.md"
  node_type: "concept"
---
This is the prose content.
""", encoding="utf-8")
    
    # 2. Setup graph
    graph = nx.DiGraph()
    add_knowledge_node(graph, KnowledgeNode(
        identity=SystemIdentity(node_id="doc:wiki/about.md", node_type="concept")
    ))
    graph_path = tmp_path / "knowledge_graph.json"
    save_graph(graph, graph_path)
    
    # 3. Request context
    request = ContextRequest(node_ids=["doc:wiki/about.md"])
    bundle = get_context_bundle(graph_path, request)
    
    # 4. Verify hydration
    assert "doc:wiki/about.md" in bundle.prose
    assert "prose content" in bundle.prose["doc:wiki/about.md"]
    
    # Verify frontmatter removal in rendering
    from wiki_compiler.context import render_markdown_bundle
    markdown = render_markdown_bundle(bundle)
    assert "This is the prose content." in markdown
    assert "identity:" not in markdown
