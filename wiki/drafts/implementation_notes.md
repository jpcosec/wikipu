---
identity:
  node_id: "doc:wiki/drafts/implementation_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/phases/03_runtime_wiring.md", relation_type: "documents"}
---

- The quotation flow owner is the persisted quotation runtime state machine.

## Details

- The quotation flow owner is the persisted quotation runtime state machine.
- `serializeQuotation(...)` is executed inside runtime save orchestration, never from Alpine/UI.
- Save/load are modeled as real runtime stages (`saving`, `loadingQuotation`) before returning to `completed` or the editable flow.
- Storage remains injected through `PersistencePort`, so local and GAS adapters stay behind the same boundary.

Generated from `raw/docs_cotizador/plan/U-1-save/phases/03_runtime_wiring.md`.