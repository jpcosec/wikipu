---
identity:
  node_id: "doc:wiki/drafts/what_the_command_does.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md", relation_type: "documents"}
---

Per job:

## Details

Per job:

1. If `nodes/match/approved/state.json` is missing, runs `match -> review_match`.
2. If reviewed decision is `approve`, marks the prep flow as terminal complete.
3. If reviewed decision is `reject`, stops at terminal reject route.
4. If reviewed decision is `request_regeneration`, runs regeneration (`match` with round feedback) and reopens a fresh review round.
5. If no decision is marked, leaves job in `pending_review`.

This path is checkpoint-independent and uses current artifacts as the source of truth.

Generated from `raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md`.