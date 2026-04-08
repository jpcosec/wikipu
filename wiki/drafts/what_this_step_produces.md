---
identity:
  node_id: "doc:wiki/drafts/what_this_step_produces.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/objectives.md", relation_type: "documents"}
---

| Artifact | Location |

## Details

| Artifact | Location |
|---|---|
| Save contract (legacy parity + rebuild schema mapping) | `packages/database/src/persistence/SavePayload.md` |
| Snapshot serializer (pure) | `packages/database/src/persistence/serializeQuotation.js` |
| Persistence boundary interface | `packages/database/src/persistence/PersistencePort.js` |
| Local adapter (InMemory/CSV simulation) | `packages/database/src/persistence/LocalPersistenceAdapter.js` |
| Runtime wiring (`confirmSave`, `loadQuotation`, async flow states) | `apps/quotation/state/createPersistedQuotationRuntime.js` |
| UI wiring (`Confirm & Save`) | `apps/quotation/playground/QuotationFlowInternal.html` |
| Bundle wiring | `bundling/createQuotationFlowComponent.js` |

---

Generated from `raw/docs_cotizador/plan/U-1-save/objectives.md`.