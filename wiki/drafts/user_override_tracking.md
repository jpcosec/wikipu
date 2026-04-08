---
identity:
  node_id: "doc:wiki/drafts/user_override_tracking.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

The Item tracks which fields users **manually set** vs. which are **auto-calculated**:

## Details

The Item tracks which fields users **manually set** vs. which are **auto-calculated**:

```javascript
// Private field: Set of field names user explicitly set
#userSetFields = new Set()

// Public methods:
setOverride(field, value) {
  context[field] = value
  #userSetFields.add(field)        // Mark as user-set
}

clearOverride(field) {
  delete context[field]
  #userSetFields.delete(field)     // Mark as auto
}

isUserSet(field) {
  return #userSetFields.has(field)
}

toDisplayObject() {
  return {
    ...currentState,
    isUserSetPax: this.isUserSet('pax'),
    isUserSetCantidad: this.isUserSet('cantidad'),
    isUserSetDuracion: this.isUserSet('duracionMin'),
    userSetFields: Array.from(#userSetFields),  // For serialization
  }
}
```

**Use case:** UI displays **orange borders** around user-set fields to signal overrides.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.