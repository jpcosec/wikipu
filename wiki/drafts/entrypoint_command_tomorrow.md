---
identity:
  node_id: "doc:wiki/drafts/entrypoint_command_tomorrow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/next_session_entrypoint.md", relation_type: "documents"}
---

Run full prep->match pipeline until `review_match` artifacts are ready:

## Details

Run full prep->match pipeline until `review_match` artifacts are ready:

```bash
python -m src.cli.run_prep_match \
  --source tu_berlin \
  --job-id 201588 \
  --run-id run-next-session \
  --source-url https://www.jobs.tu-berlin.de/en/job-postings/201588 \
  --profile-evidence data/reference_data/profile/base_profile/profile_base_data.json
```

Review file to edit:

- `data/jobs/tu_berlin/201588/nodes/match/review/decision.md`

Resume after editing decision file:

```bash
python -m src.cli.run_prep_match --source tu_berlin --job-id 201588 --resume
```

Generated from `raw/docs_postulador_langgraph/docs/operations/next_session_entrypoint.md`.