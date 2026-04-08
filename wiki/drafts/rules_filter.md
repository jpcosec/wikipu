---
identity:
  node_id: "doc:wiki/drafts/rules_filter.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

Only rules that pass **all four conditions** are included:

## Details

Only rules that pass **all four conditions** are included:

| Condition | Meaning |
|-----------|---------|
| `Activo = true` | Rule is in use |
| `Scope = 'ITEM'` | Applies to item-level components |
| `Etapa = 'RESTRICCION_UI'` | Evaluated at render time, not during pricing pipeline |
| `ID_Componente IS NULL OR ID_Componente = itemId` | Global rule or specific to this item |

Rules are sorted by `Prioridad ASC` before being returned.

**Note on production CSV data:** The rules in `data/init/REGLAS_NEGOCIO.csv` all have `ID_Componente: null`. Item-level targeting is encoded inside `Condicion_JSON` (e.g. `{ "===": [{ "var": "linea.ID_Item" }, "ITEM_XYZ"] }`). This means the FK pre-filter passes all 63 rules for every item, and the `RulesCoordinator` does the actual item-level filtering at evaluation time via JSON-Logic. This is correct behavior — the pre-filter is an optimization that is not used by the current data set.

---

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.