---
identity:
  node_id: "doc:wiki/drafts/step_04_external_data_schema_integration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Source adapter system driven by schema's `sources` section. Adapters ingest external data into neo4j as canonical base.

**Adapter types:** neo4j (direct), json_file (read + MERGE), api (fetch + MERGE), yaml_file.

**Pipeline:** Schema declares sources → adapter reads → maps to MERGE commands → executes against neo4j → provenance metadata attached.

**View query execution:** Subgraph views execute Cypher against neo4j, return graph_content for editor.

**Lazy loading:** Views declare `load_attributes`. Attributes not listed aren't fetched.

### 2. Objectives

1. neo4j + json_file adapters work end-to-end
2. MERGE semantics (idempotent)
3. Provenance metadata on all ingested nodes
4. Subgraph view queries execute correctly
5. Lazy attribute loading respects load_attributes
6. Adapter registry is extensible (source_adapter extension type)

### 3. Don'ts

- **Don't build bidirectional sync.** Ingestion is one-way.
- **Don't execute arbitrary Cypher from UI.** View queries are schema-declared.
- **Don't fetch all attributes upfront.** Respect load_attributes.
- **Don't couple adapters to each other.** Cross-source joins happen in neo4j.
- **Don't reinvent ETL.** Adapters are thin: read, map, MERGE.

### 4–7: See consolidated annexes.

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.