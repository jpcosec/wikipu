---
identity:
  node_id: "doc:wiki/drafts/start_everything_neo4j_api_ui.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/ui_workbench_phase0_bootstrap.md", relation_type: "documents"}
---

```bash

## Details

```bash
./scripts/dev-all.sh
```

Opens (or the next free ports if these are busy):

- UI: `http://127.0.0.1:4173`
- API: `http://127.0.0.1:8010`
- Neo4j Browser: `http://127.0.0.1:7474`

Ctrl+C stops UI/API. Set `STOP_NEO4J_ON_EXIT=1` if you also want Docker to stop when exiting.

Generated from `raw/docs_postulador_langgraph/docs/operations/ui_workbench_phase0_bootstrap.md`.