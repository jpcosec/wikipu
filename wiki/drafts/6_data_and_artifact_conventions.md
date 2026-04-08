---
identity:
  node_id: "doc:wiki/drafts/6_data_and_artifact_conventions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

Job workspace root:

## Details

Job workspace root:

- `data/jobs/<source>/<job_id>/`

Important artifacts in current flow:

- `nodes/match/approved/state.json`
- `nodes/match/review/decision.md`
- `nodes/match/review/decision.json` (written after parsing)
- `nodes/match/review/rounds/round_<NNN>/...` (round history)

Control plane vs data plane intent:

- `GraphState` should carry routing/control metadata.
- Heavy semantic payloads should live in on-disk artifacts.
- Current implementation still carries some transient payloads in state; this is a known transition state.

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.