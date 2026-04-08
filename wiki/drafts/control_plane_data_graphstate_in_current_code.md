---
identity:
  node_id: "doc:wiki/drafts/control_plane_data_graphstate_in_current_code.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

`GraphState` is defined in `src/core/graph/state.py`.

## Details

`GraphState` is defined in `src/core/graph/state.py`.

Current state includes both routing metadata and transient payload fields:

- Routing/identity: `source`, `job_id`, `run_id`, `source_url`, `current_node`, `status`, `review_decision`, `pending_gate`, `error_state`, `artifact_refs`
- Transient payloads: `ingested_data`, `extracted_data`, `matched_data`, `my_profile_evidence`, `last_decision`, `active_feedback`

Meaning:

- the repo is moving toward a control-plane-only state model,
- but current runtime still carries semantic payloads in memory between nodes.

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.