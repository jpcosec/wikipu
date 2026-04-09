# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Reference

The authoritative agent guide is `AGENTS.md` — read it first. It contains setup commands, all CLI commands, test commands, architecture overview, and detailed style/naming/testing conventions. This file supplements it with Claude Code-specific guidance.

## Setup

```bash
pip install -e .          # Install editable package
wiki-compiler --help      # Verify CLI is available
```

## Key Commands

```bash
python -m pytest -q                              # Full test suite
python -m pytest tests/test_<module>.py -q      # Single file
python -m pytest -k <expression> -q             # Filter by name
python -m pytest -x -q                          # Stop on first failure

wiki-compiler build                             # Rebuild knowledge_graph.json
wiki-compiler audit                             # Check graph compliance
wiki-compiler check-workflow                    # Validate issue/branch/changelog discipline
wiki-compiler query --type get_node --node-id <id>  # Graph lookup
wiki-compiler context --nodes "<node_id>"       # Focused context for a node
```

## Known Broken Test

`tests/test_wiki_construction.py::test_default_registry_has_standard_templates` expects `standard` but the codebase now uses `doc_standard`. Do not fix this test unless you are explicitly addressing template normalization.

## Architecture at a Glance

- `src/wiki_compiler/main.py` — CLI dispatcher
- `src/wiki_compiler/contracts.py` — all shared Pydantic models (single source of truth for schemas)
- `src/wiki_compiler/builder.py` — builds `knowledge_graph.json` from wiki markdown + scanned Python
- `src/wiki_compiler/scanner.py` — parses Python AST → `KnowledgeNode` objects
- `src/wiki_compiler/query_language.py`, `query_executor.py`, `query_server.py` — graph query system
- `src/wiki_compiler/validator.py`, `facet_validator.py`, `registry.py` — orthogonality and proposal enforcement
- `src/wiki_compiler/perception.py` — contextual perception layer
- `src/wiki_compiler/cleanser.py` — cleansing proposals and gate logic

## The Four-Zone Rule (ID-4)

| Zone | Purpose | Agents may write? |
|---|---|---|
| `wiki/` | Current truth | Yes (curated) |
| `raw/` | Immutable source ore | No |
| `plan_docs/` | Active issues/proposals | Yes (ephemeral) |
| `future_docs/` | Deferred backlog | Yes (low-churn) |

`wiki/` may never reference `plan_docs/` or `future_docs/`. Zones above may not be written to by zones below.

## Issue Workflow (OP-4)

1. Active issues: `plan_docs/issues/` (start at `plan_docs/issues/Index.md`)
2. When resolving: update/delete tests → run tests → update `changelog.md` → delete issue file → remove from `Index.md` → commit
3. Branch naming: `issue/<name>` or `phase/<n>`; work never happens directly on `main`
4. Run `wiki-compiler check-workflow` before committing

## Critical Invariants

- **No untyped dicts across module boundaries** — use Pydantic models from `contracts.py`
- **`Field(description=...)` required** on every Pydantic field you introduce
- **`changelog.md` updated** for every significant behavioral, schema, CLI, or doc change
- **`wiki-compiler build`** must pass after any change to wiki structure, scanner, or graph generation
- Graph is the navigation surface — query it (`wiki-compiler query`) instead of scanning directories
