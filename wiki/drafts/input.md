---
identity:
  node_id: "doc:wiki/drafts/input.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

```js

## Details

```js
resolveItemDefinition(itemId: string, db: {
  items:      ITEM_CATALOGO[],
  categorias: CATEGORIAS[],
  perfiles:   PERFILES_PRECIO[],
  reglas:     REGLAS_NEGOCIO[]
}): ResolvedItemDefinition
```

Throws a descriptive error if `itemId` is not found.

---

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.