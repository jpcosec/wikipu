from __future__ import annotations
import json
from pathlib import Path
from wiki_compiler.ingest import ingest_raw_sources
from wiki_compiler.builder import build_wiki, parse_markdown_node
from wiki_compiler.drafts import detect_stale_nodes, write_stale_drafts, promote_draft_node
from wiki_compiler.manifest import add_to_manifest

def test_delta_compile_workflow(tmp_path: Path):
    # 1. Setup raw source and manifest
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    source_file = raw_dir / "test.md"
    source_file.write_text("# Test Node\n\nInitial content.", encoding="utf-8")
    
    manifest_path = tmp_path / "manifests/raw_sources.csv"
    add_to_manifest(tmp_path, manifest_path, source_file)
    
    # 2. Ingest and Build
    wiki_dir = tmp_path / "wiki"
    drafts_dir = wiki_dir / "drafts"
    written = ingest_raw_sources(raw_dir, drafts_dir, project_root=tmp_path, manifest_path=manifest_path)
    
    # Promote to live
    # We need to find the node_id from the written file
    from wiki_compiler.builder import parse_markdown_node
    node, _ = parse_markdown_node(written[0])
    node_id = node.identity.node_id
    
    promote_draft_node(node_id, drafts_dir, project_root=tmp_path)
    
    live_node_id = node_id.replace("wiki/drafts/", "wiki/")
    live_file = wiki_dir.parent / Path(live_node_id.removeprefix("doc:")).as_posix()
    assert live_file.exists()
    
    graph_path = tmp_path / "knowledge_graph.json"
    build_wiki(wiki_dir, graph_path, project_root=tmp_path)
    
    # 3. Modify raw source
    source_file.write_text("# Test Node\n\nUpdated content.", encoding="utf-8")
    # Update manifest
    add_to_manifest(tmp_path, manifest_path, source_file)
    
    # 4. Detect stale
    stale_ids = detect_stale_nodes(graph_path, manifest_path)
    assert live_node_id in stale_ids
    
    # 5. Write drafts
    written_v2 = write_stale_drafts(graph_path, manifest_path, drafts_dir, project_root=tmp_path)
    assert any(p.name == "test_node.md" for p in written_v2)
    
    # 6. Promote draft
    node_v2, _ = parse_markdown_node(written_v2[0])
    promote_draft_node(node_v2.identity.node_id, drafts_dir, project_root=tmp_path)
    
    # Verify live file updated
    updated_content = live_file.read_text(encoding="utf-8")
    assert "Updated content." in updated_content
