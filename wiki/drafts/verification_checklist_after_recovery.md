---
identity:
  node_id: "doc:wiki/drafts/verification_checklist_after_recovery.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

For each job, confirm:

## Details

For each job, confirm:

1. `nodes/match/review/decision.md` contains front matter with `source_state_hash`.
2. Review resume no longer raises hash-related `ValueError`.
3. `nodes/match/review/decision.json` exists.
4. `nodes/match/review/rounds/round_<NNN>/feedback.json` exists.
5. `graph/checkpoint.sqlite` has non-zero rows in `checkpoints` after a successful graph run.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.