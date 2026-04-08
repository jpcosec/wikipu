---
identity:
  node_id: "doc:wiki/drafts/item_concept.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

An **Item** represents a specific menu offering with:

## Details

An **Item** represents a specific menu offering with:

- **Static properties:** Name, category, kind (menu, service, extra, setup)
- **Pricing:** Base neto, configurable by duration/quantity
- **Quantity dimensions:** Pax (guests), cantidad (units), duracionMin (minutes)
- **Defaults:** Category-driven defaults for each dimension
- **Rules:** Business rules (blocking, warnings, adjustments) per item scope
- **User overrides:** Track which fields user manually set

### Example Items

| Name | Kind | Category | Base Price | Duration | Pax |
|------|------|----------|-----------|----------|-----|
| Salon | menu | salón | $50/h | 60-480 min | 10-200 |
| Coffee | extra | extras | $2 | None | 1-50 |
| Setup | service | servicio | $1500 flat | 0 | N/A |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.