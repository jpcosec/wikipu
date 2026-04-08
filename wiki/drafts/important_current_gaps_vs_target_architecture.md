---
identity:
  node_id: "doc:wiki/drafts/important_current_gaps_vs_target_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

1. `src/core/io/` exists, but node migration to a single uniform I/O pattern is incomplete.

## Details

1. `src/core/io/` exists, but node migration to a single uniform I/O pattern is incomplete.
2. Provenance and observability are partially implemented, but not every node writes a standardized `meta/provenance.json`.
3. The current runnable flow has one active semantic review gate (`review_match`), not the full multi-stage review architecture described in older plans.
4. Several docs in the repo still describe target-state behavior rather than current runtime behavior.

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.