---
identity:
  node_id: "doc:wiki/drafts/current_operational_nodes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md", relation_type: "documents"}
---

The prep-match flow uses these nodes in sequence:

## Details

The prep-match flow uses these nodes in sequence:

```
scrape → translate_if_needed → extract_understand → match → review_match
                                                            ↓
                                              ┌─────────────┼─────────────┐
                                              ↓             ↓             ↓
                                          approve    request_regen    reject
                                              ↓             ↓             ↓
                                       generate_documents → match
                                              ↓
                                           render → package → END
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md`.