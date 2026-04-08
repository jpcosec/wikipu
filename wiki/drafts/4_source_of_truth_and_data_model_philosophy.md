---
identity:
  node_id: "doc:wiki/drafts/4_source_of_truth_and_data_model_philosophy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

### Current source of truth

## Details

### Current source of truth

All data is local and file-based.

Primary location:

- `data/jobs/<source>/<job_id>/`

Key artifact conventions:

- `nodes/<node>/approved/state.json`
- `nodes/<node>/proposed/*.md`
- `nodes/<node>/review/decision.md`
- `nodes/<node>/trace/error_screenshot.png`
- `raw/source_text.md`

### Important product constraint

The UI is not the source of truth.

The UI is a projection/editor over disk artifacts.

That means the designer should assume:

1. save actions write back to local files
2. stage views are artifact-centric
3. data may be incomplete or missing for some stages
4. every screen should degrade gracefully when an artifact does not exist yet

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.