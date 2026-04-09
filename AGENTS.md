# AGENTS Guide

This repository is a Python package named `llm-wiki-compiler` with the runtime code in `src/wiki_compiler/`.

Agents working here should optimize for small, reversible changes that preserve the repo's knowledge-graph and wiki conventions.

## Quick Facts
- Python requirement: `>=3.10` from `pyproject.toml`.
- Main package: `src/wiki_compiler/`.
- Secondary package: `src/wikipu/`.
- Tests live in `tests/` and use `pytest`.
- CLI entrypoint: `wiki-compiler`.
- Canonical documentation: `README.md`, `wiki/`, and `wiki/standards/00_house_rules.md`.
- Changelog updates are expected for significant changes.

## Setup Commands
- Install editable package: `pip install -e .`
- Show CLI help: `wiki-compiler --help`
- Alternative CLI entry: `python -m wiki_compiler.main --help`

## Build Commands
- Main graph build: `wiki-compiler build`
- Explicit build inputs: `wiki-compiler build --source wiki --graph knowledge_graph.json --project-root . --code-root src`
- Recompute and refresh baseline: `wiki-compiler build --update-baseline`
- Ingest raw notes into wiki drafts: `wiki-compiler ingest`
- Audit the built graph: `wiki-compiler audit`
- Render focused graph context: `wiki-compiler context --nodes "doc:wiki/index.md"`

## Test Commands
- Full suite: `python -m pytest -q`
- Verbose suite: `python -m pytest`
- Single file: `python -m pytest tests/test_query_server.py -q`
- Single test: `python -m pytest tests/test_query_server.py::test_valid_query_returns_matching_nodes -q`
- Filter by expression: `python -m pytest -k query -q`
- Stop after first failure: `python -m pytest -x -q`

## Current Test Status
- Verified on 2026-04-09: `python -m pytest -q` runs, but the suite is not fully green.
- Known failure: `tests/test_wiki_construction.py::test_default_registry_has_standard_templates`.
- Failure cause: the test still expects `standard`, while the codebase now uses `doc_standard`.
- If you are touching template logic, run `tests/test_wiki_construction.py` first.

## Lint / Formatting Commands
- There is no root-level, repo-enforced lint command configured in `pyproject.toml`.
- There is no checked-in `ruff`, `mypy`, `black`, `isort`, `tox`, or `nox` configuration at the repo root.
- The practical verification baseline today is `python -m pytest -q` plus targeted CLI checks.
- If you add or use external lint tooling, treat it as advisory unless the user asks for broader cleanup.

## Suggested Non-Canonical Checks
- CLI smoke test: `wiki-compiler build` and `wiki-compiler audit`
- Focused regression run after scanner work: `python -m pytest tests/test_runtime_features.py -q`
- Focused regression run after query work: `python -m pytest tests/test_query_server.py tests/test_registry_and_query.py -q`

## Repository Layout
- `src/wiki_compiler/`: main compiler, scanner, graph, query, and CLI code.
- `src/wikipu/`: helper decorators used by scanned source examples.
- `tests/`: pytest suite.
- `wiki/`: current truth and standards.
- `wiki/how_to/`: canonical operational guides for graph usage, planning, design, documentation, and research.
- `wiki/issues_guide.md`: canonical issue lifecycle and indexing process.
- `raw/`: source material; read-only for agents.
- `plan_docs/`: active planning artifacts.
- `future_docs/`: deferred ideas.
- `knowledge_graph.json`: generated graph artifact.
- `.compliance_baseline.json`: build baseline artifact.

## High-Level Architecture
- `main.py` wires the CLI and dispatches subcommands.
- `builder.py` builds the graph from wiki markdown and scanned Python code.
- `scanner.py` parses Python AST and emits `KnowledgeNode` objects.
- `contracts.py` defines the Pydantic models used as the shared schema layer.
- `query_language.py`, `query_executor.py`, and `query_server.py` implement graph querying.
- `validator.py`, `facet_validator.py`, and `registry.py` enforce orthogonality and proposal rules.

## Using The Graph
- The graph is the primary navigation surface for agents; do not start with broad directory wandering when the question is structural.
- Rebuild it with `wiki-compiler build` when wiki or source structure may be stale.
- Query single nodes with `wiki-compiler query --type get_node --node-id <node_id>`.
- Traverse relationships with `wiki-compiler query --type get_ancestors --node-id <node_id>` and `wiki-compiler query --type get_descendants --node-id <node_id>`.
- Use `wiki-compiler context --nodes "<node_id>"` for focused context instead of reading many files.
- Common node IDs include `doc:wiki/...`, `file:src/...`, and `code:src/...`.
- Key edge types include `contains`, `depends_on`, `documents`, `transcludes`, and `implements`.
- Canonical guidance lives in `wiki/how_to/use_the_graph.md` and `wiki/knowledge_node_facets.md`.

