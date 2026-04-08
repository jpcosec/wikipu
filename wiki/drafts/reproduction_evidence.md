---
identity:
  node_id: "doc:wiki/drafts/reproduction_evidence.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md", relation_type: "documents"}
---

### 1) CLI resume currently fails in current shell context

## Details

### 1) CLI resume currently fails in current shell context

Command:

```bash
python -m src.cli.run_prep_match --source tu_berlin --job-id 201588 --resume
```

Observed error:

```text
ModuleNotFoundError: No module named 'langgraph'
```

Important context from `docs/operations/agent_entrypoint.md`:

- expected env is `conda activate phd-cv`
- expected preflight is `set -a; source .env; set +a`

So this symptom is treated as an environment preflight miss in the tested shell, not as a repository code defect by itself.

### 2) Review node fails closed on reviewed files

Running `src/nodes/review_match/logic.py` directly against current reviewed artifacts fails for all scoped jobs with:

```text
ValueError: decision.md is missing source_state_hash; regenerate review markdown from current nodes/match/approved/state.json and re-apply decisions
```

### 3) Data-plane and control-plane state snapshot

For all scoped reviewed jobs:

- `nodes/match/review/decision.md` exists
- decision checkboxes are already marked (`[x]` variants)
- `source_state_hash` front matter is missing
- `nodes/match/review/decision.json` does not exist
- `nodes/match/review/rounds/round_*/feedback.json` does not exist
- `graph/checkpoint.sqlite` exists but `checkpoints` and `writes` table row counts are `0`

Generated from `raw/docs_postulador_langgraph/docs/operations/reviewed_jobs_pipeline_diagnosis.md`.