---
identity:
  node_id: "doc:wiki/drafts/10_current_api_surface_relevant_to_ux.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

### Portfolio

## Details

### Portfolio

- `GET /api/v1/portfolio/summary`

### Job workspace

- `GET /api/v1/jobs/{source}/{job_id}/timeline`
- `GET /api/v1/jobs/{source}/{job_id}/view1`
- `GET /api/v1/jobs/{source}/{job_id}/view2`
- `GET /api/v1/jobs/{source}/{job_id}/view3`
- `GET /api/v1/jobs/{source}/{job_id}/review/match`

### Local artifact editing

- `GET /api/v1/jobs/{source}/{job_id}/editor/{node_name}/state`
- `PUT /api/v1/jobs/{source}/{job_id}/editor/{node_name}/state`
- `GET /api/v1/jobs/{source}/{job_id}/stage/{stage}/outputs`
- `GET /api/v1/jobs/{source}/{job_id}/documents/{doc_key}`
- `PUT /api/v1/jobs/{source}/{job_id}/documents/{doc_key}`

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.