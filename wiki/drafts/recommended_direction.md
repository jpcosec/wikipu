---
identity:
  node_id: "doc:wiki/drafts/recommended_direction.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/logging_layer_conflicts.md", relation_type: "documents"}
---

Introduce a shared logging configuration layer under `src/shared/` and migrate entry points to it.

## Details

Introduce a shared logging configuration layer under `src/shared/` and migrate entry points to it.

Likely steps:

1. add a shared logger/bootstrap utility
2. stop using `force=True` in module CLIs unless there is a strong reason
3. standardize on `LogTag` for application-level messages
4. keep third-party logs isolated from our application logger where possible
5. document the official logging model in the relevant READMEs

Generated from `raw/docs_postulador_refactor/future_docs/issues/logging_layer_conflicts.md`.