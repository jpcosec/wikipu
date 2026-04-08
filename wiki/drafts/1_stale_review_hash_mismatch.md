---
identity:
  node_id: "doc:wiki/drafts/1_stale_review_hash_mismatch.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
---

Symptoms:

## Details

Symptoms:

- resume fails with a source hash mismatch error.

Cause:

- `decision.md` was generated from an older `nodes/match/approved/state.json`.

Fix:

1. regenerate or let `review_match` regenerate the current review markdown,
2. re-apply review decisions,
3. resume again.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.