---
identity:
  node_id: "doc:wiki/standards/languages/python.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

Python-specific encoding of the CS-1 through CS-9 code style rules. All rules are supplemented by Python idioms, Pydantic-first data handling, and enforcement via ruff, docstring-coverage, and ASTFacet scanning. These rules apply to every `.py` file in any project using this system.

---

## Rule Mapping

| CS Rule | Python Equivalent | Example |
|---|---|---|
| **CS-1** — Module docstring | Triple-quoted module-level docstring immediately after `from __future__ import annotations`. One paragraph, states the module's role. | `"""Ingests raw ore files and emits structured WikiNode records."""` |
| **CS-2** — Public symbol docstring | Google-style or NumPy-style docstring on every `def` and `class` that is not prefixed with `_`. At minimum: one-line summary + `Args` + `Returns` / `Raises` sections when applicable. | See snippet below |
| **CS-3** — Typed contracts at boundaries | All inter-module data uses Pydantic `BaseModel` subclasses defined in `contracts.py`. No `dict`, no `Any`, no plain `str` carrying structured data across a module boundary. `from __future__ import annotations` at top of every module. | `def process(node: WikiNode) -> BuildResult:` |
| **CS-4** — Semantic field descriptions | Every Pydantic field carries `Field(description="...")`. The description must be a sentence explaining intent, not just repeating the field name. | `status: str = Field(description="Compliance status: 'implemented', 'planned', or 'scaffolding'.")` |
| **CS-5** — Domain exceptions | Custom exception classes defined at the top of the file (or in a dedicated `exceptions.py`). Catch-and-re-raise only typed exceptions. Never `except Exception:` for flow control. | `class IngestError(RuntimeError): ...` |
| **CS-6** — No silent errors | Use `logging.exception(...)` or `logger.error(..., exc_info=True)` before re-raising. Re-raise with `raise NewError("context") from e` to preserve the chain. Never `except ...: pass`. | `except ParseError as e: logger.error("Failed to parse %s", path); raise IngestError(path) from e` |
| **CS-7** — Non-obvious comments only | Comments explain invariants (`# node_id must be unique within the graph`) or non-obvious decisions (`# ruff disables here: generated code`). Never `# increment counter` or similar. | — |
| **CS-8** — Changelog on every change | Update `changelog.md` in the same commit as any significant change to module behavior, API shape, or data contract. | — |
| **CS-9** — Functions as classes when complex | If a function accumulates more than ~4 local variables or requires multiple passes over the same data, extract it into a class with `__call__` or named stage methods. Helpers should be private methods, not nested functions. | `class NodeBuilder: def build(self) -> WikiNode: ...` |

### CS-2 Docstring snippet

```python
def build_node(source: RawDoc, config: BuildConfig) -> WikiNode:
    """Convert a raw document into a structured wiki node.

    Args:
        source: Parsed raw document with frontmatter and body.
        config: Build-time configuration controlling output paths and validation level.

    Returns:
        A fully validated WikiNode ready for graph insertion.

    Raises:
        BuildError: If the source document is missing required frontmatter fields.
    """
```

---

## Toolchain

### ruff (linter + formatter)

Replaces flake8, isort, black, and several pylint checks in a single tool.

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = [
  "E", "W",   # pycodestyle
  "F",        # pyflakes
  "I",        # isort
  "UP",       # pyupgrade
  "ANN",      # flake8-annotations — enforces type hints on public symbols
  "D",        # pydocstyle — enforces docstrings (CS-1, CS-2)
  "B",        # flake8-bugbear
  "RUF",      # ruff-native rules
]
ignore = [
  "D105",  # missing docstring in magic method — intentional
  "D107",  # missing docstring in __init__ — covered by class docstring
]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

Run: `ruff check . && ruff format --check .`

### mypy (type checker)

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
disallow_untyped_defs = true
```

Run: `mypy src/`

### docstring-coverage

Audits that every public symbol has a docstring. Catches what ruff's `ANN` rules miss at the prose level.

```bash
docstring-coverage src/ --fail-under=100 --skip-magic --skip-init
```

### pydantic (contract enforcement)

All `BaseModel` subclasses live in `contracts.py` within their module. No data class or `TypedDict` crosses a module boundary — only Pydantic models. All fields carry `Field(description=...)`.

```python
from __future__ import annotations

from pydantic import BaseModel, Field


class WikiNode(BaseModel):
    """A single knowledge node in the wiki graph."""

    node_id: str = Field(description="Unique identifier in format 'doc:<relative_path>'.")
    node_type: str = Field(description="Artifact type: concept, doc_standard, adr, how_to, etc.")
    body: str = Field(description="Full markdown body of the node, excluding frontmatter.")
```

---

## Enforcement

| Check | Tool | Automated (CI) | Manual (Review) |
|---|---|---|---|
| CS-1 module docstring | ruff `D100`/`D104` | Yes — fails CI on missing module docstring | — |
| CS-2 public docstrings | ruff `D` rules + docstring-coverage | Yes — `--fail-under=100` | Reviewer checks prose quality |
| CS-3 typed boundaries | mypy `--strict` + ASTFacet scan | Yes — mypy in CI; ASTFacet flags untyped cross-module calls | Reviewer checks `contracts.py` structure |
| CS-4 field descriptions | ASTFacet audit | Yes — ASTFacet detects `Field()` without `description=` | Reviewer checks semantic accuracy |
| CS-5 domain exceptions | ruff `B` rules | Partial — `B904` flags bare `raise` inside `except`; custom audit for bare `Exception` | Reviewer checks exception hierarchy |
| CS-6 no silent errors | ruff `B` rules | Partial — `B007`, `B017` flag some silent patterns | Reviewer checks every `except` block |
| CS-7 comment discipline | — | Not automated | Reviewer flags narrative comments |
| CS-8 changelog | pre-commit hook | Planned — hook warns if `changelog.md` not modified in a branch with `.py` changes | Reviewer checks on PR |
| CS-9 function complexity | ruff `C901` (McCabe) | Yes — `max-complexity = 10` | Reviewer checks class extraction |
| `from __future__ import annotations` | ruff `UP` / `FA100` | Yes | — |
| Pydantic-only boundaries | ASTFacet scan | Yes | — |

### Recommended pre-commit config

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        additional_dependencies: [pydantic]
```

## Rule Schema

Each rule maps a CS rule ID to its Python-specific equivalent, the enforcement tool, and whether it is automated in CI. The Rule Mapping table above is the authoritative schema for this document.

## Fields

| Field | Description |
|---|---|
| CS Rule | The code-style rule identifier from `house_rules.md` Layer 5 |
| Python Equivalent | How the rule manifests in Python idioms and tooling |
| Enforcement Tool | The tool (ruff, mypy, docstring-coverage, ASTFacet) that checks this rule |

## Usage Examples

_See the Rule Mapping and Toolchain sections above for concrete enforcement configuration._
