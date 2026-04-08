---
identity:
  node_id: "doc:wiki/drafts/task_1_project_scaffolding.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `pyproject.toml`
- Create: `src/doc_router/__init__.py`
- Create: `src/doc_router/cli.py`

- [ ] **Step 1: Create pyproject.toml**

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
sources = ["src"]

[project]
name = "doc-router"
version = "0.1.0"
description = "Documentation-driven development framework"
requires-python = ">=3.11"
dependencies = [
    "click>=8.1",
    "pyyaml>=6.0",
    "fastapi>=0.111",
    "uvicorn>=0.30",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-asyncio>=0.23",
    "httpx>=0.27",
]

[project.scripts]
doc-router = "doc_router.cli:cli"
```

- [ ] **Step 2: Create package init**

```python
# src/doc_router/__init__.py
"""Doc-Router: Documentation-driven development framework."""

__version__ = "0.1.0"
```

- [ ] **Step 3: Create minimal CLI**

```python
# src/doc_router/cli.py
"""CLI entrypoint for doc-router."""

import click

from doc_router import __version__


@click.group()
@click.version_option(version=__version__)
def cli() -> None:
    """Documentation-driven development framework."""


@cli.command()
def init() -> None:
    """Create doc-router.yml and templates directory."""
    click.echo("doc-router init — not yet implemented")
```

- [ ] **Step 4: Install and verify**

Run: `pip install -e ".[dev]"`
Run: `doc-router --version`
Expected: `doc-router, version 0.1.0`

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml src/doc_router/__init__.py src/doc_router/cli.py
git commit -m "feat(doc-router): scaffold project with CLI entrypoint"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.