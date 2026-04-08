---
identity:
  node_id: "doc:wiki/drafts/preventive_actions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

1. Add a one-off migration utility for legacy `decision.md` files (pre-hash format) before running resume in mixed-version data folders.

## Details

1. Add a one-off migration utility for legacy `decision.md` files (pre-hash format) before running resume in mixed-version data folders.
2. Add an operator preflight command that checks:
   - dependency imports,
   - checkpoint row presence,
   - review hash-lock readiness.
3. Keep compatibility notes explicit when review markdown schema changes.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.