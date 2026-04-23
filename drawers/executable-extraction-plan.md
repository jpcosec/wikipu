---
status: open
priority: p1
depends_on:
  - drawers/kgdb-migration-plan.md
  - drawers/ontology-package-spec.md
  - drawers/diagrams/target_architecture.md
created: 2026-04-23
assigned_to: self
---

# Executable Extraction Plan

This document is the step-by-step implementation runbook for the kgdb + ontology split.
Target state is shown in `drawers/diagrams/target_architecture.md`.

Each task is small enough for one sitting. Every task ends with a test gate.
The baseline before starting: **100 tests pass, 21 pre-existing failures** (unrelated to the split).

Test gate command: `uv run pytest tests/ -q --tb=no`
Import audit command: `grep -r "from wiki_compiler\." src/kgdb/ src/ontology/ 2>/dev/null`

---

## Phase 1 — Create kgdb in-repo package

Goal: `graph_utils.py`, `query_language.py`, `query_executor.py`, and the two base contracts live in `src/kgdb/`. `wiki_compiler` imports them from there. No logic changes.

### Task 1.1 — Scaffold `src/kgdb/` package

Files to create:
- `src/kgdb/__init__.py` (empty)
- `src/kgdb/contracts/__init__.py` (empty)
- `src/kgdb/graph/__init__.py` (empty)
- `src/kgdb/query/__init__.py` (empty)

Done signal: `python -c "import kgdb"` succeeds (after `pip install -e .`).
Test gate: 100 pass, 21 fail — no change.

### Task 1.2 — Move `contracts/base.py` and `contracts/node.py` to `src/kgdb/contracts/`

Files to move:
- `src/wiki_compiler/contracts/base.py` → `src/kgdb/contracts/base.py`
- `src/wiki_compiler/contracts/node.py` → `src/kgdb/contracts/node.py`

After move:
- Add re-exports in `src/wiki_compiler/contracts/base.py` (shim): `from kgdb.contracts.base import Edge, SystemIdentity`
- Add re-exports in `src/wiki_compiler/contracts/node.py` (shim): `from kgdb.contracts.node import KnowledgeNode`
- Update `src/kgdb/contracts/__init__.py` to export `Edge`, `SystemIdentity`, `KnowledgeNode`

