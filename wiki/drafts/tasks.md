---
identity:
  node_id: "doc:wiki/drafts/tasks.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md", relation_type: "documents"}
---

### Task 1: Extend config with plan_paths

## Details

### Task 1: Extend config with plan_paths

**Files:**
- Modify: `src/doc_router/config.py`
- Modify: `tests/test_config.py`
- Modify: `tests/fixtures/sample_project/doc-router.yml`

- [ ] **Step 1: Write the failing test**

Add to `tests/test_config.py`:

```python
def test_load_config_with_plan_paths(sample_config_path: Path) -> None:
    """Config should parse plan_paths from YAML."""
    config = load_config(sample_config_path)
    assert hasattr(config, "plan_paths")
    assert config.plan_paths == {"plans": "docs/plans/"}


def test_load_config_default_plan_paths(tmp_path: Path) -> None:
    """Config should default plan_paths when not specified."""
    cfg_file = tmp_path / "doc-router.yml"
    cfg_file.write_text(
        "project: test\ndomains: [a]\nstages: [b]\nnatures: [c]\n"
    )
    config = load_config(cfg_file)
    assert config.plan_paths == {"plans": "docs/plans/"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_config.py -v -k "plan_paths"`
Expected: FAIL — `DocRouterConfig` has no `plan_paths` attribute

- [ ] **Step 3: Implement**

In `src/doc_router/config.py`, add `plan_paths` field to `DocRouterConfig`:

```python
@dataclass(frozen=True)
class DocRouterConfig:
    project: str
    domains: list[str]
    stages: list[str]
    natures: list[str]
    doc_paths: dict[str, str] = field(default_factory=lambda: {"central": "docs/"})
    source_paths: list[str] = field(default_factory=lambda: ["src/"])
    template_paths: dict[str, str] = field(default_factory=dict)
    plan_paths: dict[str, str] = field(default_factory=lambda: {"plans": "docs/plans/"})
```

In `load_config`, add parsing:

```python
    plan_paths=raw.get("plan_paths", {"plans": "docs/plans/"}),
```

Update `tests/fixtures/sample_project/doc-router.yml` to add:

```yaml
plan_paths:
  plans: docs/plans/
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_config.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/config.py tests/test_config.py tests/fixtures/sample_project/doc-router.yml
git commit -m "feat(doc-router): add plan_paths to config"
```

---

### Task 2: Plans module — plan discovery and iteration chain

**Files:**
- Create: `src/doc_router/plans.py`
- Create: `tests/test_plans.py`
- Create: `tests/fixtures/sample_project/docs/plans/test-feature/plan_test-feature_0.md`
- Create: `tests/fixtures/sample_project/docs/plans/test-feature/review_test-feature_0.md`

- [ ] **Step 1: Create fixture plan files**

`tests/fixtures/sample_project/docs/plans/test-feature/plan_test-feature_0.md`:

```markdown
---
id: plan-test-feature-0
domain: pipeline
stage: extract
nature: development
type: plan
group: test-feature
version: 0
parent: null
status: active
touches:
  - path: src/nodes/extract/logic.py
    symbol: run_logic
  - path: docs/architecture.md
---

# Test Feature Plan

This is a test plan for the extract pipeline.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md`.