"""
Curation pipeline for draft wiki nodes: scoring quality and promoting drafts to the main wiki.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


def score_drafts(graph_path: Path, drafts_dir: Path) -> list[dict]:
    """
    Load graph, filter nodes whose node_id starts with "doc:wiki/drafts/",
    run quality checks, return ranked list (highest quality first).

    Quality signals:
      +1  non-empty abstract (not the fallback "No abstract provided.")
      +1  abstract length > 1 sentence
      +1  node_type is not the fallback default ("file")
      +1  source file still exists on disk

    Each result: {"node_id": str, "score": int, "issues": list[str]}
    """
    graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
    results = []

    for node in graph_data.get("nodes", []):
        node_id = node.get("id", "")
        if not node_id.startswith("doc:wiki/drafts/"):
            continue

        schema = node.get("schema", {})
        score, issues = _evaluate_node(node_id, schema, drafts_dir)
        results.append({"node_id": node_id, "score": score, "issues": issues})

    return sorted(results, key=lambda r: r["score"], reverse=True)


def _evaluate_node(node_id: str, schema: dict, drafts_dir: Path) -> tuple[int, list[str]]:
    """Runs quality checks on a single node schema, returns (score, issues)."""
    score = 0
    issues: list[str] = []

    # Check abstract
    abstract = _get_abstract(schema)
    if abstract and abstract != "No abstract provided.":
        score += 1
        if _sentence_count(abstract) > 1:
            score += 1
    else:
        issues.append("Missing or empty abstract.")

    # Check node_type
    node_type = schema.get("identity", {}).get("node_type", "file")
    if node_type != "file":
        score += 1
    else:
        issues.append("node_type is fallback default 'file'.")

    # Check source file existence
    draft_file = _node_id_to_file(node_id, drafts_dir)
    if draft_file is not None and draft_file.exists():
        score += 1
    else:
        issues.append("Draft file not found on disk.")

    return score, issues


def _get_abstract(schema: dict) -> str:
    """Extracts the abstract from a node schema (first line of semantics intent or raw_docstring)."""
    semantics = schema.get("semantics") or {}
    return (semantics.get("intent") or "").strip()


def _sentence_count(text: str) -> int:
    """Counts approximate number of sentences in text."""
    return len(re.findall(r"[.!?]+", text))


def _node_id_to_file(node_id: str, drafts_dir: Path) -> Path | None:
    """
    Maps a node_id like "doc:wiki/drafts/sub/slug.md" to an absolute file path
    under drafts_dir.
    """
    prefix = "doc:wiki/drafts/"
    if not node_id.startswith(prefix):
        return None
    rel = node_id[len(prefix):]
    return drafts_dir / rel


def promote_draft(node_id: str, dest: str, drafts_dir: Path, wiki_dir: Path) -> None:
    """
    Move draft node file from wiki/drafts/ to dest path in wiki/,
    rewrite node_id in frontmatter to match new path.
    Trigger is external — caller runs wiki-compiler build after.
    """
    source_file = _node_id_to_file(node_id, drafts_dir)
    if source_file is None or not source_file.exists():
        raise FileNotFoundError(f"Draft file not found for node_id '{node_id}'.")

    dest_path = wiki_dir / dest
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    content = source_file.read_text(encoding="utf-8")
    new_node_id = f"doc:wiki/{dest}"
    content = _rewrite_node_id(content, node_id, new_node_id)

    dest_path.write_text(content, encoding="utf-8")
    source_file.unlink()


def _rewrite_node_id(content: str, old_id: str, new_id: str) -> str:
    """Replaces the node_id value in YAML frontmatter."""
    return content.replace(f'node_id: "{old_id}"', f'node_id: "{new_id}"', 1)
