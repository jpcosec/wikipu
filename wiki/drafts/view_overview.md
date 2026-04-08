---
identity:
  node_id: "doc:wiki/drafts/view_overview.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

| Spec | View | Route | Pipeline Stage | Feature Path |

## Details

| Spec | View | Route | Pipeline Stage | Feature Path |
|------|------|-------|---------------|--------------|
| A1 | Portfolio Dashboard | `/` | (none - global) | `features/portfolio/` |
| A2 | Data Explorer | `/explorer` | (none - global) | `features/explorer/` |
| A3 | Base CV Editor | `/cv` | (none - global) | `features/base-cv/` |
| B0 | Job Flow Inspector | `/jobs/:source/:jobId` | (global - job) | `features/job-pipeline/` |
| B1 | Scrape Diagnostics | `/jobs/:source/:jobId/scrape` | scrape | `features/job-pipeline/` |
| B2 | Extract & Understand | `/jobs/:source/:jobId/extract` | extract | `features/job-pipeline/` |
| B3 | Match | `/jobs/:source/:jobId/match` | match | `features/job-pipeline/` |
| B4 | Generate Documents | `/jobs/:source/:jobId/sculpt` | drafting | `features/job-pipeline/` |
| B5 | Package & Deployment | `/jobs/:source/:jobId/sculpt` | package | `features/job-pipeline/` |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.