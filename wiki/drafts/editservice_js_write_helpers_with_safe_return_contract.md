---
identity:
  node_id: "doc:wiki/drafts/editservice_js_write_helpers_with_safe_return_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md", relation_type: "documents"}
---

```js

## Details

```js
export function updateRow(model, id, patch) {
  try {
    const row = model.findById(id)
    if (!row) return { ok: false, data: null, error: `Row not found: ${id}` }
    const updated = model.update({ ...row, ...patch })
    return { ok: true, data: updated, error: null }
  } catch (error) {
    return { ok: false, data: null, error: String(error.message || error) }
  }
}

export function addRow(model, row) {
  try {
    return { ok: true, data: model.create(row), error: null }
  } catch (error) {
    return { ok: false, data: null, error: String(error.message || error) }
  }
}

export function deleteRow(model, id) {
  try {
    const deleted = model.deleteById(id)
    if (!deleted) return { ok: false, data: null, error: `Row not found: ${id}` }
    return { ok: true, data: { id }, error: null }
  } catch (error) {
    return { ok: false, data: null, error: String(error.message || error) }
  }
}
```

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md`.