Done signal: `python -c "from kgdb.contracts import Edge, KnowledgeNode"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 1.3 — Move `graph_utils.py` to `src/kgdb/graph/`

File to move:
- `src/wiki_compiler/graph_utils.py` → `src/kgdb/graph/utils.py`

After move:
- Replace `src/wiki_compiler/graph_utils.py` with a shim: `from kgdb.graph.utils import *`
- Update imports inside `src/kgdb/graph/utils.py`: `from wiki_compiler.contracts import` → `from kgdb.contracts import`
- Export from `src/kgdb/graph/__init__.py`: `from kgdb.graph.utils import add_knowledge_node, load_graph, save_graph, load_knowledge_node, iter_knowledge_nodes`

Done signal: `python -c "from kgdb.graph import load_graph, save_graph"` succeeds.
Verify shim: `python -c "from wiki_compiler.graph_utils import load_graph"` still works.
Test gate: 100 pass, 21 fail — no change.

### Task 1.4 — Move `query_language.py` and `query_executor.py` to `src/kgdb/query/`

Files to move:
- `src/wiki_compiler/query_language.py` → `src/kgdb/query/language.py`
- `src/wiki_compiler/query_executor.py` → `src/kgdb/query/executor.py`

After move:
- Replace `src/wiki_compiler/query_language.py` with shim: `from kgdb.query.language import *`
- Replace `src/wiki_compiler/query_executor.py` with shim: `from kgdb.query.executor import *`
- Fix internal imports in moved files: `from wiki_compiler.contracts import` → `from kgdb.contracts import`; `from wiki_compiler.graph_utils import` → `from kgdb.graph import`
- Export from `src/kgdb/query/__init__.py`: `FieldCondition`, `FacetFilter`, `GraphScope`, `StructuredQuery`, `execute_query`

Done signal: `python -c "from kgdb.query import execute_query, StructuredQuery"` succeeds.
Verify shims: `python -c "from wiki_compiler.query_executor import execute_query"` still works.
Test gate: 100 pass, 21 fail — no change.

### Task 1.5 — Add `src/kgdb/main.py`

Create `src/kgdb/main.py` with four sub-commands:

```
kgdb get   --graph <path> --node <id>          → print KnowledgeNode as JSON
kgdb list  --graph <path>                       → print all node IDs
kgdb query --graph <path> --query-file <file>  → execute StructuredQuery JSON, print results
kgdb edges --graph <path> --node <id>          → print edges for a node
```

Wire up `[project.scripts]` in `pyproject.toml`: add `kgdb = "kgdb.main:main"`.

Done signal: `uv run kgdb list --graph knowledge_graph.json` (or any graph file) runs without error.
Test gate: 100 pass, 21 fail — no change.

---

## Phase 2 — Create ontology in-repo package

Goal: all domain knowledge modules live in `src/ontology/`. `wiki_compiler` imports them from there. No logic changes.

### Task 2.1 — Scaffold `src/ontology/` package

Files to create:
- `src/ontology/__init__.py`
- `src/ontology/contracts/__init__.py`
- `src/ontology/reasoning/__init__.py`
- `src/ontology/facets/__init__.py`
- `src/ontology/energy/__init__.py`
- `src/ontology/cleansing/__init__.py`

Done signal: `python -c "import ontology"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 2.2 — Move domain contracts to `src/ontology/contracts/`

Files to move:
- `src/wiki_compiler/contracts/facets.py` → `src/ontology/contracts/facets.py`
- `src/wiki_compiler/contracts/energy.py` → `src/ontology/contracts/energy.py`
- `src/wiki_compiler/contracts/wiki_nodes.py` → `src/ontology/contracts/wiki_nodes.py`
- `src/wiki_compiler/contracts/proposals.py` → `src/ontology/contracts/proposals.py`

After move:
- Replace each original with a shim re-exporting from `ontology.contracts.*`
- Fix internal imports in moved files: use `kgdb.contracts` for `Edge`, `KnowledgeNode`
- Update `src/ontology/contracts/__init__.py` to re-export all domain contract types

Done signal: `python -c "from ontology.contracts import IOFacet, EnergyReport, CleansingProposal"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 2.3 — Move `owl_reasoner.py` and `owl_backend/` to `src/ontology/reasoning/`

Files to move:
- `src/wiki_compiler/owl_reasoner.py` → `src/ontology/reasoning/reasoner.py`
- `src/wiki_compiler/owl_backend/` → `src/ontology/reasoning/owl_backend/`
- `src/wiki_compiler/auditor_owl.py` → `src/ontology/reasoning/auditor.py`

After move:
- Replace originals with shims re-exporting `OwlReasoner`, `OwlConflictCheck`
- Fix internal imports in moved files: `from wiki_compiler.` → `from ontology.` or `from kgdb.`
- Verify `owl_backend` imports no workspace modules

Done signal: `python -c "from ontology.reasoning import OwlReasoner, OwlConflictCheck"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 2.4 — Move `energy.py` to `src/ontology/energy/`

File to move:
- `src/wiki_compiler/energy.py` → `src/ontology/energy/audit.py`

After move:
- Replace `src/wiki_compiler/energy.py` with shim re-exporting `run_energy_audit`, `calculate_systemic_energy`, constants
- Fix internal imports: `from wiki_compiler.graph_utils import` → `from kgdb.graph import`; `from wiki_compiler.contracts import` → `from ontology.contracts import`
- Export from `src/ontology/energy/__init__.py`

