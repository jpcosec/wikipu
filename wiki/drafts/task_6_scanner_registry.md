---
identity:
  node_id: "doc:wiki/drafts/task_6_scanner_registry.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/scanner/registry.py`

- [ ] **Step 1: Write failing test**

Add to `tests/test_scanner_python.py` or create a new file:

```python
# tests/test_scanner_registry.py
"""Tests for scanner registry."""

from pathlib import Path

from doc_router.scanner.registry import scan_project
from doc_router.config import load_config


def test_scan_project_finds_all_entities(sample_project_dir: Path) -> None:
    config = load_config(sample_project_dir / "doc-router.yml")
    nodes, edges = scan_project(sample_project_dir, config)
    # 2 docs (design.md, architecture.md) + 1 code (MatchLogic)
    assert len(nodes) == 3
    types = {n.type for n in nodes}
    assert types == {"doc", "code"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_scanner_registry.py -v`
Expected: FAIL

- [ ] **Step 3: Implement registry**

```python
# src/doc_router/scanner/registry.py
"""Scan a project by dispatching to file-type-specific scanners."""

from __future__ import annotations

from pathlib import Path

from doc_router.config import DocRouterConfig
from doc_router.models import RouteEdge, RouteNode
from doc_router.scanner.markdown import scan_markdown_dir
from doc_router.scanner.python import scan_python_dir


def scan_project(
    project_root: Path, config: DocRouterConfig
) -> tuple[list[RouteNode], list[RouteEdge]]:
    all_nodes: list[RouteNode] = []
    all_edges: list[RouteEdge] = []

    # Scan doc paths
    for doc_dir in config.doc_paths.values():
        full_path = project_root / doc_dir
        if full_path.is_dir():
            nodes, edges = scan_markdown_dir(full_path, project_root)
            all_nodes.extend(nodes)
            all_edges.extend(edges)

    # Scan source paths
    for src_dir in config.source_paths:
        full_path = project_root / src_dir
        if full_path.is_dir():
            nodes, edges = scan_python_dir(full_path, project_root)
            all_nodes.extend(nodes)
            all_edges.extend(edges)

    return all_nodes, all_edges
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_scanner_registry.py -v`
Expected: 1 passed

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/scanner/registry.py tests/test_scanner_registry.py
git commit -m "feat(doc-router): scanner registry dispatches by file type"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.