---
identity:
  node_id: "doc:wiki/drafts/events_full_list.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

| Event | Payload |

## Details

| Event | Payload |
|-------|---------|
| SELECT_TABLE | `{ tableId }` |
| SORT | `{ column }` (toggles dir if same column) |
| TOGGLE_FILTER | `{ tag }` |
| DOUBLE_CLICK_CELL | `{ rowId, field, value }` |
| UPDATE_BUFFER | `{ value }` |
| COMMIT_EDIT | — |
| CANCEL_EDIT | — |
| ADD_ROW | — |
| COMMIT_ADD | — |
| CANCEL_ADD | — |
| DELETE_ROW | `{ rowId }` |

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.