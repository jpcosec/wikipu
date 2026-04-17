---
pill_type: decision
scope: component
language: en
nature: context
bound_to: owl-phase1-parallel-run, owl-phase2-quadstore-primary, owl-phase3-reasoning, owl-phase4-full-migration
created: 2026-04-17
lifecycle: current
---

# OWL Integration Decision Context

## Why OWL over alternatives

- **YAML frontmatter only** — No inference, manual edge maintenance
- **RDFlib only** — Stores triples but no reasoning
- **Neo4j** — Requires separate tooling, slower than owlready2 benchmarks
- **Build custom reasoner** — HermiT/Pellet are proven

OWL aligns with our topology definition: "knowledge is typed relationships between concepts."

## Constraints

1. **Java required** — HermiT/Pellet need JVM for reasoning
2. **Learning curve** — OWL semantics differ from YAML
3. **Migration effort** — Existing wiki/ content needs transformation
4. **Sync complexity** — Pydantic ↔ OWL bidirectional sync needed

## Key Design Decisions

1. **Quadstore backend** — SQLite3 via owlready2, not file-based RDF
2. **SHACL gatekeeping** — Validate before committing triples
3. **SyncGate class** — Bidirectional Pydantic ↔ OWL sync
4. **Markdown stays** — Narrative prose; OWL for structured content

## Reference

- `wiki/adrs/003_owl_integration.md`
- `wiki/adrs/004_workflow_as_ontology.md`
