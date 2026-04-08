---
identity:
  node_id: "doc:wiki/drafts/inputs_and_prerequisites.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

### `match` node required state

## Details

### `match` node required state

- `state.job_id`
- `state.extracted_data.requirements` (non-empty list)
- `state.my_profile_evidence` (non-empty list)

On regeneration (`state.review_decision == "request_regeneration"`), `match` additionally requires latest review feedback from:

- `data/jobs/<source>/<job_id>/nodes/match/review/rounds/<latest>/feedback.json`

Fail-closed checks:

- feedback file must exist and parse as mapping,
- `round_n >= 1`,
- non-empty feedback list,
- at least one actionable patch entry (`action == "patch"` or valid `patch_evidence`).

### `review_match` node required state

- `state.source`
- `state.job_id`
- `state.matched_data.matches`

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.