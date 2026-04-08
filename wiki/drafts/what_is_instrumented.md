---
identity:
  node_id: "doc:wiki/drafts/what_is_instrumented.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md", relation_type: "documents"}
---

- Graph-level run span: `graph.run_pipeline`

## Details

- Graph-level run span: `graph.run_pipeline`
- Every graph node span: `node.<node_name>` (applies to all nodes registered in `create_app`)
- Deterministic quality evaluation span: `quality_eval.prep_match`

Generated from `raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md`.