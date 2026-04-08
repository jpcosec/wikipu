---
identity:
  node_id: "doc:wiki/drafts/hash_lock_behavior.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

`review_match` protects against stale review decisions:

## Details

`review_match` protects against stale review decisions:

- If checked decisions exist but `source_state_hash` is missing -> error.
- If embedded hash differs from current match payload hash -> error.
- If hash is missing and no boxes are checked (legacy blank review file) -> regenerate clean review markdown and remain pending.

This prevents applying human decisions to a different match state.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.