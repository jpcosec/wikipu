---
identity:
  node_id: "doc:wiki/drafts/2_missing_checkpoint_history_for_resume_secondary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

`run_prep_match --resume` depends on persisted LangGraph checkpoint state (`thread_id = f"{source}_{job_id}"`) to wake from interrupt before `review_match`.

## Details

`run_prep_match --resume` depends on persisted LangGraph checkpoint state (`thread_id = f"{source}_{job_id}"`) to wake from interrupt before `review_match`.

Current per-job sqlite files have schema but no checkpoint rows, so there is no recorded interrupt state to resume from.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.