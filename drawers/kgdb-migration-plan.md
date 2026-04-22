---
status: open
priority: p1
depends_on:
  - drawers/kgdb-storage-boundary.md
  - drawers/kgdb-module-ownership-audit.md
created: 2026-04-22
assigned_to: self
---

# kgdb Migration Plan

This document turns the storage boundary and module audit into an executable extraction sequence.

## Goal

Move relation + semantic ownership into `kgdb` without breaking `wikipu`'s role as curator of both the document and graph layers.

## Package Boundary

### Future `kgdb` package

Initial package surface should be organized by stored truth:

- `kgdb/contracts/` for graph contracts
- `kgdb/graph/` for graph persistence and traversal
- `kgdb/query/` for query language and execution
- `kgdb/reasoning/` for OWL and semantic inference
- `kgdb/reporting/` for graph-native reports derived from relation structure

### Remaining `wikipu` surface

Keep these as curator-facing adapters and workflows:

- CLI entrypoints
- workspace scanners and source selection
- gate/session/trail handling
- wiki/desk/drawers curation flows
- adapters that fetch from `sldb` and `kgdb`

## Adapter Entry Points To Create Inside `wikipu`

Before any repo split, create explicit adapter modules that `main.py` and `commands/` can call.

### Graph adapters

- `wikipu.adapters.kgdb_build`
- `wikipu.adapters.kgdb_query`
- `wikipu.adapters.kgdb_context`
- `wikipu.adapters.kgdb_reasoning`

These should isolate the rest of `wikipu` from internal `kgdb` layout.

### Document adapters

- `wikipu.adapters.sldb_index`
- `wikipu.adapters.sldb_documents`

These define how `wikipu` asks for facts before handing them to `kgdb`.

## Import Direction Rules

The split should enforce these rules:

- `wikipu -> sldb`
- `wikipu -> kgdb`
- `kgdb -> sldb artifacts` only through stable document/index inputs
- never `sldb -> kgdb`
- never `kgdb -> wikipu`

Inside `wikipu`, commands should import adapters, not internal graph modules directly.

## Extraction Order

### Step 1: create internal seams

- route `main.py` and command handlers through adapter functions
- isolate graph-building calls behind one `kgdb`-shaped interface
- isolate document/index retrieval behind one `sldb`-shaped interface

### Step 2: split mixed modules

First split these files in place:

- `contracts.py`
- `energy.py`
- `context.py`
- `builder.py`
- `scanner.py`
- `facet_injectors.py`

Each split should leave:

- a graph-core unit with no workspace assumptions
- a curator-facing adapter or policy layer in `wikipu`

### Step 3: move clean `kgdb` candidates

Move these once adapters exist:

- `graph_utils.py`
- `query_language.py`
- `query_executor.py`
- `owl_reasoner.py`
- `auditor_owl.py`
- `cleanser.py`

### Step 4: extract the package physically

- create sibling repo/package `kgdb`
- move the cleaned graph-core modules there
- update `wikipu` adapters to import the external package

## Test Migration Rules

- tests that verify graph storage, traversal, reasoning, or graph-native reports move to `kgdb`
- tests that verify CLI behavior, zone policy, curation flows, or workspace state stay in `wikipu`
- mixed tests should be split at the same time as mixed modules

## Done Criteria

The extraction is successful when:

- `sldb` can still index and validate documents independently
- `kgdb` can build and query a relation graph from indexed facts
- `wikipu` still presents one coherent workflow over both layers
- `wikipu` no longer imports graph internals directly outside its adapters