Done signal: `python -c "from ontology.energy import run_energy_audit"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 2.5 — Move `cleanser.py` (detection only) to `src/ontology/cleansing/`

The detection rules belong in `ontology`. The `apply_cleansing_proposal` function executes filesystem operations — keep it in `wiki_compiler` as the execution side, fed by `ontology` detection results.

File to create:
- `src/ontology/cleansing/rules.py` ← `detect_cleansing_candidates` + all `_*_proposals` helpers
- Keep `apply_cleansing_proposal` and execution helpers (`_execute_*`) in `src/wiki_compiler/cleanser.py`
- `src/wiki_compiler/cleanser.py` imports `detect_cleansing_candidates` from `ontology.cleansing`

Done signal: `python -c "from ontology.cleansing import detect_cleansing_candidates"` succeeds.
Verify: `python -c "from wiki_compiler.cleanser import apply_cleansing_proposal"` still works.
Test gate: 100 pass, 21 fail — no change.

### Task 2.6 — Move `registry.py`, `facet_injectors.py`, `facet_validator.py` to `src/ontology/facets/`

Files to move:
- `src/wiki_compiler/registry.py` → `src/ontology/facets/registry.py`
- `src/wiki_compiler/facet_injectors.py` → `src/ontology/facets/injectors.py`
- `src/wiki_compiler/facet_validator.py` → `src/ontology/facets/validator.py`

After move:
- Replace originals with shims re-exporting `FacetRegistry`, `build_default_registry`, `ADRInjector`, `TestMapInjector`, `validate_facet_proposal`
- Fix internal imports in moved files: use `ontology.contracts` for facet types; use `kgdb` for graph primitives

Done signal: `python -c "from ontology.facets import FacetRegistry, validate_facet_proposal"` succeeds.
Test gate: 100 pass, 21 fail — no change.

### Task 2.7 — Add `src/ontology/main.py`

Create `src/ontology/main.py` with these sub-commands:

```
ontology reason          --graph <path>                → run OWL reasoner, print inferred relationships
ontology check           --graph <path>                → consistency check; exit 1 if inconsistent
ontology energy          --graph <path> --project-root <path>  → systemic energy audit
ontology cleanse detect  --graph <path>                → detect cleansing candidates
ontology inject-facets   --graph <path> --source <dir> → inject domain facets
ontology propose-facet   --proposal <file> --graph <path> → validate facet orthogonality
ontology audit-owl       --graph <path>                → OWL conflict check
```

Wire up `[project.scripts]`: add `ontology = "ontology.main:main"`.

Done signal: `uv run ontology energy --graph knowledge_graph.json --project-root .` runs without error (even if graph file doesn't exist, it should fail gracefully not crash on import).
Test gate: 100 pass, 21 fail — no change.

---

## Phase 3 — Split mixed modules

Goal: `builder.py`, `scanner.py`, and `context.py` are cleanly split between their target packages. No shims remain for the split portions — only the correct package is used.

### Task 3.1 — Split `context.py`: graph traversal → kgdb, task hydration → wiki_compiler

Identify the split point in `context.py`:
- `collect_neighborhood`, `collect_neighborhood_by_direction` → `src/kgdb/query/neighborhood.py`
- `get_context_bundle`, `match_active_tasks`, `load_relevant_checklists`, `render_context`, `render_markdown_bundle`, `match_nodes_from_task` → stay in `wiki_compiler/context.py`

After split:
- `wiki_compiler/context.py` imports neighborhood functions from `kgdb.query.neighborhood`
- No shim needed — context.py keeps the rest and calls kgdb

Done signal: `python -c "from kgdb.query.neighborhood import collect_neighborhood"` succeeds.
Verify: `python -c "from wiki_compiler.context import get_context_bundle"` still works.
Test gate: 100 pass (+ any previously failing context tests now pass), 21 or fewer fail.

### Task 3.2 — Split `scanner.py`: entity extraction → ontology, project policy → wiki_compiler

Identify the split point:
- Python AST walking, entity/symbol extraction, signature detection → `src/ontology/facets/scanner.py`
- File discovery, exclusion rules (`.wikiignore`, `exclusion/`), project-root scanning policy → stay in `wiki_compiler/scanner.py`

After split:
- `wiki_compiler/scanner.py` calls `ontology.facets.scanner` for entity extraction, handles project policy itself

Done signal: `python -c "from ontology.facets.scanner import extract_code_entities"` (or equivalent) succeeds.
Test gate: 100 pass, 21 or fewer fail.

### Task 3.3 — Split `builder.py`: edge building → ontology, wiki compilation → wiki_compiler

Identify the split point:
- `infer_reference_documents_edges`, `add_documents_edges`, `code_nodes_for_file`, `calculate_compliance_score` → `src/ontology/facets/builder.py`
- `build_wiki`, `build_directory_skeleton`, `index_markdown_files`, `parse_markdown_node`, `compile_markdown_node`, `render_compiled_markdown`, source selection, zone orchestration → stay in `wiki_compiler/builder.py`

After split:
- `wiki_compiler/builder.py` calls `ontology.facets.builder` for edge building and compliance scoring

Done signal: `python -c "from ontology.facets.builder import infer_reference_documents_edges"` succeeds.
Test gate: 100 pass, 21 or fewer fail.

---

## Phase 4 — Create adapter layer in wikipu

Goal: `wiki_compiler/main.py` and `commands/` never import `kgdb` or `ontology` internals directly. All cross-boundary calls go through `wiki_compiler/adapters/`.

### Task 4.1 — Create `src/wiki_compiler/adapters/` package

Files to create:
- `src/wiki_compiler/adapters/__init__.py`
- `src/wiki_compiler/adapters/kgdb_store.py` — wraps `kgdb.graph`: `load_graph`, `save_graph`, `add_knowledge_node`, `iter_knowledge_nodes`
- `src/wiki_compiler/adapters/kgdb_query.py` — wraps `kgdb.query`: `execute_query`, `collect_neighborhood`
- `src/wiki_compiler/adapters/ontology_energy.py` — wraps `ontology.energy`: `run_energy_audit`
- `src/wiki_compiler/adapters/ontology_cleanse.py` — wraps `ontology.cleansing`: `detect_cleansing_candidates`; and `wiki_compiler.cleanser`: `apply_cleansing_proposal`
- `src/wiki_compiler/adapters/ontology_reason.py` — wraps `ontology.reasoning`: `OwlReasoner`, `OwlConflictCheck`
- `src/wiki_compiler/adapters/ontology_facets.py` — wraps `ontology.facets`: `build_default_registry`, `validate_facet_proposal`, inject

Done signal: `python -c "from wiki_compiler.adapters import kgdb_store, ontology_energy"` succeeds.
Test gate: 100 pass, 21 or fewer fail.

### Task 4.2 — Route `commands/energy.py` and `commands/cleanse.py` through adapters

Update `commands/energy.py` to call `adapters.ontology_energy.run_energy_audit` instead of importing `energy.py` directly.
Update `commands/cleanse.py` to call `adapters.ontology_cleanse.detect` and `adapters.ontology_cleanse.apply` instead of importing `cleanser.py` directly.

Import audit: `grep -r "from wiki_compiler.energy\|from wiki_compiler.cleanser" src/wiki_compiler/commands/` should return nothing.
Test gate: 100 pass, 21 or fewer fail.

### Task 4.3 — Route `commands/build.py` and `main.py` graph I/O through adapters

Update `commands/build.py` to use `adapters.kgdb_store` for `load_graph`/`save_graph`.
Update `main.py` to use adapters for all direct `graph_utils`, `energy`, `facet_validator`, and `registry` calls.

Import audit: `grep "from wiki_compiler\.graph_utils\|from wiki_compiler\.energy\|from wiki_compiler\.registry\|from wiki_compiler\.facet_validator" src/wiki_compiler/main.py` should return nothing.
Test gate: 100 pass, 21 or fewer fail.

### Task 4.4 — Remove shims once all internal cross-boundary imports are gone

For each shim file created in Phases 1 and 2:
1. Run `grep -r "from wiki_compiler\.<module>" src/` to confirm no remaining direct imports
2. Delete the shim file
3. Run test gate

Do this module by module, not all at once.

Test gate per deletion: 100 pass, 21 or fewer fail.

---

## Phase 5 — Physical extraction (separate task, after Phase 4 is green)

Prerequisites: all shims deleted, adapter layer complete, test gate holds.

### Task 5.1 — Extract `src/kgdb/` to sibling repo

1. `mkdir -p ../kgdb/src && cp -r src/kgdb ../kgdb/src/kgdb`
2. Create `../kgdb/pyproject.toml` with `kgdb = "kgdb.main:main"` and minimal deps (`pydantic`, `networkx`)
3. Add `kgdb` as a local path dependency in `pyproject.toml`: `kgdb = {path = "../kgdb", editable = true}`
4. Remove `src/kgdb/` from this repo
5. `uv pip install -e ../kgdb`

Test gate: 100 pass, 21 or fewer fail.

### Task 5.2 — Extract `src/ontology/` to sibling repo

1. `mkdir -p ../ontology/src && cp -r src/ontology ../ontology/src/ontology`
2. Create `../ontology/pyproject.toml` with `ontology = "ontology.main:main"` and deps (`pydantic`, `networkx`, `owlready2`, `rdflib`, `kgdb`)
3. Add `ontology` as a local path dependency in `pyproject.toml`
4. Remove `src/ontology/` from this repo
5. `uv pip install -e ../ontology`

Test gate: 100 pass, 21 or fewer fail.

---

## Import law enforcement (run after each phase)

These greps should all return empty by end of Phase 4:

```bash
# kgdb must not import ontology or wiki_compiler
grep -r "from ontology\|from wiki_compiler" src/kgdb/

