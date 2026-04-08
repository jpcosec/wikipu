---
identity:
  node_id: "doc:wiki/drafts/guards.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

| Guard | Logic |

## Details

| Guard | Logic |
|-------|-------|
| `isValidEdit` | `validation.validateField(activeTable, editTarget.field, editTarget.buffer)` returns no error |
| `isValidRow` | `validation.validateRow(activeTable, pendingRow.fields)` returns no errors |
| `isConfirmedDelete` | inline confirm state (a second click on a "confirm" button, not `window.confirm`) |

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.