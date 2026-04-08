---
identity:
  node_id: "doc:wiki/drafts/5_complete_data_flow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md", relation_type: "documents"}
---

```

## Details

```
[data/master]  ──evidences──>  [scrape]  ──text──>  [extract]  ──requirements──>  [match]
                                                                                        │
                                                                                        ↓
                                                           [global evidence_bank]  <──augmentation
                                                                                        │
                                                                                        ↓
                                                           [strategy/delta]  ──>  [drafting]
                                                                                        │
                                                                                        ↓
                                                           [render]  ──>  [final/package]
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md`.