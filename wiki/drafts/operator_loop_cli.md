---
identity:
  node_id: "doc:wiki/drafts/operator_loop_cli.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md", relation_type: "documents"}
---

Initial run:

## Details

Initial run:

```bash
python -m src.cli.run_prep_match \
  --source <source> \
  --job-id <job_id> \
  --source-url <url> \
  --profile-evidence <path_to_json>
```

Edit review markdown:

- `data/jobs/<source>/<job_id>/nodes/match/review/decision.md`

Resume:

```bash
python -m src.cli.run_prep_match --source <source> --job-id <job_id> --resume
```

Repeat until route is `approve` or `reject`.

Generated from `raw/docs_postulador_langgraph/docs/runtime/match_review_cycle.md`.