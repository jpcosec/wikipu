---
identity:
  node_id: "doc:wiki/drafts/category_js_the_domain_class.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/minimal_js_pseudo_code.md", relation_type: "documents"}
---

```js

## Details

```js
export class Category {
  #definition   // DB category row (ID_Categoria, Nombre, Icono_UI, ...)
  #items        // Item[] — child item instances

  constructor(definition) {
    this.#definition = definition
    this.#items = []
  }

  // Add an Item instance to this category
  addItem(item) {
    this.#items.push(item)
    return this
  }

  // Remove by item ID
  removeItem(itemId) {
    this.#items = this.#items.filter(i => i.toDisplayObject().id !== itemId)
    return this
  }

  // Push context down to all children
  // Category does not interpret or transform the context — just passes it through
  receiveContext(ctx) {
    this.#items.forEach(item => item.receiveContext(ctx))
    return this
  }

  // Produce render-ready output
  toDisplayObject() {
    const items = this.#items.map(i => i.toDisplayObject())
    const subtotal = items.reduce((sum, i) => sum + (i.total ?? 0), 0)

    return {
      id:          this.#definition.ID_Categoria,
      nombre:      this.#definition.Nombre,
      icono:       this.#definition.Icono_UI ?? null,
      items,
      subtotal,
      itemCount:   items.length,
      hasErrors:   items.some(i => (i.ruleErrors?.length ?? 0) > 0),
      hasWarnings: items.some(i => (i.ruleWarnings?.length ?? 0) > 0),
    }
  }
}
```

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/minimal_js_pseudo_code.md`.