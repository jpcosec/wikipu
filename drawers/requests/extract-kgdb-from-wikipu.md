---
status: open
priority: p1
assigned_to: wikipu-team
created: 2026-04-22
labels:
  - feature-request
  - architecture
  - extraction
  - modular
---

# Feature Request: Isolate kgdb from wikipu

## Context

`src/wiki_compiler/` currently stores three different kinds of truth in one place:

1. document truth
2. relation + semantic truth
3. operational curation truth

Those concerns should stop sharing the same storage and ownership boundary.

This proposal isolates the relation + semantic layer into `kgdb`, keeps document indexing in `sldb`, and keeps `wikipu` as curator of both layers.

## Clarification: Relationship with sldb

This request is complementary to the sldb requests that were moved to the `sldb` repo.

| Library | Responsibility |
|---|---|
| `sldb` | Store documents and index them as the factual corpus |
| `kgdb` | Store cross-document relations and the semantic layer above those facts |
| `wikipu` | Curate both layers through zones, workflows, and CLI |

`kgdb` does not replace `sldb`, and `sldb` does not replace `kgdb`.

```
sldb
├── documents/      ← facts
├── models/         ← contracts
└── document index  ← where facts can be found

kgdb
├── graph/          ← horizontal relations between facts
├── semantics/      ← meaning layered above facts
├── reasoning/      ← inference on top of that layer
└── query/          ← traversal and interpretation

wikipu
├── wiki/           ← curated truth surface
├── desk/           ← active curation work
├── drawers/        ← deferred curation work
└── wiki-compiler   ← curates both layers
```

## Problem

Today `wikipu` owns storage and behavior that should belong to different systems:

- document-oriented state is mixed with graph-oriented state
- graph reasoning is mixed with workspace-specific curation logic
- the CLI dispatch layer is coupled to persistence details
- extraction is harder because ownership is not written down first

## Proposal

### Store truth in the right place first

- facts about documents live in `sldb`
- horizontal relations between those facts live in `kgdb`
- semantic interpretation above those relations also lives in `kgdb`
- workspace and curation state stays in `wikipu`

### Then move code according to ownership

- modules that primarily build or interpret relation + semantic state move toward `kgdb`
- modules that primarily curate workspace state stay in `wikipu`
- mixed modules get split into storage-facing cores and curation-facing adapters

Detailed ownership audit lives in `drawers/kgdb-module-ownership-audit.md`.

## Storage Boundary

The intended storage split is:

### `sldb`

- document bodies
- document contracts and templates
- validation state
- federation metadata
- document index

### `kgdb`

- relation graph between documents and code/doc entities
- typed semantic overlays on top of those relations
- reasoning outputs
- graph-oriented query state
- graph-native reports that describe relation structure

### `wikipu`

- curated wiki surface
- active/deferred operational surfaces (`desk/`, `drawers/`)
- workflow state, gates, sessions, trails
- CLI composition and orchestration
- policies for when to consult `sldb` and `kgdb`

Detailed boundary note lives in `drawers/kgdb-storage-boundary.md`.

## Migration Sequence

### Phase 1: stabilize ownership language

- rename the extracted library to `kgdb`
- describe the split in terms of storage responsibility, not file shuffling
- classify current modules by ownership

### Phase 2: carve stable adapters inside `wikipu`

- keep `wikipu` entrypoints and workflow surfaces in place
- extract graph/semantic cores behind adapter functions
- remove direct workspace assumptions from relation-oriented code where possible

### Phase 3: extract the library physically

- create sibling package/repo `kgdb`
- move the relation + semantic modules there
- keep `wikipu` consuming `kgdb` as curator/orchestrator

### Phase 4: verify the new shape

- `sldb` still indexes documents correctly
- `kgdb` can build/query/reason about relations independently
- `wikipu` can still curate both layers through one CLI

## Deliverables for this drawer item

- `drawers/kgdb-storage-boundary.md`
- `drawers/kgdb-module-ownership-audit.md`
- `drawers/kgdb-migration-plan.md`

## Questions closed by this revision

1. **Name:** use `kgdb`
2. **Role:** `kgdb` owns horizontal relations + semantic layer, not document indexing
3. **Approach:** start with storage ownership and curation boundaries, then do the implementation split

---

Submitted by: wikipu team
Date: 2026-04-22
Affected repos: wikipu, sldb, (new: kgdb)
