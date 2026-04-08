---
identity:
  node_id: "doc:wiki/drafts/fix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md", relation_type: "documents"}
---

1. Remove the local SQLite fallback block from `_run_pipeline`.

## Details

1. Remove the local SQLite fallback block from `_run_pipeline`.
2. Remove the local SQLite fallback block from `_run_review` (including the broken `app.checkpointer` assignment and the `build_match_skill_graph` import).
3. In `_run_review`, skip `thread_id` construction when source/job_id are absent (explorer mode).
4. Replace all fallback `except` blocks with a single `LangGraphConnectionError` surfaced to the user.
5. Delete `data/jobs/checkpoints.db` from the repo (or add to `.gitignore`).

Generated from `raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md`.