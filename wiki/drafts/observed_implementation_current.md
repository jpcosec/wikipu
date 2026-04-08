---
identity:
  node_id: "doc:wiki/drafts/observed_implementation_current.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

### Item

## Details

### Item

- `packages/components/item/Item.js` is a stateful class with private fields and synchronous `calculate()`.
- The class does not own an internal actor.
- Actor runtime exists outside the class in `packages/components/item/machine/itemMachine.js` (`createItemMachine`, `createItemActor`).

### Category, Catalog, BasketDay, Basket

- These layers are implemented as actor factory modules (`createXActor`) in machine files.
- They do not currently expose actor-owned classes as the primary API.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.