---
identity:
  node_id: "doc:wiki/drafts/task_4_markdown_scanner.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/scanner/__init__.py`
- Create: `src/doc_router/scanner/markdown.py`
- Create: `tests/fixtures/sample_project/docs/design.md`
- Create: `tests/fixtures/sample_project/docs/architecture.md`
- Create: `tests/test_scanner_markdown.py`

- [ ] **Step 1: Create tagged markdown fixtures**

```markdown
<!-- tests/fixtures/sample_project/docs/design.md -->
---
id: pipeline-match-design
domain: pipeline
stage: match
nature: philosophy
implements:
  - src/module.py
  - src/module.py::MatchLogic
depends_on:
  - core-architecture
version: 2026-03-22
---

# Match Stage Design

This document describes the match stage.
```

```markdown
<!-- tests/fixtures/sample_project/docs/architecture.md -->
---
id: core-architecture
domain: core
nature: philosophy
version: 2026-03-20
---

# System Architecture

Core architecture document.
```

- [ ] **Step 2: Write failing tests**

```python
# tests/test_scanner_markdown.py
"""Tests for markdown frontmatter scanner."""

from pathlib import Path

from doc_router.scanner.markdown import scan_markdown_file, scan_markdown_dir


def test_scan_single_file(sample_project_dir: Path) -> None:
    doc = sample_project_dir / "docs" / "design.md"
    nodes, edges = scan_markdown_file(doc, sample_project_dir)
    assert len(nodes) == 1
    node = nodes[0]
    assert node.id == "pipeline-match-design"
    assert node.domain == "pipeline"
    assert node.stage == "match"
    assert node.nature == "philosophy"
    assert node.type == "doc"
    assert node.version == "2026-03-22"
    # implements → edges
    assert len(edges) >= 1
    impl_edges = [e for e in edges if e.type == "implements"]
    assert len(impl_edges) == 2
    dep_edges = [e for e in edges if e.type == "depends_on"]
    assert len(dep_edges) == 1
    assert dep_edges[0].target == "core-architecture"


def test_scan_file_without_frontmatter(tmp_path: Path) -> None:
    doc = tmp_path / "plain.md"
    doc.write_text("# No Frontmatter\n\nJust text.\n")
    nodes, edges = scan_markdown_file(doc, tmp_path)
    assert len(nodes) == 0
    assert len(edges) == 0


def test_scan_file_missing_required_fields(tmp_path: Path) -> None:
    doc = tmp_path / "bad.md"
    doc.write_text("---\ndomain: ui\n---\n# Missing id and nature\n")
    nodes, edges = scan_markdown_file(doc, tmp_path)
    # Should return empty (skip invalid) not crash
    assert len(nodes) == 0


def test_scan_directory(sample_project_dir: Path) -> None:
    docs_dir = sample_project_dir / "docs"
    nodes, edges = scan_markdown_dir(docs_dir, sample_project_dir)
    assert len(nodes) == 2  # design.md + architecture.md
    ids = {n.id for n in nodes}
    assert "pipeline-match-design" in ids
    assert "core-architecture" in ids
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_scanner_markdown.py -v`
Expected: FAIL

- [ ] **Step 4: Implement markdown scanner**

```python
# src/doc_router/scanner/__init__.py
"""File scanners for extracting doc-router tags."""

# src/doc_router/scanner/markdown.py
"""Parse YAML frontmatter from markdown files."""

from __future__ import annotations

import logging
from pathlib import Path

import yaml

from doc_router.models import RouteEdge, RouteNode

logger = logging.getLogger(__name__)

_REQUIRED_FIELDS = ("id", "domain", "nature")


def scan_markdown_file(
    path: Path, project_root: Path
) -> tuple[list[RouteNode], list[RouteEdge]]:
    text = path.read_text(encoding="utf-8")
    frontmatter = _extract_frontmatter(text)
    if frontmatter is None:
        return [], []

    missing = [f for f in _REQUIRED_FIELDS if f not in frontmatter]
    if missing:
        logger.warning("Skipping %s: missing fields %s", path, missing)
        return [], []

    rel_path = str(path.relative_to(project_root))
    node_id = frontmatter["id"]

    node = RouteNode(
        id=node_id,
        type="doc",
        path=rel_path,
        domain=frontmatter["domain"],
        stage=frontmatter.get("stage", "global"),
        nature=frontmatter["nature"],
        version=str(frontmatter["version"]) if frontmatter.get("version") else None,
    )

    edges: list[RouteEdge] = []
    for target in frontmatter.get("implements", []):
        edges.append(RouteEdge(source=node_id, target=str(target), type="implements"))
    for target in frontmatter.get("depends_on", []):
        edges.append(RouteEdge(source=node_id, target=str(target), type="depends_on"))

    return [node], edges


def scan_markdown_dir(
    directory: Path, project_root: Path
) -> tuple[list[RouteNode], list[RouteEdge]]:
    all_nodes: list[RouteNode] = []
    all_edges: list[RouteEdge] = []
    for md_file in sorted(directory.rglob("*.md")):
        nodes, edges = scan_markdown_file(md_file, project_root)
        all_nodes.extend(nodes)
        all_edges.extend(edges)
    return all_nodes, all_edges


def _extract_frontmatter(text: str) -> dict | None:
    stripped = text.strip()
    if not stripped.startswith("---"):
        return None
    end = stripped.find("---", 3)
    if end == -1:
        return None
    raw = stripped[3:end].strip()
    try:
        data = yaml.safe_load(raw)
        return data if isinstance(data, dict) else None
    except yaml.YAMLError:
        return None
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_scanner_markdown.py -v`
Expected: 4 passed

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/scanner/ tests/test_scanner_markdown.py tests/fixtures/sample_project/docs/
git commit -m "feat(doc-router): markdown frontmatter scanner"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.