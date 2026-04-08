---
identity:
  node_id: "doc:wiki/drafts/alpine_component_data_structure_mount_function.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/minimal_js_pseudo_code.md", relation_type: "documents"}
---

```js

## Details

```js
// createCategoryStandaloneComponent.js

Alpine.data('categoryStandaloneComponent', () => ({

  // ── External state (playground controls) ──────────────
  selectedCategoryId: 'CAT_GASTRO',    // controlled by category dropdown
  paxGlobal:  50,
  dia:        1,
  hora:       '09:00',
  selectedItemToAdd: 'ITEM_CENA',      // controlled by add-item dropdown

  // ── Internal Alpine state ──────────────────────────────
  category: null,     // Category instance
  state:    {},       // category.toDisplayObject() result

  init() {
    this.rebuildCategory()
  },

  rebuildCategory() {
    const catDef = SEED_CATEGORIAS.find(c => c.ID_Categoria === this.selectedCategoryId)
    this.category = new Category(catDef)
    this.refresh()
  },

  addItem() {
    const def = resolveItemDefinition(this.selectedItemToAdd, db)
    const item = Item.fromDefinition(def)
    this.category.addItem(item)
    // Bring item into basket mode and give it current context
    item.addToBasket()
    this.pushContext()
  },

  removeItem(itemId) {
    this.category.removeItem(itemId)
    this.refresh()
  },

  setContext(field, value) {
    this[field] = (field === 'hora') ? value : Number(value)
    this.pushContext()
  },

  pushContext() {
    // Push current external context to all items, then recalculate
    this.category.receiveContext({
      paxGlobal: this.paxGlobal,
      dia:       this.dia,
      hora:      this.hora,
    })
    // Each item must recalculate after receiving new context
    // (implementation detail: expose a recalculateAll() or loop items)
    this.refresh()
  },

  refresh() {
    this.state = this.category.toDisplayObject()
  },
}))
```

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/minimal_js_pseudo_code.md`.