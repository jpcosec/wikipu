---
identity:
  node_id: "doc:wiki/drafts/start_only_api_ui_keep_neo4j_manual.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/ui_workbench_phase0_bootstrap.md", relation_type: "documents"}
---

```bash

## Details

```bash
./scripts/dev.sh
```

Opens UI at `http://127.0.0.1:4173` and API at `http://127.0.0.1:8010`.

### Or start separately

```bash
# API only
python -m src.cli.run_review_api

# UI only
npm --prefix apps/review-workbench install
npm --prefix apps/review-workbench run dev
```

Generated from `raw/docs_postulador_langgraph/docs/operations/ui_workbench_phase0_bootstrap.md`.