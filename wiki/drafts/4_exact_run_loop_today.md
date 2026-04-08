---
identity:
  node_id: "doc:wiki/drafts/4_exact_run_loop_today.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

Before running/resuming, export `.env` variables into the current shell:

## Details

Before running/resuming, export `.env` variables into the current shell:

```bash
set -a; source .env; set +a
```

Run until first review gate:

```bash
python -m src.cli.run_prep_match \
  --source tu_berlin \
  --job-id 201588 \
  --run-id run-local \
  --source-url https://www.jobs.tu-berlin.de/en/job-postings/201588 \
  --profile-evidence data/reference_data/profile/base_profile/profile_base_data.json
```

Then edit:

- `data/jobs/<source>/<job_id>/nodes/match/review/decision.md`

Resume:

```bash
python -m src.cli.run_prep_match --source <source> --job-id <job_id> --resume
```

Checkpoint path (default):

- `data/jobs/<source>/<job_id>/graph/checkpoint.sqlite`

Thread identity invariant:

- `thread_id = f"{source}_{job_id}"`

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.