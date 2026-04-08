---
identity:
  node_id: "doc:wiki/drafts/5_partial_output_handling.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

Ingestion may produce partial results (some records succeed, some fail). Handle explicitly:

## Details

Ingestion may produce partial results (some records succeed, some fail). Handle explicitly:

- Write successful records.
- Log failures per-record with `LogTag.WARN` — include enough context to retry the specific record.
- Never abort the whole batch because one record failed.
- Write a `meta.json` alongside the output with: total attempted, succeeded, failed, failure reasons.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.