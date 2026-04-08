---
identity:
  node_id: "doc:wiki/drafts/composition_as_declaration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

The base class definition is the capability specification. Reading:

## Details

The base class definition is the capability specification. Reading:

```js
class Item extends ItemBase { ... }
```

immediately tells you: this class can price, evaluate rules, receive inherited context, store to a database, bridge an actor, and sync to Alpine. You do not need to read the implementation to understand the contract.

This is the primary ergonomic benefit of pre-composed base classes over per-class mixin application. When a developer opens an unknown component file, the `extends XxxBase` line is the entire capability summary.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.