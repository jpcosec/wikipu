---
identity:
  node_id: "doc:wiki/drafts/applied_recovery_2026_03_11.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

The hash-lock migration was applied to reviewed TU Berlin jobs:

## Details

The hash-lock migration was applied to reviewed TU Berlin jobs:

- `201578`
- `201588`
- `201601`
- `201606`
- `201661`
- `201695`

For each job:

- `nodes/match/review/decision.md` now includes front matter with `source_state_hash`.
- backup of the original reviewed file exists as `nodes/match/review/decision.legacy_reviewed.md`.
- deterministic parsing produced `nodes/match/review/decision.json` and `nodes/match/review/rounds/round_001/feedback.json`.

Batch continuation was then executed with:

- `python -m src.cli.run_available_jobs --source tu_berlin --profile-evidence data/reference_data/profile/base_profile/profile_base_data.json`

Observed outcomes:

- `201661` reached terminal complete route (`approve`).
- `201578`, `201588`, `201601`, `201606`, and `201695` advanced through regeneration and reopened review as new `round_002` pending review.
- `201637` completed first match generation and is now pending first review (`round_001`).

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.