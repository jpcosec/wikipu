---
identity:
  node_id: "doc:wiki/drafts/one_time_safety_migration_already_idempotent.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md", relation_type: "documents"}
---

This preserves reviewed decisions and adds hash-lock front matter to legacy reviewed files.

## Details

This preserves reviewed decisions and adds hash-lock front matter to legacy reviewed files.

```bash
python -m src.cli.migrate_review_hash_lock --source tu_berlin --all-jobs --dry-run
python -m src.cli.migrate_review_hash_lock --source tu_berlin --all-jobs
```

Backups are written as:

- `data/jobs/<source>/<job_id>/nodes/match/review/decision.legacy_reviewed*.md`

Generated from `raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md`.