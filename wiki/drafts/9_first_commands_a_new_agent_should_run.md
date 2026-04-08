---
identity:
  node_id: "doc:wiki/drafts/9_first_commands_a_new_agent_should_run.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

```bash

## Details

```bash
conda activate phd-cv
set -a; source .env; set +a
rg --files
python -m pytest -q
python -m src.cli.run_prep_match --help
```

Then inspect:

- `src/graph.py`
- `src/cli/run_prep_match.py`
- `src/nodes/*/logic.py`
- `docs/operations/tool_interaction_and_known_issues.md`

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.