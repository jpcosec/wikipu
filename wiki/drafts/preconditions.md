---
identity:
  node_id: "doc:wiki/drafts/preconditions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md", relation_type: "documents"}
---

Use the runtime environment documented in `docs/operations/agent_entrypoint.md`:

## Details

Use the runtime environment documented in `docs/operations/agent_entrypoint.md`:

```bash
conda activate phd-cv
set -a; source .env; set +a
```

Required runtime deps for LLM steps:

- `langgraph`
- `google-generativeai`

Generated from `raw/docs_postulador_langgraph/docs/operations/available_jobs_recovery_runbook.md`.