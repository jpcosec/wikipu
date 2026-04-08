---
identity:
  node_id: "doc:wiki/drafts/task_8_linter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/linter.py`
- Create: `tests/test_linter.py`

- [ ] **Step 1: Write failing tests**

```python
# tests/test_linter.py
"""Tests for tag linter."""

from doc_router.config import DocRouterConfig
from doc_router.linter import lint_nodes
from doc_router.models import RouteNode


def _config() -> DocRouterConfig:
    return DocRouterConfig(
        project="test",
        domains=["ui", "pipeline"],
        stages=["match", "extract"],
        natures=["philosophy", "implementation"],
    )


def test_lint_valid_node() -> None:
    node = RouteNode(id="a", type="doc", path="a.md", domain="pipeline", stage="match", nature="philosophy")
    issues = lint_nodes([node], _config())
    assert len(issues) == 0


def test_lint_invalid_domain() -> None:
    node = RouteNode(id="a", type="doc", path="a.md", domain="WRONG", nature="philosophy")
    issues = lint_nodes([node], _config())
    assert len(issues) == 1
    assert issues[0]["type"] == "invalid_domain"


def test_lint_invalid_stage() -> None:
    node = RouteNode(id="a", type="doc", path="a.md", domain="ui", stage="WRONG", nature="philosophy")
    issues = lint_nodes([node], _config())
    assert len(issues) == 1
    assert issues[0]["type"] == "invalid_stage"


def test_lint_global_stage_always_valid() -> None:
    node = RouteNode(id="a", type="doc", path="a.md", domain="ui", stage="global", nature="philosophy")
    issues = lint_nodes([node], _config())
    assert len(issues) == 0


def test_lint_invalid_nature() -> None:
    node = RouteNode(id="a", type="doc", path="a.md", domain="ui", nature="WRONG")
    issues = lint_nodes([node], _config())
    assert len(issues) == 1
    assert issues[0]["type"] == "invalid_nature"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_linter.py -v`
Expected: FAIL

- [ ] **Step 3: Implement linter**

```python
# src/doc_router/linter.py
"""Validate tags against project vocabulary."""

from __future__ import annotations

from doc_router.config import DocRouterConfig
from doc_router.models import RouteNode

Issue = dict[str, str]


def lint_nodes(nodes: list[RouteNode], config: DocRouterConfig) -> list[Issue]:
    issues: list[Issue] = []
    valid_domains = set(config.domains)
    valid_stages = set(config.stages) | {"global"}
    valid_natures = set(config.natures)

    for node in nodes:
        if node.domain not in valid_domains:
            issues.append({
                "type": "invalid_domain",
                "node_id": node.id,
                "path": node.path,
                "value": node.domain,
                "valid": ", ".join(sorted(valid_domains)),
            })
        if node.stage not in valid_stages:
            issues.append({
                "type": "invalid_stage",
                "node_id": node.id,
                "path": node.path,
                "value": node.stage,
                "valid": ", ".join(sorted(valid_stages)),
            })
        if node.nature not in valid_natures:
            issues.append({
                "type": "invalid_nature",
                "node_id": node.id,
                "path": node.path,
                "value": node.nature,
                "valid": ", ".join(sorted(valid_natures)),
            })

    return issues
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_linter.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/linter.py tests/test_linter.py
git commit -m "feat(doc-router): vocabulary linter for tag validation"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.