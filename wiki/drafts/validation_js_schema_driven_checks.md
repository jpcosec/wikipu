---
identity:
  node_id: "doc:wiki/drafts/validation_js_schema_driven_checks.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md", relation_type: "documents"}
---

```js

## Details

```js
export function validateField(tableName, fieldName, value, context) {
  const column = context.schema[tableName].columns.find((c) => c.name === fieldName)
  if (!column) return null

  if (!column.nullable && (value === null || value === undefined || value === '')) {
    return 'Campo requerido'
  }

  if (column.type === 'ENUM' && Array.isArray(column.options) && value != null) {
    if (!column.options.includes(value)) return 'Valor no permitido'
  }

  if (column.type === 'FK' && value != null) {
    const target = context.models[column.ref]
    const fkExists = Boolean(target?.findById(value))
    if (!fkExists) return `No existe referencia en ${column.ref}`
  }

  return null
}

export function validateRow(tableName, row, context) {
  const errors = {}
  for (const key of Object.keys(row)) {
    const error = validateField(tableName, key, row[key], context)
    if (error) errors[key] = error
  }
  return errors
}
```

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md`.