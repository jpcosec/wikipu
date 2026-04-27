---
status: open
priority: p1
depends_on:
  - drawers/kgdb-storage-boundary.md
created: 2026-04-22
updated: 2026-04-23
assigned_to: self
---

# Module Ownership Audit

This audit classifies current `src/wiki_compiler/` modules by where they should live after the split.

## Bucket meanings

- `kgdb`: pure graph database — storage, traversal, generic query engine, base graph contracts
- `ontology`: domain knowledge above the graph — OWL, facets, energy, cleansing rules, wiki document types
- `wikipu`: curation, workspace, orchestration, CLI
- `split`: mixed module; needs to be split into its respective cores before extraction

The critical distinction: `kgdb` has no opinion about what nodes mean. `ontology` interprets them through domain knowledge.

## Audit: top-level modules

| Module | Target | Why |
|---|---|---|
| `graph_utils.py` | kgdb | pure graph I/O primitives: add/load/save/iter nodes |
| `query_language.py` | kgdb | generic query DSL: FieldCondition, FacetFilter, GraphScope, StructuredQuery |
| `query_executor.py` | kgdb | generic query execution: traverse and filter by structured query |
| `owl_reasoner.py` | ontology | OWL semantic inference via HermiT/Pellet — domain knowledge |
| `owl_backend/` | ontology | full OWL backend: export, frontmatter, extractor, wikilinks, annotations |
| `auditor_owl.py` | ontology | OWL conflict detection — knows about Markdown/OWL semantic consistency |
| `energy.py` | ontology | systemic energy metrics; encodes domain rules about drift, redundancy, FFT |
| `cleanser.py` | ontology | domain-aware cleansing rules; knows about tests, plans, configs, abstracts |
| `facet_injectors.py` | ontology | ADRInjector, TestMapInjector — domain document type knowledge |
| `facet_validator.py` | ontology | facet proposal validation; encodes domain semantics of facet orthogonality |
| `registry.py` | ontology | FacetRegistry with domain-specific facet definitions |
| `contracts.py` | split | re-exports from contracts/; see contracts/ breakdown below |
| `builder.py` | split | graph-assembly core (edges from markdown, compliance score) → ontology; wiki compilation, zone orchestration, source selection → wikipu |
| `context.py` | split | graph neighborhood traversal → kgdb; task hydration, checklist rendering → wikipu |
| `scanner.py` | split | code/entity extraction feeds ontology; project scanning policy, exclusion rules → wikipu |
| `protocols.py` | split | interface definitions follow their respective boundary |
| `__init__.py` | split | package surface changes after split |
| `coordinator.py` | wikipu | coordinates repo workflow; not graph storage or domain interpretation |
| `perception.py` | wikipu | zone contracts and git-backed workspace perception |
| `auditor.py` | wikipu | compliance reporting across workspace; not graph storage |
| `main.py` | wikipu | CLI composition for the full curation workflow |
| `query_server.py` | wikipu | serving/query entrypoint; policy-level access to kgdb and ontology |
| `scaffolder.py` | wikipu | project bootstrapping |
| `curate.py` | wikipu | explicit curation workflow |
| `ingest.py` | wikipu | raw-to-curated ingestion policy |
| `manifest.py` | wikipu | raw source manifest management |
| `drafts.py` | wikipu | draft lifecycle |
| `trails.py` | wikipu | trail artifacts |
| `gates.py` | wikipu | human approval surface |
| `session_storage.py` | wikipu | session state |
| `workflow_guard.py` | wikipu | workflow enforcement |
| `sync_gate.py` | wikipu | operational synchronization control |
| `preflight.py` | wikipu | repo/process checks |
| `artifact_validation.py` | wikipu | authored artifact validation |
| `validator.py` | wikipu | topology proposal validation is a curation concern |
| `node_templates.py` | wikipu | wiki authoring templates |

## Audit: contracts/ package

| Module | Target | Why |
|---|---|---|
| `contracts/base.py` | kgdb | Edge, SystemIdentity — base graph primitives |
| `contracts/node.py` | kgdb | KnowledgeNode — the base graph node contract |
| `contracts/facets.py` | ontology | IOFacet, ASTFacet, SemanticFacet, ADRFacet, TestMapFacet, ComplianceFacet, SourceFacet, GitFacet — domain facet contracts |
| `contracts/energy.py` | ontology | SystemicEnergy, EnergyReport, ZoneContract — domain energy and zone contracts |
| `contracts/wiki_nodes.py` | ontology | ConceptDoc, HowToDoc, DocStandardDoc, ReferenceDoc, IndexDoc, ADRDoc, SelfDocDoc — document type taxonomy |
| `contracts/proposals.py` | ontology | AuditFinding, FacetProposal, FacetOrthogonalityReport, TopologyProposal, CollisionReport, ArtifactValidationFinding, CleansingProposal, CleansingReport — domain proposal contracts |
| `contracts/tasks.py` | wikipu | TaskDoc — task management contract |
| `contracts/tracking.py` | wikipu | RawSourceEntry, RawSourceManifest, GateRow, GateTable, CycleRecord, CycleHistory, TrailArtifact, TrailCollection, SessionLog, ContextRequest, ChecklistItem, Checklist, ContextBundle — operational tracking |
| `contracts/__init__.py` | split | re-export surface must be revised after split |

## First extraction candidates for kgdb

These are the cleanest starting points — no domain knowledge, no workspace assumptions:

- `graph_utils.py`
- `query_language.py`
- `query_executor.py`
- `contracts/base.py`
- `contracts/node.py`

## First extraction candidates for ontology

These have no workspace assumptions and import only kgdb primitives:

- `owl_reasoner.py`
- `owl_backend/`
- `auditor_owl.py`
- `energy.py`
- `contracts/facets.py`
- `contracts/energy.py`
- `contracts/wiki_nodes.py`
- `contracts/proposals.py`

## Modules that must be split carefully

These mix concerns from two or more layers:

- `builder.py` — graph edge building (ontology) + wiki compilation + zone orchestration (wikipu)
- `context.py` — graph neighborhood traversal (kgdb) + task/checklist hydration (wikipu)
- `scanner.py` — entity extraction (feeds ontology) + project scanning policy (wikipu)
- `facet_validator.py` — facet validation logic (ontology) + collision state management (consider if state belongs in wikipu)
- `cleanser.py` — mostly ontology, but `apply_cleansing_proposal` executes filesystem operations (wikipu)

## Suggested next implementation artifacts

After this audit, the extraction was atomized into `desk/tasks/` and executed. Remaining follow-up now lives on `desk/tasks/Board.md`, with energy re-ownership tracked by `desk/tasks/136-keep-energy-in-wikipu.md`.
