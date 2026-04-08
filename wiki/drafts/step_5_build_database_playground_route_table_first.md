---
identity:
  node_id: "doc:wiki/drafts/step_5_build_database_playground_route_table_first.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md", relation_type: "documents"}
---

Files:

## Details

Files:
- `apps/sandbox/routes/step-I1-database/index.html`
- `apps/sandbox/index.html` (add nav link)
- `tools/serve-sandbox.mjs` (add route `'step-I1-database'`)

The playground should support:
1. Table selector for all 11 real tables (loaded from `data/init/*.csv`)
2. Sortable headers
3. Tag filters (category for items, action type for rules)
4. Inline cell edit with Enter/Escape behavior
5. Add row flow with `_new: true` pending state and cancel/remove
6. Validation feedback on invalid edits

Manual test:
- Open `http://localhost:8090/step-I1-database/`
- Browse all tables and verify field names + row rendering
- Edit invalid value and verify save is blocked with visual error
- Add row, save valid row, and cancel pending row
- Double-click cell to edit, confirm with Enter, cancel with Escape

Commit: `feat: add editable database playground (step-I1)`

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md`.