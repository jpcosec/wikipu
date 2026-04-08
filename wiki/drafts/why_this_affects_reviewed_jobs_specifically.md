---
identity:
  node_id: "doc:wiki/drafts/why_this_affects_reviewed_jobs_specifically.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

The guard is asymmetric by design:

## Details

The guard is asymmetric by design:

- Legacy file with no hash and no marked decisions -> allowed to regenerate safely.
- Legacy file with no hash and marked decisions -> blocked, requiring regeneration plus manual re-application.

Your reviewed jobs are in the second category.

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.