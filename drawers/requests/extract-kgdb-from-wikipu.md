---
status: open
priority: p1
assigned_to: wikipu-team
created: 2026-04-22
updated: 2026-04-23
labels:
  - feature-request
  - architecture
  - extraction
  - modular
---

# Feature Request: Isolate kgdb and ontology from wikipu

## Context

`src/wiki_compiler/` currently stores four different kinds of truth in one place:

1. document truth
2. graph storage and traversal
3. domain knowledge and semantic interpretation
4. operational curation truth

Those concerns should stop sharing the same boundary.

This proposal isolates the graph database layer into `kgdb`, the domain knowledge and semantic layer into `ontology`, keeps document indexing in `sldb`, and keeps `wikipu` as curator of all three layers.

## Four-Layer Model

| Library | Responsibility |
|---|---|
| `sldb` | Store documents and index them as the factual corpus |
| `kgdb` | Store and traverse cross-document relations — pure graph database |
| `ontology` | Apply domain knowledge above the graph: OWL reasoning, facets, energy, cleansing rules |
| `wikipu` | Curate all three layers through zones, workflows, and CLI |

`kgdb` is a database. It does not know what a facet means, what energy is, or how to reason about OWL classes. `ontology` uses `kgdb` as its storage and traversal engine, adding the domain-specific interpretation layer on top.

```
sldb
├── documents/      ← facts
├── models/         ← contracts
└── document index  ← where facts can be found

kgdb
├── graph/          ← node/edge storage (networkx persistence)
└── query/          ← generic traversal and structured query engine

ontology
├── facets/         ← domain facet definitions, registry, injection, validation
├── reasoning/      ← OWL reasoner and consistency checking
├── energy/         ← systemic energy metrics and drift detection
├── cleansing/      ← domain-aware structural cleansing rules
└── wiki_nodes/     ← document type taxonomy and domain contracts

wikipu
├── wiki/           ← curated truth surface
├── desk/           ← active curation work
├── drawers/        ← deferred curation work
└── wiki-compiler   ← curates all layers
```

## Problem

Today `wikipu` owns storage and behavior that should belong to different systems:

- graph database primitives are mixed with domain facet logic
- OWL reasoning and energy metrics are treated as graph-database concerns
- domain cleansing rules (which know about tests, plans, and config files) live inside what should be a generic storage layer
- the CLI dispatch layer is coupled to persistence and domain details simultaneously
- extraction is harder because ownership is not written down first

## Proposal

### Store truth in the right place first

- facts about documents live in `sldb`
- horizontal relations between those facts live in `kgdb` (raw graph, no semantics)
- semantic interpretation and domain rules above those relations live in `ontology`
- workspace and curation state stays in `wikipu`

### Then move code according to ownership

- modules that primarily store or traverse raw graph state move toward `kgdb`
- modules that interpret graph state through domain knowledge move toward `ontology`
- modules that primarily curate workspace state stay in `wikipu`
- mixed modules get split into their respective cores and curator-facing adapters

Detailed ownership audit lives in `drawers/kgdb-module-ownership-audit.md`.
Execution follow-up now lives in `desk/tasks/Board.md`, with energy re-ownership tracked in `desk/tasks/136-keep-energy-in-wikipu.md`.

## Storage Boundary

### `sldb`

- document bodies
- document contracts and templates
- validation state
- federation metadata
- document index

### `kgdb`

- node and edge persistence (networkx graph serialization)
- node/edge base contracts (Edge, SystemIdentity, KnowledgeNode)
- generic structured query DSL and execution engine
- graph I/O primitives

### `ontology`

- OWL backend, reasoner, and consistency checking
- domain facet contracts (IOFacet, ASTFacet, SemanticFacet, ADRFacet, TestMapFacet, ComplianceFacet, SourceFacet, GitFacet)
- facet registry, injection, and validation
- domain contracts, excluding the energy lane that is being moved back into `wikipu`
- domain cleansing rules and proposals
- wiki document type taxonomy (ConceptDoc, HowToDoc, ADRDoc, etc.)
- audit findings and topology proposal contracts

### `wikipu`

- curated wiki surface
- active/deferred operational surfaces (`desk/`, `drawers/`)
- workflow state, gates, sessions, trails
- CLI composition and orchestration
- policies for when to consult `sldb`, `kgdb`, and `ontology`

Detailed boundary note lives in `drawers/kgdb-storage-boundary.md`.

## Migration Sequence

### Phase 1: stabilize ownership language

- rename the extracted graph library to `kgdb`
- introduce `ontology` as the domain knowledge package
- describe each split in terms of storage and interpretation responsibility
- classify current modules by ownership (done in audit)

### Phase 2: carve stable adapters inside `wikipu`

- keep `wikipu` entrypoints and workflow surfaces in place
- extract graph/db cores behind `kgdb`-shaped adapter functions
- extract domain/semantic cores behind `ontology`-shaped adapter functions
- remove direct workspace assumptions from relation-oriented and reasoning code

### Phase 3: extract both libraries physically

- create sibling package/repo `kgdb` with its own `main`
- create sibling package/repo `ontology` with its own `main`
- move the graph-db modules to `kgdb`
- move the domain knowledge modules to `ontology`
- keep `wikipu` consuming both as curator/orchestrator

### Phase 4: verify the new shape

- `sldb` still indexes documents correctly
- `kgdb` can store, traverse, and query a graph independently of domain knowledge
- `ontology` can reason, inject facets, and run energy/cleansing without knowing about wiki workflows
- `wikipu` can still curate all layers through one CLI

## Deliverables for this drawer item

- `drawers/kgdb-storage-boundary.md`
- `drawers/kgdb-module-ownership-audit.md`
- `desk/tasks/Board.md`
- `desk/tasks/136-keep-energy-in-wikipu.md`

## Questions closed by this revision

1. **Name:** use `kgdb` for the graph database, `ontology` for the domain knowledge layer
2. **Role of kgdb:** pure graph database — node/edge storage, generic query engine, no domain knowledge
3. **Role of ontology:** domain knowledge above the graph — OWL, facets, energy, cleansing rules; uses kgdb as its storage substrate
4. **Approach:** start with storage and interpretation ownership, then do the implementation split

---

Submitted by: wikipu team
Date: 2026-04-22
Updated: 2026-04-23
Affected repos: wikipu, sldb, (new: kgdb), (new: ontology)
