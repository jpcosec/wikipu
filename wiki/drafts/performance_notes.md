---
identity:
  node_id: "doc:wiki/drafts/performance_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

- **Caching:** Rule evaluation results cached; invalidated only on definition/rule changes

## Details

- **Caching:** Rule evaluation results cached; invalidated only on definition/rule changes
- **Pure functions:** Pricing calculations have no I/O or async operations
- **Lazy evaluation:** Display strings computed only on request
- **No polling:** State changes propagated via XState, not polling loops

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.