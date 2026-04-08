---
identity:
  node_id: "doc:wiki/drafts/suggested_steps.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md", relation_type: "documents"}
---

1. define the canonical profile evidence payload shape

## Details

1. define the canonical profile evidence payload shape
2. isolate legacy compatibility in one loader/normalizer boundary
3. add a dedicated graph node for profile loading
4. make downstream nodes consume only normalized data or refs
5. add tests for all accepted input sources and legacy payload variants

Generated from `raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md`.