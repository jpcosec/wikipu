---
identity:
  node_id: "doc:wiki/drafts/required_properties.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/reference/node_io_target_matrix.md", relation_type: "documents"}
---

1. All generator outputs must be persisted under `nodes/<node>/proposed/`.

## Details

1. All generator outputs must be persisted under `nodes/<node>/proposed/`.
2. All review decisions must be persisted under `nodes/<node>/review/decision.{md,json}` with stale-hash safety.
3. Downstream nodes may consume only `approved/` artifacts.
4. Provenance metadata is required for approved outputs in reviewable paths.
5. No silent fallback-to-success behavior is allowed.

Generated from `raw/docs_postulador_langgraph/docs/reference/node_io_target_matrix.md`.