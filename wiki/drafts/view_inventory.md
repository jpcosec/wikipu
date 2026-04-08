---
identity:
  node_id: "doc:wiki/drafts/view_inventory.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

The product has **5 top-level views** (URL routes):

## Details

The product has **5 top-level views** (URL routes):

| Route | View name | Implemented | Sample reference |
|---|---|---|---|
| `/` | Portfolio | ✅ | `global_porfolio_view.html` |
| `/jobs/:source/:jobId` | Job workspace | ✅ | `extraction.html` + `matching*.html` |
| `/jobs/:source/:jobId/node-editor` | Node editor | ✅ | partial — see gap below |
| `/jobs/:source/:jobId` outputs tab | Pipeline outputs | ✅ | `document_generation.html` |
| `/jobs/:source/:jobId` outputs tab (scraping) | Scrape diagnostics | ✅ | (not sampled) |
| — | Deployment / package | ❌ | `deployment.html` |

Within `/jobs/:source/:jobId` there are 4 sub-tabs (view-1 through view-3 + outputs), all listed above.

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.