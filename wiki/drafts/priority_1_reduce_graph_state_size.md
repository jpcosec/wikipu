---
identity:
  node_id: "doc:wiki/drafts/priority_1_reduce_graph_state_size.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

`MatchSkillState` still carries full semantic payloads such as:

- `requirements`
- `profile_evidence`
- `effective_profile_evidence`
- `match_result`
- `active_feedback`

This is convenient for the current implementation, but it makes checkpoint state heavier than necessary.

### Why It Matters

- larger checkpoints
- slower graph persistence
- harder-to-reason-about state transitions
- more coupling between nodes

### Recommended Change

Move toward refs-only or mostly-refs state.

Instead of carrying large payloads in state, carry:

- `source`
- `job_id`
- `run_id` if needed
- `round_number`
- `status`
- `review_decision`
- artifact refs such as:
  - `requirements_ref`
  - `profile_evidence_ref`
  - `effective_profile_ref`
  - `match_result_ref`
  - `review_surface_ref`
  - `feedback_ref`

Then let each node load the artifact it needs from `MatchArtifactStore`.

### Suggested Steps

1. extend `MatchArtifactStore` so it can persist and load all node inputs explicitly
2. update `load_match_inputs` to write refs instead of returning full payloads
3. update downstream nodes to reload data from refs
4. keep only routing signals in `MatchSkillState`

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.