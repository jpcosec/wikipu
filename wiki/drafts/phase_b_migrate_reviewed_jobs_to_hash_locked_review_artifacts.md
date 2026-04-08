---
identity:
  node_id: "doc:wiki/drafts/phase_b_migrate_reviewed_jobs_to_hash_locked_review_artifacts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

For each affected job:

## Details

For each affected job:

1. Back up current reviewed file:
   - `nodes/match/review/decision.md` -> `nodes/match/review/decision.legacy_reviewed.md`
2. Regenerate a fresh hash-bearing `decision.md` from current `nodes/match/approved/state.json`.
3. Re-apply reviewer decisions/comments onto the regenerated file.
4. Resume and verify `decision.json` and `feedback.json` are produced.

Note: because checkpoint tables are empty, safest operational path is to rerun prep stages for each job (non-resume) to recreate valid checkpoint history and fresh review artifacts, then re-apply decisions.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.