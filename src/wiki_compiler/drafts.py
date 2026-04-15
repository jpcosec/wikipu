"""
Manages the delta-compile/draft-write workflow for stale wiki nodes.
"""

from __future__ import annotations

import json
from pathlib import Path

from .graph_utils import iter_knowledge_nodes, load_graph
from .manifest import load_manifest, compute_content_hash
from .ingest import ingest_raw_sources


def detect_stale_nodes(graph_path: Path, manifest_path: Path) -> list[str]:
    """Returns a list of node IDs that are stale compared to their raw sources."""
    graph = load_graph(graph_path)
    manifest = load_manifest(manifest_path)
    manifest_map = {entry.path: entry.content_hash for entry in manifest}

    stale_nodes: list[str] = []

    for node in iter_knowledge_nodes(graph):
        if not node.source:
            continue

        current_hash = manifest_map.get(node.source.source_path)
        if not current_hash:
            # Check disk directly if not in manifest
            source_file = Path(node.source.source_path)
            if source_file.exists():
                current_hash = compute_content_hash(source_file)

        if current_hash and current_hash != node.source.source_hash:
            stale_nodes.append(node.identity.node_id)

    return stale_nodes


def write_stale_drafts(
    graph_path: Path,
    manifest_path: Path,
    drafts_dir: Path,
    project_root: Path = Path("."),
) -> list[Path]:
    """Generates draft stubs for all stale nodes."""
    stale_ids = detect_stale_nodes(graph_path, manifest_path)
    if not stale_ids:
        return []

    graph = load_graph(graph_path)
    written: list[Path] = []

    # We need to know which raw sources to re-ingest
    sources_to_ingest: set[Path] = set()
    for node_id in stale_ids:
        node = [
            n for n in iter_knowledge_nodes(graph) if n.identity.node_id == node_id
        ][0]
        sources_to_ingest.add(project_root / node.source.source_path)

    for source_path in sources_to_ingest:
        # Re-ingest these specific files into drafts
        # We use a temporary dir or just ingest into drafts_dir
        # ingest_raw_sources takes a directory, so we might need a wrapper or a temporary symlink tree
        # For simplicity, let's call ingest on the parent of each source and filter
        written.extend(
            ingest_raw_sources(
                source_dir=source_path.parent,
                dest_dir=drafts_dir,
                project_root=project_root,
                overwrite=True,
                manifest_path=manifest_path,
            )
        )

    return written


def promote_draft_node(
    node_id: str, drafts_dir: Path, project_root: Path = Path(".")
) -> Path:
    """Promotes a draft node to its canonical wiki path."""
    # Find the draft file that has this node_id
    from .builder import parse_markdown_node

    for draft_file in drafts_dir.rglob("*.md"):
        node, _ = parse_markdown_node(draft_file)
        if node and node.identity.node_id == node_id:
            # If promoting from desk/drafts/, we want to update the node_id to be in wiki/
            live_node_id = node_id.replace("desk/drafts/", "wiki/")

            # Canonical path is derived from live_node_id: doc:wiki/... -> wiki/...
            rel_path = live_node_id.removeprefix("doc:")
            dest_path = project_root / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Move draft to live
            draft_content = draft_file.read_text(encoding="utf-8")

            if live_node_id != node_id:
                draft_content = draft_content.replace(
                    f'node_id: "{node_id}"', f'node_id: "{live_node_id}"'
                )

            # Update status to implemented if it was planned
            if node.compliance and node.compliance.status == "planned":
                draft_content = draft_content.replace(
                    'status: "planned"', 'status: "implemented"'
                )

            dest_path.write_text(draft_content, encoding="utf-8")
            draft_file.unlink()
            return dest_path

    raise ValueError(f"Draft node {node_id} not found in {drafts_dir}")
