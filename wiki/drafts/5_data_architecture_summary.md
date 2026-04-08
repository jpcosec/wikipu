---
identity:
  node_id: "doc:wiki/drafts/5_data_architecture_summary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md", relation_type: "documents"}
---

| Component | Location | Function |

## Details

| Component | Location | Function |
|-----------|----------|---------|
| CV Profile | `data/master/profile.json` | Your structured base history |
| Evidence Bank | `data/master/evidence/` | HITL-validated links and proofs |
| Review Nodes | `data/jobs/<source>/<job_id>/review/` | Stage-specific corrections |
| Document Delta | `data/jobs/<source>/<job_id>/strategy/` | Change instructions for current application |
| Filters | `data/master/filters/` | Learned exclusions from past applications |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md`.