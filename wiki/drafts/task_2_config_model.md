---
identity:
  node_id: "doc:wiki/drafts/task_2_config_model.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `src/doc_router/config.py`
- Create: `tests/conftest.py`
- Create: `tests/test_config.py`
- Create: `tests/fixtures/sample_project/doc-router.yml`

- [ ] **Step 1: Create sample config fixture**

```yaml
# tests/fixtures/sample_project/doc-router.yml
project: sample-project
domains: [ui, api, pipeline, core]
stages: [scrape, extract, match, render]
natures: [philosophy, implementation, development, testing]
doc_paths:
  central: docs/
  plans: plan/
source_paths:
  - src/
```

- [ ] **Step 2: Create conftest with fixtures**

```python
# tests/conftest.py
"""Shared test fixtures."""

from pathlib import Path

import pytest


FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_project_dir() -> Path:
    return FIXTURES_DIR / "sample_project"


@pytest.fixture
def sample_config_path(sample_project_dir: Path) -> Path:
    return sample_project_dir / "doc-router.yml"
```

- [ ] **Step 3: Write failing test for config loading**

```python
# tests/test_config.py
"""Tests for config loading and validation."""

from pathlib import Path

from doc_router.config import DocRouterConfig, load_config


def test_load_valid_config(sample_config_path: Path) -> None:
    config = load_config(sample_config_path)
    assert config.project == "sample-project"
    assert "pipeline" in config.domains
    assert "match" in config.stages
    assert "philosophy" in config.natures
    assert config.doc_paths["central"] == "docs/"
    assert config.source_paths == ["src/"]


def test_load_config_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "doc-router.yml"
    try:
        load_config(missing)
        assert False, "Should have raised"
    except FileNotFoundError:
        pass


def test_config_validates_required_fields(tmp_path: Path) -> None:
    bad_config = tmp_path / "doc-router.yml"
    bad_config.write_text("project: test\n")
    try:
        load_config(bad_config)
        assert False, "Should have raised"
    except ValueError as e:
        assert "domains" in str(e)
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `python -m pytest tests/test_config.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'doc_router.config'`

- [ ] **Step 5: Implement config module**

```python
# src/doc_router/config.py
"""Load and validate doc-router.yml configuration."""

from dataclasses import dataclass, field
from pathlib import Path

import yaml


_REQUIRED_FIELDS = ("project", "domains", "stages", "natures")


@dataclass(frozen=True)
class DocRouterConfig:
    project: str
    domains: list[str]
    stages: list[str]
    natures: list[str]
    doc_paths: dict[str, str] = field(default_factory=lambda: {"central": "docs/"})
    source_paths: list[str] = field(default_factory=lambda: ["src/"])
    template_paths: dict[str, str] = field(default_factory=dict)


def load_config(path: Path) -> DocRouterConfig:
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise ValueError(f"Invalid config format in {path}")

    missing = [f for f in _REQUIRED_FIELDS if f not in raw]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    return DocRouterConfig(
        project=raw["project"],
        domains=raw["domains"],
        stages=raw["stages"],
        natures=raw["natures"],
        doc_paths=raw.get("doc_paths", {"central": "docs/"}),
        source_paths=raw.get("source_paths", ["src/"]),
        template_paths=raw.get("templates", {}),
    )
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python -m pytest tests/test_config.py -v`
Expected: 3 passed

- [ ] **Step 7: Commit**

```bash
git add src/doc_router/config.py tests/conftest.py tests/test_config.py tests/fixtures/
git commit -m "feat(doc-router): config loading and validation"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.