# ontology must not import wiki_compiler
grep -r "from wiki_compiler" src/ontology/

# wiki_compiler commands must not import kgdb/ontology internals directly
grep -r "from kgdb\.\|from ontology\." src/wiki_compiler/commands/
grep -r "from kgdb\.\|from ontology\." src/wiki_compiler/main.py

# Only adapters/ may import kgdb/ontology inside wiki_compiler
grep -rn "from kgdb\.\|from ontology\." src/wiki_compiler/ \
  | grep -v "adapters/"
```

All must be empty before Phase 5 begins.

---

## Progress tracker

| Phase | Task | Status |
|---|---|---|
| 1 | 1.1 Scaffold src/kgdb/ | not started |
| 1 | 1.2 Move base contracts | not started |
| 1 | 1.3 Move graph_utils | not started |
| 1 | 1.4 Move query_language + query_executor | not started |
| 1 | 1.5 kgdb main.py | not started |
| 2 | 2.1 Scaffold src/ontology/ | not started |
| 2 | 2.2 Move domain contracts | not started |
| 2 | 2.3 Move owl_reasoner + owl_backend + auditor_owl | not started |
| 2 | 2.4 Move energy.py | not started |
| 2 | 2.5 Split cleanser.py | not started |
| 2 | 2.6 Move registry + injectors + validator | not started |
| 2 | 2.7 ontology main.py | not started |
| 3 | 3.1 Split context.py | not started |
| 3 | 3.2 Split scanner.py | not started |
| 3 | 3.3 Split builder.py | not started |
| 4 | 4.1 Create adapters/ package | not started |
| 4 | 4.2 Route energy + cleanse commands | not started |
| 4 | 4.3 Route build + main graph I/O | not started |
| 4 | 4.4 Remove shims | not started |
| 5 | 5.1 Extract kgdb repo | not started |
| 5 | 5.2 Extract ontology repo | not started |
