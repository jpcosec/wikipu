---
identity:
  node_id: "doc:wiki/drafts/current_flow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

```

## Details

```
scrape → translate_if_needed → extract_understand → match → review_match
                                                            ↓
                                              ┌─────────────┼─────────────┐
                                              ↓             ↓             ↓
                                          approve    request_regen    reject
                                              ↓             ↓             ↓
                                       generate_documents → match (loop)
                                              ↓
                                           render
                                              ↓
                                           package
                                              ↓
                                             END
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.