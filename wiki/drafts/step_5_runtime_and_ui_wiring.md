---
identity:
  node_id: "doc:wiki/drafts/step_5_runtime_and_ui_wiring.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/agent_guideline.md", relation_type: "documents"}
---

Wire:

## Details

Wire:

- `confirmSave()`
- `loadQuotation(id)`

in runtime and flow component, using only `PersistencePort`.

UI behavior:

- `Confirm & Save` active in validation,
- quotation ID visible in completed stage,
- error path visible when save fails.

---

Generated from `raw/docs_cotizador/plan/U-1-save/agent_guideline.md`.