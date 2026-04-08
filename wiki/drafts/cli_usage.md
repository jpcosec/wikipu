---
identity:
  node_id: "doc:wiki/drafts/cli_usage.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md", relation_type: "documents"}
---

Run prep-match with explicit verification:

## Details

Run prep-match with explicit verification:

```bash
python -m src.cli.run_pipeline \
  --source <source> \
  --job-id <job_id> \
  --source-url <url> \
  --profile-evidence <path> \
  --langsmith-verifiable
```

In this mode:

- missing `LANGSMITH_API_KEY` fails closed
- a deterministic verification report is written to `data/jobs/<source>/<job_id>/graph/langsmith_verification.json`
- failed quality checks raise an error

Generated from `raw/docs_postulador_langgraph/docs/runtime/langsmith_verification.md`.