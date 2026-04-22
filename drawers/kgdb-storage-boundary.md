---
status: open
priority: p1
depends_on:
  - drawers/requests/extract-kgdb-from-wikipu.md
created: 2026-04-22
assigned_to: self
---

# kgdb Storage Boundary

This note defines where each kind of truth should live before any code extraction happens.

## Principle

The split is about storage responsibility first.

- `sldb` stores facts as documents and maintains an index of them.
- `kgdb` stores horizontal relations between those facts and adds semantic interpretation above them.
- `wikipu` curates both layers and decides how they are exposed to humans and agents.

## `sldb` owns

- document bodies
- document contracts and templates
- roundtrip validation
- document index
- federation metadata
- hash-integrity state

`sldb` answers: where is the fact, what schema does it obey, and is it valid?

## `kgdb` owns

- typed relations between documents, code entities, and other graph nodes
- semantic overlays that interpret those relations
- reasoning outputs derived from the graph
- graph-oriented traversal and query state
- graph-native reports built from relation structure

`kgdb` answers: how do facts relate horizontally, and what meaning emerges from those relations?

## `wikipu` owns

- curated wiki output
- `desk/` and `drawers/` operational surfaces
- gates, sessions, trails, and workflow state
- build and audit orchestration
- the user-facing CLI that curates both layers

`wikipu` answers: what should the operator see, review, and do next?

## What should not be mixed anymore

- document indexing should not be embedded in graph semantics
- workspace curation rules should not live inside graph storage modules
- relation/semantic persistence should not be treated as wiki-only state

## Recommended dependency direction

- `wikipu` may depend on `sldb`
- `wikipu` may depend on `kgdb`
- `kgdb` may consume document/index artifacts from `sldb`
- `sldb` should not depend on `kgdb`
- `kgdb` should not depend on `wikipu`

## Preferred artifact boundary

### From `sldb` to `kgdb`

- stable document identifiers
- document metadata needed for relation building
- document index exports

### From `kgdb` to `wikipu`

- graph views
- semantic views
- query results
- reasoning reports

### From `sldb` to `wikipu`

- document retrieval
- validation status
- document index and model information

## Acceptance signal

The boundary is good when:

- a document can exist in `sldb` without `kgdb`
- a graph can be rebuilt in `kgdb` from indexed facts
- `wikipu` can curate both without owning their internal persistence
