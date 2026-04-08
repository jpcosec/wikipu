---
identity:
  node_id: "doc:wiki/drafts/recommended_recovery_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

Implemented helper for safe migration:

## Details

Implemented helper for safe migration:

- `python -m src.cli.migrate_review_hash_lock --source <source> --job-id <id> [--job-id <id> ...]`
- use `--dry-run` first to preview actions.

Implemented checkpoint-independent continuation runner:

- `python -m src.cli.run_available_jobs --source <source> --dry-run`
- `python -m src.cli.run_available_jobs --source <source> --profile-evidence <path_to_profile_json>`

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.