## Working With Issues
- Active issues live under `plan_docs/issues/`, usually in `plan_docs/issues/gaps/` and `plan_docs/issues/unimplemented/`.
- The first file to inspect is `plan_docs/issues/Index.md`, which is the subagent entrypoint generated from the issue graph.
- Use `wiki/issues_guide.md` as the canonical source for issue format, atomization, contradiction checks, dependency mapping, and resolution lifecycle.
- Use `wiki/how_to/plan.md` for the operational planning workflow that points back to the issue guide.
- Issue files are ephemeral: when resolved, delete the issue file, remove it from `plan_docs/issues/Index.md`, and record lasting design decisions in `wiki/adrs/` when needed.
- `future_docs/` holds deferred ideas, not active implementation issues.

## Core Style Rules
- Prefer small, explicit functions over large control-heavy ones.
- If a function needs many local variables or multiple phases, extract helpers or a small class.
- Keep code self-explanatory; comments are for invariants or non-obvious decisions only.
- Update `changelog.md` for significant behavioral, schema, CLI, or documentation changes.
- Preserve existing user changes; do not revert unrelated work.

## Python File Conventions
- Start modules with a module docstring.
- Prefer `from __future__ import annotations` at the top of Python files.
- Use UTF-8 file reads and writes, typically via `Path.read_text()` and `Path.write_text()`.
- Prefer `pathlib.Path` over raw string paths.
- Keep public functions and classes documented with concise docstrings.
- Match the local file style when editing older modules unless the task requires normalization.

## Imports
- Prefer grouped imports in this order: standard library, third-party, local package.
- Keep one import per line when that improves readability.
- Favor explicit imports over wildcard imports.
- Avoid introducing circular imports across `wiki_compiler` modules.
- If a contract is shared across modules, put it in `contracts.py` instead of duplicating a shape locally.

## Types and Data Contracts
- Treat Pydantic models as the canonical module-boundary contract.
- Do not pass untyped `dict` payloads across module boundaries when a model is appropriate.
- Add `Field(description=...)` to Pydantic fields you introduce.
- Use precise union syntax like `str | None`.
- Keep literals and enums narrow when the domain is closed.
- Preserve schema compatibility unless the change explicitly updates callers and tests.

## Naming Conventions
- Functions, variables, and modules: `snake_case`.
- Classes and Pydantic models: `PascalCase`.
- Constants and regex patterns: `UPPER_SNAKE_CASE`.
- Test functions: `test_<behavior>()`.
- Prefer names that describe domain intent, not implementation trivia.

## Error Handling
- Do not silently swallow exceptions.
- Raise typed, domain-appropriate exceptions when adding new failure modes.
- When translating exceptions, preserve causality with `raise NewError(...) from exc`.
- Include enough context in error messages for CLI users and future agents.
- Avoid using generic `Exception` for control flow.

## Testing Style
- Favor deterministic unit tests with direct function calls.
- Use `tmp_path` for filesystem scenarios.
- Keep test fixtures lightweight and local to the test file unless reuse is clear.
- Use helper writers like `write(path, content)` when many tests need scratch files.
- Assert on observable behavior and schema outputs, not internal implementation details.

## Working With The Wiki
- `wiki/` is current truth; keep it aligned with code.
- `raw/` is immutable input; agents read it but should not write to it.
- New or changed wiki nodes should still pass `wiki-compiler build` and, when relevant, `wiki-compiler audit`.
- Respect the node templates and compliance semantics in `wiki/standards/`.
- Use `doc_standard` rather than the older `standard` node type.

## Documentation Rules To Remember
- `README.md` is the top-level entry document.
- General documentation should live in the appropriate documentation area, and module-specific docs should stay close to the module they describe.
- In this repo, the canonical knowledge/documentation system is primarily the `wiki/` tree.
- Significant repo changes should be recorded in `changelog.md`.

## Agent Workflow Advice
- Read the nearest tests before changing behavior.
- Prefer targeted test runs before full-suite runs.
- For CLI or graph-schema work, validate with both tests and a CLI smoke check.
- Avoid broad reformatting in files you were not asked to clean up.
- Keep changes atomic and easy to review.

## Cursor / Copilot Rules
- No `.cursorrules` file was found at the repo root.
- No `.cursor/rules/` directory was found at the repo root.
- No `.github/copilot-instructions.md` file was found.
- Do not assume hidden editor-specific instructions beyond what is checked into this repository.

## Safe Defaults For Future Agents
- Default to `python -m pytest <target> -q` for verification.
- Default to `wiki-compiler build` after changing wiki structure, scanner behavior, or graph generation.
- Default to narrow, typed changes in `contracts.py` when introducing new shared data.
- Default to updating `changelog.md` when the change would matter to another developer or agent.
