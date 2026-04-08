---
identity:
  node_id: "doc:wiki/drafts/task_5_python_docstring_scanner.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/scanner/python.py`
- Create: `tests/fixtures/sample_project/src/module.py`
- Create: `tests/fixtures/sample_project/src/empty.py`
- Create: `tests/test_scanner_python.py`

- [ ] **Step 1: Create tagged Python fixture**

```python
# tests/fixtures/sample_project/src/module.py
"""Sample module with doc-router tags."""


class MatchLogic:
    """Aligns candidate evidence to job requirements.

    :doc-id: pipeline-match-impl
    :domain: pipeline
    :stage: match
    :nature: implementation
    :doc-ref: pipeline-match-design
    :contract: src/nodes/match/contract.py::MatchInput
    :hitl-gate: review_match
    """

    def run(self) -> None:
        pass


class HelperClass:
    """A helper with no doc-router tags."""

    pass
```

```python
# tests/fixtures/sample_project/src/empty.py
"""Module with no doc-router tags."""


def utility() -> None:
    pass
```

- [ ] **Step 2: Write failing tests**

```python
# tests/test_scanner_python.py
"""Tests for Python docstring scanner."""

from pathlib import Path

from doc_router.scanner.python import scan_python_file, scan_python_dir


def test_scan_tagged_class(sample_project_dir: Path) -> None:
    py_file = sample_project_dir / "src" / "module.py"
    nodes, edges = scan_python_file(py_file, sample_project_dir)
    assert len(nodes) == 1
    node = nodes[0]
    assert node.id == "pipeline-match-impl"
    assert node.type == "code"
    assert node.symbol == "MatchLogic"
    assert node.domain == "pipeline"
    assert node.stage == "match"
    assert node.tags["hitl_gate"] == "review_match"
    # doc-ref → edge
    ref_edges = [e for e in edges if e.type == "doc-ref"]
    assert len(ref_edges) == 1
    assert ref_edges[0].target == "pipeline-match-design"


def test_scan_file_without_tags(sample_project_dir: Path) -> None:
    py_file = sample_project_dir / "src" / "empty.py"
    nodes, edges = scan_python_file(py_file, sample_project_dir)
    assert len(nodes) == 0


def test_scan_python_dir(sample_project_dir: Path) -> None:
    src_dir = sample_project_dir / "src"
    nodes, edges = scan_python_dir(src_dir, sample_project_dir)
    assert len(nodes) == 1  # Only MatchLogic has tags
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_scanner_python.py -v`
Expected: FAIL

- [ ] **Step 4: Implement Python scanner**

```python
# src/doc_router/scanner/python.py
"""Parse :doc-*: tags from Python docstrings."""

from __future__ import annotations

import ast
import logging
import re
from pathlib import Path

from doc_router.models import RouteEdge, RouteNode

logger = logging.getLogger(__name__)

_TAG_PATTERN = re.compile(r":(\w[\w-]*):\s*(.+)")
_EDGE_TAGS = {"doc-ref": "doc-ref", "contract": "contract"}
_META_TAGS = {"hitl-gate": "hitl_gate", "contract": "contract"}


def scan_python_file(
    path: Path, project_root: Path
) -> tuple[list[RouteNode], list[RouteEdge]]:
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (SyntaxError, UnicodeDecodeError):
        logger.warning("Could not parse %s", path)
        return [], []

    rel_path = str(path.relative_to(project_root))
    all_nodes: list[RouteNode] = []
    all_edges: list[RouteEdge] = []

    for node in ast.walk(tree):
        if not isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        docstring = ast.get_docstring(node)
        if not docstring:
            continue
        tags = _parse_doc_tags(docstring)
        if "id" not in tags:
            continue

        node_id = tags["id"]
        route_node = RouteNode(
            id=node_id,
            type="code",
            path=rel_path,
            domain=tags.get("domain", "unknown"),
            stage=tags.get("stage", "global"),
            nature=tags.get("nature", "implementation"),
            symbol=node.name,
            tags={
                meta_key: tags[tag_name]
                for tag_name, meta_key in _META_TAGS.items()
                if tag_name in tags
            },
        )
        all_nodes.append(route_node)

        if "doc-ref" in tags:
            all_edges.append(RouteEdge(source=node_id, target=tags["doc-ref"], type="doc-ref"))
        if "contract" in tags:
            all_edges.append(RouteEdge(source=node_id, target=tags["contract"], type="contract"))

    return all_nodes, all_edges


def scan_python_dir(
    directory: Path, project_root: Path
) -> tuple[list[RouteNode], list[RouteEdge]]:
    all_nodes: list[RouteNode] = []
    all_edges: list[RouteEdge] = []
    for py_file in sorted(directory.rglob("*.py")):
        nodes, edges = scan_python_file(py_file, project_root)
        all_nodes.extend(nodes)
        all_edges.extend(edges)
    return all_nodes, all_edges


def _parse_doc_tags(docstring: str) -> dict[str, str]:
    tags: dict[str, str] = {}
    for match in _TAG_PATTERN.finditer(docstring):
        key = match.group(1)
        value = match.group(2).strip()
        # Normalize: :doc-id: → "id", :doc-ref: stays as "doc-ref"
        if key == "doc-id":
            key = "id"
        tags[key] = value
    return tags
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_scanner_python.py -v`
Expected: 3 passed

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/scanner/python.py tests/test_scanner_python.py tests/fixtures/sample_project/src/
git commit -m "feat(doc-router): Python docstring tag scanner"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.