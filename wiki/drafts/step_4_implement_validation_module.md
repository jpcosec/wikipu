---
identity:
  node_id: "doc:wiki/drafts/step_4_implement_validation_module.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md", relation_type: "documents"}
---

File: `packages/database/src/validation.js`

## Details

File: `packages/database/src/validation.js`

Build per-table validation rules from `Config_Schema.js`:
- Required fields
- Enum/allowed-value checks
- FK existence checks

Expose:
- `validateField(table, field, value, context)`
- `validateRow(table, row, context)`

Add tests for field-level and row-level validation behavior.

Commit: `feat: add schema-derived validation for db playground`

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md`.