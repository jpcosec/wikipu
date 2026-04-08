---
identity:
  node_id: "doc:wiki/drafts/current_state_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

- In the current prep graph, `review_match.approve` now continues into document generation and markdown delivery (`generate_documents -> render -> package`).

## Details

- In the current prep graph, `review_match.approve` now continues into document generation and markdown delivery (`generate_documents -> render -> package`).
- The larger multi-stage target architecture still exists in planning docs, but this match-review loop is the operational gate in the runnable CLI flow today.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.