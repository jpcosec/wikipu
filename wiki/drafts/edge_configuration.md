---
identity:
  node_id: "doc:wiki/drafts/edge_configuration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

```python

## Details

```python
PREP_MATCH_LINEAR_EDGES = (
    ("scrape", "translate_if_needed"),
    ("translate_if_needed", "extract_understand"),
    ("extract_understand", "match"),
    ("match", "review_match"),
    ("generate_documents", "render"),
    ("render", "package"),
)

PREP_MATCH_REVIEW_TRANSITIONS = {
    "review_match": {
        "approve": "generate_documents",
        "request_regeneration": "match",
        "reject": END_NODE,
    }
}
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.