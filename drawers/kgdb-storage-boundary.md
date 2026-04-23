---
status: open
priority: p1
depends_on:
  - drawers/requests/extract-kgdb-from-wikipu.md
created: 2026-04-22
updated: 2026-04-23
assigned_to: self
---

# Storage and Interpretation Boundary

This note defines where each kind of truth should live before any code extraction happens.

## Principle

The split is about responsibility first — storage responsibility for `kgdb`, interpretation responsibility for `ontology`.

- `sldb` stores facts as documents and maintains an index of them.
- `kgdb` stores horizontal relations between those facts and exposes a generic traversal and query engine. It has no opinion about what relations mean.
- `ontology` interprets the graph through domain knowledge: OWL reasoning, facet semantics, energy metrics, cleansing rules.
- `wikipu` curates all three layers and decides how they are exposed to humans and agents.

## `sldb` owns

- document bodies
- document contracts and templates
- roundtrip validation
- document index
- federation metadata
- hash-integrity state

`sldb` answers: where is the fact, what schema does it obey, and is it valid?

## `kgdb` owns

- node and edge persistence (networkx graph serialization and I/O)
- base graph contracts: `Edge`, `SystemIdentity`, `KnowledgeNode`
- generic structured query DSL: `FieldCondition`, `FacetFilter`, `GraphScope`, `StructuredQuery`
- generic query execution: traverse, filter, match — without any knowledge of what a facet means
- graph I/O primitives: `add_knowledge_node`, `load_graph`, `save_graph`, `load_knowledge_node`, `iter_knowledge_nodes`

`kgdb` answers: which nodes exist, what are their edges, and which nodes match a generic filter?

`kgdb` does NOT answer: what does a SemanticFacet mean, how stale is the graph, are there OWL contradictions, what is the systemic energy?

## `ontology` owns

- OWL backend and ontology definitions
- OWL reasoner integration (HermiT/Pellet via owlready2)
- OWL consistency checking
- domain facet contracts: `IOFacet`, `ASTFacet`, `SemanticFacet`, `ADRFacet`, `TestMapFacet`, `ComplianceFacet`, `SourceFacet`, `GitFacet`
- facet registry, injection logic, and validation
- systemic energy contracts (`SystemicEnergy`, `EnergyReport`) and audit logic
- domain cleansing rules (stale edges, orphaned tests, orphaned plans, misplaced folders, duplicate abstracts)
- wiki document type taxonomy (`ConceptDoc`, `HowToDoc`, `ADRDoc`, `ReferenceDoc`, etc.)
- audit and topology proposal contracts (`AuditFinding`, `FacetProposal`, `CleansingProposal`, `TopologyProposal`, etc.)
- `ZoneContract`

`ontology` answers: what do the relations mean, is the graph semantically consistent, what domain-level problems exist, how much systemic energy does the current state carry?

`ontology` uses `kgdb` as its storage and traversal substrate. It never replaces it.

## `wikipu` owns

- curated wiki output
- `desk/` and `drawers/` operational surfaces
- gates, sessions, trails, and workflow state
- build and audit orchestration
- the user-facing CLI that curates all layers
- task management and sldb-backed task documents

`wikipu` answers: what should the operator see, review, and do next?

## What should not be mixed anymore

- domain facet semantics should not live inside the graph storage layer
- OWL reasoning should not be a graph-database concern
- energy and cleansing rules that encode domain-specific knowledge (tests, plans, configs) should not live in the db layer
- workspace curation rules should not live inside graph storage or interpretation modules
- graph storage should not know about wiki document types or zone contracts

## Dependency direction

```
sldb        (no upstream deps in this system)
kgdb   →   sldb artifacts (stable inputs only)
ontology →  kgdb  (uses kgdb primitives for storage and traversal)
ontology →  sldb artifacts (stable document inputs for relation building)
wikipu  →   sldb
wikipu  →   kgdb
wikipu  →   ontology
```

Forbidden:
- `sldb → kgdb`, `sldb → ontology`, `sldb → wikipu`
- `kgdb → ontology` (db has no knowledge of domain)
- `kgdb → wikipu`
- `ontology → wikipu`

## Preferred artifact boundary

### From `sldb` to `kgdb`

- stable document identifiers
- document metadata needed for relation building
- document index exports

### From `kgdb` to `ontology`

- graph instances (`nx.DiGraph`) for reasoning and analysis
- query results as `KnowledgeNode` lists
- raw node/edge data for interpretation

### From `kgdb` to `wikipu`

- graph views
- query results

### From `ontology` to `wikipu`

- reasoning reports
- energy reports
- cleansing proposals
- audit findings
- facet orthogonality reports

### From `sldb` to `wikipu`

- document retrieval
- validation status
- document index and model information

## Acceptance signal

The boundary is good when:

- a document can exist in `sldb` without `kgdb` or `ontology`
- a graph can be built and queried in `kgdb` without any domain knowledge
- `ontology` can reason about a graph loaded from `kgdb` without knowing about wiki workflows
- `wikipu` can curate all three layers without owning their internal persistence or interpretation logic
