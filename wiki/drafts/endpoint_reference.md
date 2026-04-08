---
identity:
  node_id: "doc:wiki/drafts/endpoint_reference.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/10_ui_dev_integration_map.md", relation_type: "documents"}
---

| Action | Endpoint |

## Details

| Action | Endpoint |
|--------|----------|
| Portfolio summary | `GET /api/v1/portfolio/summary` |
| Scrape outputs | `GET /stage/scrape/outputs` |
| View extract | `GET /view2` |
| Match state | `GET /view1` |
| Review match | `GET /review/match` |
| Update match | `PATCH /review/match/evidence` |
| Save document | `PUT /api/v1/jobs/{source}/{job_id}/documents/{doc_key}` |
| Browse files | `GET /api/v1/jobs/{source}/{job_id}/browse` |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/10_ui_dev_integration_map.md`.