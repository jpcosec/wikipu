---
identity:
  node_id: "doc:wiki/drafts/4_node_implementation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md", relation_type: "documents"}
---

### Affected Nodes

## Details

### Affected Nodes

| Node Name | File | Changes |
|-----------|------|---------|
| `build_application_context` | `src/nodes/strategy/build_context.py` | NEW |
| `review_application_context` | `src/nodes/strategy/review_context.py` | NEW |

### Edge Transitions

```
match → build_application_context → review_application_context → drafting

Conditions:
- build_application_context: Always (after match)
- review_application_context: Only if HITL required
- drafting: After review (or skip if no HITL)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md`.