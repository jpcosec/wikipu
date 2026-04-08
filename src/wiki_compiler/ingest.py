from __future__ import annotations

import re
from pathlib import Path

from .scanner import load_wikiignore_rules, match_ignore_reason


def ingest_raw_sources(
    source_dir: Path,
    dest_dir: Path,
    project_root: Path | None = None,
    overwrite: bool = False,
) -> list[Path]:
    root = project_root or source_dir.parent
    ignore_rules = load_wikiignore_rules(root / ".wikiignore")
    written: list[Path] = []
    for source_path in sorted(path for path in source_dir.rglob("*") if path.is_file()):
        if any(
            part.startswith(".") for part in source_path.relative_to(source_dir).parts
        ):
            continue
        rel_source = source_path.relative_to(root).as_posix()
        if match_ignore_reason(rel_source, ignore_rules) is not None:
            continue
        
        # New: Atomic Decomposition
        nodes = decompose_source(source_path)
        for title, content, node_type in nodes:
            draft_slug = slugify(title)
            # If multiple nodes from same source, append slug part if needed?
            # For now, slugify(title) should be unique enough within a source.
            draft_path = dest_dir / f"{draft_slug}.md"
            if draft_path.exists() and not overwrite:
                continue
            draft_path.parent.mkdir(parents=True, exist_ok=True)
            draft_path.write_text(
                render_draft(source_path, rel_source, dest_dir, draft_slug, title, content, node_type),
                encoding="utf-8",
            )
            written.append(draft_path)
    return written


def decompose_source(source_path: Path) -> list[tuple[str, str, str]]:
    """Splits a source file into atomic nodes based on headings."""
    try:
        text = source_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [(source_path.stem, f"Binary source `{source_path.name}`.", "concept")]

    # Split by ## headings
    sections = re.split(r"\n(?=## )", "\n" + text)
    nodes = []
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        lines = section.splitlines()
        if lines[0].startswith("## "):
            title = lines[0].lstrip("# ").strip()
            content = "\n".join(lines[1:]).strip()
            # Heuristic for node_type
            node_type = "concept"
            if "how to" in title.lower() or "steps" in content.lower():
                node_type = "how_to"
            elif "rule" in title.lower() or "standard" in title.lower():
                node_type = "standard"
        else:
            # First section might be the main title
            if lines[0].startswith("# "):
                title = lines[0].lstrip("# ").strip()
                content = "\n".join(lines[1:]).strip()
            else:
                title = source_path.stem.replace("_", " ").title()
                content = section
            node_type = "concept"
            
        nodes.append((title, content, node_type))
        
    return nodes


def render_draft(
    source_path: Path,
    rel_source: str,
    dest_dir: Path,
    draft_slug: str,
    title: str,
    content: str,
    node_type: str = "concept",
) -> str:
    rel_dest = draft_node_path(dest_dir, draft_slug)
    # Extract first paragraph as abstract
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    abstract = lines[0] if lines else "No abstract provided."
    
    return "\n".join(
        [
            "---",
            "identity:",
            f'  node_id: "doc:{rel_dest}"',
            f'  node_type: "{node_type}"',
            "edges:",
            f'  - {{target_id: "raw:{rel_source}", relation_type: "documents"}}',
            "compliance:",
            '  status: "planned"',
            "---",
            "",
            abstract,
            "",
            f"## Details",
            "",
            content,
            "",
            f"Generated from `{rel_source}`.",
        ]
    )


def summarize_source(source_path: Path) -> tuple[str, str]:
    try:
        text = source_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        title = source_path.stem.replace("_", " ").replace("-", " ").title()
        return title, f"Binary or non-UTF-8 source captured from `{source_path.name}`."
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    title = source_path.stem.replace("_", " ").replace("-", " ").title()
    if lines and lines[0].startswith("#"):
        title = lines[0].lstrip("# ")
        lines = lines[1:]
    summary = lines[0] if lines else f"Draft generated from `{source_path.name}`."
    return title, summary


def draft_node_path(dest_dir: Path, stem: str) -> str:
    base = dest_dir.parent.name + "/" + dest_dir.name
    return f"{base}/{slugify(stem)}.md"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return slug or "draft_node"
