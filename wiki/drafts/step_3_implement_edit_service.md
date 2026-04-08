---
identity:
  node_id: "doc:wiki/drafts/step_3_implement_edit_service.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md", relation_type: "documents"}
---

File: `packages/database/src/services/editService.js`

## Details

File: `packages/database/src/services/editService.js`

Implement pure write helpers over in-memory models:
- `updateRow(table, id, patch)`
- `addRow(table, row)`
- `deleteRow(table, id)`

Rules:
- Return `{ ok, data, error }` for every operation
- Do not throw from public service methods
- Keep implementation synchronous for in-memory workflows

Add tests for success + failure paths.

Commit: `feat: add database edit service for playground writes`

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md`.