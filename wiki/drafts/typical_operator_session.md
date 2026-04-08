---
identity:
  node_id: "doc:wiki/drafts/typical_operator_session.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md", relation_type: "documents"}
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

Repeat until route is `approve` or `reject` and the flow reaches `package`.

Generated from `raw/docs_postulador_langgraph/docs/operations/tool_interaction_and_known_issues.md`.