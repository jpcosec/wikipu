---
identity:
  node_id: "doc:wiki/drafts/why_it_matters.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/logging_layer_conflicts.md", relation_type: "documents"}
---

- root logger configuration can be overridden unexpectedly

## Details

- root logger configuration can be overridden unexpectedly
- module CLIs can stomp on each other's logging behavior
- observability output is inconsistent across the stack
- it is harder to separate our application logs from LangGraph / third-party logs

Generated from `raw/docs_postulador_refactor/future_docs/issues/logging_layer_conflicts.md`.