---
identity:
  node_id: "doc:wiki/drafts/closure_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

The `InMemoryStore` instance lives in the factory closure — not in machine context (it's not serializable). Actions call `editService.updateRow / addRow / deleteRow` on the store, then refresh `context.rows` by reading back from the store.

## Details

The `InMemoryStore` instance lives in the factory closure — not in machine context (it's not serializable). Actions call `editService.updateRow / addRow / deleteRow` on the store, then refresh `context.rows` by reading back from the store.

```
factory closure:
  store = createDatabase(seed)   ← mutable, never in context

machine context:
  rows = store.getAll(table)     ← plain snapshot, updated after each write
```

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.