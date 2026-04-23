---
status: open
priority: p1
depends_on:
  - drawers/requests/extract-kgdb-from-wikipu.md
  - drawers/kgdb-storage-boundary.md
created: 2026-04-23
assigned_to: self
---

# Target Architecture Diagram — kgdb + ontology + wikipu

This deferred diagram shows the intended future state where `wikipu` curates three external layers: `sldb` for document facts, `kgdb` for pure graph database operations, and `ontology` for domain knowledge and semantic interpretation.

## Context

This is not current truth. It is the target-state architecture that the extraction plan in `drawers/executable-extraction-plan.md` is designed to reach. It should stay in `drawers/` until the split is fully implemented.

Compare with `wiki/reference/diagrams/current_system_architecture.md` to see what is changing.

## Source

- Spec source: `drawers/diagrams/specs/target_architecture.yml`
- Rendered Mermaid: `drawers/diagrams/rendered/target_architecture.mmd`
- Rendered PlantUML: `drawers/diagrams/rendered/target_architecture.puml`

## Diagram

```mermaid
graph TD
    SLDB["sldb"]
    SLDB --> DocumentStore
    SLDB --> DocumentIndex
    DocumentStore["document bodies + contracts"]
    DocumentIndex["document index + validation"]
    KGDB["kgdb"]
    KGDB --> GraphStorage
    KGDB --> QueryEngine
    KGDB --> KGDBContracts
    KGDB --> KGDBMain
    GraphStorage["graph/ — node/edge persistence"]
    QueryEngine["query/ — StructuredQuery + executor"]
    KGDBContracts["contracts/ — Edge, KnowledgeNode"]
    KGDBMain["main.py — kgdb CLI"]
    Ontology["ontology"]
    Ontology --> OWLLayer
    Ontology --> FacetLayer
    Ontology --> EnergyLayer
    Ontology --> CleansingLayer
    Ontology --> DomainContracts
    Ontology --> OntologyMain
    OWLLayer["reasoning/ — OWL + HermiT"]
    FacetLayer["facets/ — registry + injectors + validator"]
    EnergyLayer["energy/ — systemic energy audit"]
    CleansingLayer["cleansing/ — domain structural rules"]
    DomainContracts["contracts/ — facets, energy, wiki_nodes, proposals"]
    OntologyMain["main.py — ontology CLI"]
    Wikipu["wikipu"]
    Wikipu --> CuratorCLI
    Wikipu --> Adapters
    Wikipu --> WorkspaceZones
    Wikipu --> CurationFlows
    CuratorCLI["wiki-compiler CLI + commands/"]
    Adapters["adapters/ — kgdb + ontology + sldb"]
    WorkspaceZones["wiki/ + desk/ + drawers/ + raw/ + src/"]
    CurationFlows["coordinator, gates, sessions, trails"]
    GraphArtifact["knowledge_graph.json"]
    Outputs["operator outputs"]
    Outputs --> WikiOut
    Outputs --> AuditOut
    Outputs --> EnergyOut
    WikiOut["curated wiki view"]
    AuditOut["audit + context bundles"]
    EnergyOut["energy + cleansing reports"]
    Wikipu -->|consumes documents and index| SLDB
    Wikipu -->|consumes graph storage and query| KGDB
    Wikipu -->|consumes domain services| Ontology
    Ontology -->|uses storage substrate| KGDB
    SLDB -->|stable doc inputs| KGDB
    SLDB -->|stable doc inputs| Ontology
    KGDB -->|node-link JSON| GraphArtifact
    GraphArtifact -->|query and reports| Outputs
    Adapters -->|kgdb adapter| KGDB
    Adapters -->|ontology adapter| Ontology
    Adapters -->|sldb adapter| SLDB
    CuratorCLI -->|all operations| Adapters
    CurationFlows -->|graph and domain ops| Adapters
    Ontology -->|energy + cleansing| EnergyOut
    KGDB -->|query results| AuditOut
    Wikipu -->|curated wiki| WikiOut
```

## What this target makes explicit

- `kgdb` is a pure database — no OWL, no facet semantics, no domain rules
- `ontology` is the domain knowledge layer — it uses `kgdb` as its storage substrate, never the other way
- `Adapters` inside `wikipu` is the only crossing point — `CuratorCLI` and `CurationFlows` never import kgdb or ontology internals directly
- `sldb` feeds both `kgdb` and `ontology` through stable document artifact inputs
- Each of the three new packages has its own CLI (`main.py`)

## Usage Examples

- Use this diagram when discussing the desired end state of the three-package split.
- Use it alongside `drawers/executable-extraction-plan.md` to track which phases have been completed.
- Compare against `wiki/reference/diagrams/current_system_architecture.md` to explain what is changing.
