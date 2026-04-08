---
identity:
  node_id: "doc:wiki/drafts/review_routing.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

The `review_match` node uses conditional edges:

## Details

The `review_match` node uses conditional edges:

| Decision | Next Node |
|----------|-----------|
| `approve` | `generate_documents` |
| `request_regeneration` | `match` |
| `reject` | END |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.