---
identity:
  node_id: "doc:wiki/drafts/integration_points.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

### With Basket Container

## Details

### With Basket Container
Items are added to a basket and sync pricing totals:

```javascript
// In parent container
const basket = new Basket();
const item = new Item(definition);

item.on('priceChange', () => {
  basket.recalculateTotals();  // Parent observes changes
});
```

### With Database
Item definitions come from database, rules too:

```javascript
const catalog = await store.getCatalog();
const itemDef = catalog.find(i => i.itemId === 'SALON_01');
const item = new Item(itemDef, { rules: itemDef.rules });
```

### With Rules Engine
Rules are evaluated by the embedded `RulesCoordinator`:

```javascript
const coordinator = new RulesCoordinator('ITEM', rules);
const result = coordinator.evaluate({
  itemId: this.itemId,
  pax: this.quantities.pax,
  cantidad: this.quantities.cantidad,
  duracionMin: this.quantities.duracionMin,
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.