---
identity:
  node_id: "doc:wiki/drafts/entrypoint.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

```python

## Details

```python
from src.graph import create_prep_match_app, run_prep_match

# Build the app
app = create_prep_match_app()

# Or run directly
result = run_prep_match(initial_state, resume=False)
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.