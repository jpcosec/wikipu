---
identity:
  node_id: "doc:wiki/drafts/profile_resolution_rule.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

```

## Details

```
resolvedPerfilId = item.ID_Perfil_Precio_Override ?? categoria.ID_Perfil_Precio_Default
```

Item override wins. If the item has no override (`null`), the category's default profile is used. If neither resolves, the function throws.

---

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.