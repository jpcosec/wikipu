---
identity:
  node_id: "doc:wiki/drafts/lifecycle_metadata.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/data_management.md", relation_type: "documents"}
---

`meta.json` is managed centrally by the data manager.

## Details

`meta.json` is managed centrally by the data manager.

Initial schema-v0 fields:

- `schema_version`
- `status` (`active`, `urgent`, `archived`, `discarded`)
- `created_at`
- `updated_at`

The pipeline may read this metadata for filtering and operational decisions, but
it must not move job roots on disk.

---

Generated from `raw/docs_postulador_refactor/docs/runtime/data_management.md`.