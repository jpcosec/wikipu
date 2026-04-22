---
status: open
priority: p1
depends_on:
  - drawers/requests/three-library-architecture.md
  - drawers/requests/extract-kgdb-from-wikipu.md
created: 2026-04-23
assigned_to: self
---

# kgdb Target Architecture Diagram

This deferred diagram shows the intended future split where `wikipu` curates two external layers: `sldb` for document facts and indexing, and `kgdb` for horizontal relations and semantic interpretation.

## Context

This is not current truth. It is a target-state architecture aid for the `kgdb` isolation effort and should stay in `drawers/` until the split is implemented.

## Source

- Spec source: `drawers/diagrams/specs/kgdb_target_architecture.yml`
- Rendered Mermaid: `drawers/diagrams/rendered/kgdb_target_architecture.mmd`
- Rendered PlantUML: `drawers/diagrams/rendered/kgdb_target_architecture.puml`

## Diagram

```mermaid
graph TD
    Wikipu["wikipu"]
    Wikipu --> CuratorCLI
    Wikipu --> WorkspaceZones
    Wikipu --> CurationFlows
    CuratorCLI["wiki-compiler CLI"]
    WorkspaceZones["wiki/ + desk/ + drawers/ + raw/ + src/"]
    CurationFlows["curation and orchestration"]
    SLDB["sldb"]
    SLDB --> DocumentStore
    SLDB --> ModelsTemplates
    SLDB --> ValidationIndex
    DocumentStore["documents"]
    ModelsTemplates["models + templates"]
    ValidationIndex["validation + document index"]
    KGDB["kgdb"]
    KGDB --> RelationGraph
    KGDB --> SemanticLayer
    KGDB --> ReasoningQuery
    RelationGraph["horizontal relations"]
    SemanticLayer["semantic overlays"]
    ReasoningQuery["reasoning + query + reports"]
    Interfaces["stable interfaces"]
    Interfaces --> SLDBExport["indexed facts"]
    Interfaces --> KGDBViews["graph + semantic views"]
    SLDBExport["sldb exports"]
    KGDBViews["kgdb exports"]
    Outputs["operator outputs"]
    Outputs --> WikiProjection
    Outputs --> AuditContext
    Outputs --> FutureActions
    WikiProjection["curated wiki view"]
    AuditContext["audit + context + energy"]
    FutureActions["gates + tasks + proposals"]
    Wikipu -->|consumes| SLDB
    Wikipu -->|consumes| KGDB
    SLDB -->|provides facts| Interfaces
    KGDB -->|provides relations and semantics| Interfaces
    Interfaces -->|curated presentation| Outputs
```

## What this target makes explicit

- `wikipu` is the curator, not the owner of document indexing or relation semantics
- `sldb` owns facts, document structure, and indexing
- `kgdb` owns horizontal relations, semantic interpretation, and graph-native outputs
- the future split depends on stable interfaces between the three systems

## Usage Examples

- Use this diagram when discussing the desired end state of the three-library split.
- Compare it with `wiki/reference/diagrams/current_system_architecture.md` to explain what is changing.
