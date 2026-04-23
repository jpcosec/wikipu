---
status: open
priority: p1
depends_on:
  - drawers/kgdb-storage-boundary.md
  - drawers/kgdb-module-ownership-audit.md
created: 2026-04-22
updated: 2026-04-23
assigned_to: self
---

# kgdb Migration Plan

This document turns the storage boundary and module audit into an executable extraction sequence for the `kgdb` package specifically.

For the `ontology` package extraction plan, see `drawers/ontology-package-spec.md`.

## Goal

Move pure graph database ownership into `kgdb`: node/edge storage, base contracts, and the generic query engine. No domain knowledge crosses into this package.

## Package Boundary

### Future `kgdb` package

```
kgdb/
├── graph/          ← node/edge persistence (networkx I/O)
├── query/          ← generic structured query DSL and execution
├── contracts/      ← base graph contracts (Edge, SystemIdentity, KnowledgeNode)
└── main.py         ← kgdb CLI entrypoint
```

### `kgdb` main commands

The kgdb CLI operates on a graph file directly, with no domain knowledge:

- `kgdb get --graph <path> --node <id>` — retrieve a single node
- `kgdb list --graph <path>` — iterate all nodes
- `kgdb query --graph <path> --query-file <file>` — execute a StructuredQuery JSON
- `kgdb edges --graph <path> --node <id>` — list edges for a node

### What kgdb must NOT contain

- OWL reasoner, ontology definitions, or any owlready2 dependency
- Facet contracts beyond the base `KnowledgeNode` (no IOFacet, SemanticFacet, etc.)
- Energy, cleansing, or audit logic
- Any knowledge of wiki document types, zones, or workspace concepts

### Remaining `wikipu` surface

Keep these as curator-facing adapters and workflows:

- CLI entrypoints and all sub-commands
- workspace scanners and source selection
- gate/session/trail handling
- wiki/desk/drawers curation flows
- adapters that fetch from `sldb`, `kgdb`, and `ontology`

## Adapter Entry Points To Create Inside `wikipu`

Before any repo split, create explicit adapter modules that `main.py` and `commands/` can call.

### Graph adapters (kgdb-shaped)

- `wikipu.adapters.kgdb_store` — persist and load graphs
- `wikipu.adapters.kgdb_query` — execute structured queries
- `wikipu.adapters.kgdb_context` — fetch graph neighborhoods

These isolate the rest of `wikipu` from internal `kgdb` layout.

### Ontology adapters (ontology-shaped)

- `wikipu.adapters.ontology_reason` — run OWL reasoner
- `wikipu.adapters.ontology_energy` — run energy audit
- `wikipu.adapters.ontology_cleanse` — detect and apply cleansing
- `wikipu.adapters.ontology_facets` — inject and validate facets

### Document adapters (sldb-shaped)

- `wikipu.adapters.sldb_index`
- `wikipu.adapters.sldb_documents`

## Import Direction Rules

```
sldb        (no upstream deps)
kgdb   →   sldb artifacts only (stable inputs)
ontology →  kgdb  (uses kgdb storage and traversal)
ontology →  sldb artifacts
wikipu  →   sldb
wikipu  →   kgdb
wikipu  →   ontology
```

Forbidden:
- `kgdb → ontology` — db must not know domain
- `kgdb → wikipu`
- `ontology → wikipu`
- `sldb → anything in this system`

Inside `wikipu`, commands import adapters, not kgdb or ontology internals directly.

## Extraction Order

### Step 1: create internal seams in `wikipu`

- route `main.py` and command handlers through `wikipu.adapters.kgdb_*` functions
- route domain operations through `wikipu.adapters.ontology_*` functions
- isolate document/index retrieval behind `wikipu.adapters.sldb_*` functions
- no logic changes — just introduce the seam

### Step 2: split mixed modules

Split these files, leaving a clean kgdb-shaped core and a separate layer:

- `context.py` → `kgdb.query.neighborhood` (graph traversal) + `wikipu` (task/checklist hydration)
- `builder.py` → `ontology` (edge building, compliance scoring) + `wikipu` (wiki compilation, zone orchestration)
- `scanner.py` → `ontology` (entity extraction) + `wikipu` (project scanning policy)
- `contracts/proposals.py` → verify all types belong in ontology (none in kgdb)
- `protocols.py` → distribute to respective packages

### Step 3: move clean `kgdb` candidates

Move these once adapters exist and `context.py` has been split:

- `graph_utils.py`
- `query_language.py`
- `query_executor.py`
- `contracts/base.py`
- `contracts/node.py`

### Step 4: extract the package physically

- create sibling repo/package `kgdb` with its own `pyproject.toml` and `kgdb/main.py`
- move the cleaned graph-core modules there
- expose the `kgdb` CLI via `[project.scripts]`
- update `wikipu` adapters to import the external package

## Test Migration Rules

- tests that verify graph storage, I/O, or generic query execution move to `kgdb`
- tests that verify OWL reasoning, energy, facets, or cleansing move to `ontology`
- tests that verify CLI behavior, zone policy, curation flows, or workspace state stay in `wikipu`
- mixed tests split at the same time as mixed modules

Relevant test files for `kgdb`:
- `test_registry_and_query.py` (query execution portions)
- `test_context_routing.py` (neighborhood traversal portions)

## Done Criteria

The kgdb extraction is successful when:

- `kgdb` has no imports from `ontology`, `wikipu`, or owlready2
- `kgdb` can store, load, and query a graph given only base contracts and a graph file path
- `wikipu` accesses `kgdb` only through its adapter layer
- no `wiki_compiler` module imports `graph_utils`, `query_language`, or `query_executor` directly outside the adapters
