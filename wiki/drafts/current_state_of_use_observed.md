---
identity:
  node_id: "doc:wiki/drafts/current_state_of_use_observed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

### Active core flow (I-2/I-3)

## Details

### Active core flow (I-2/I-3)

- `item` uses a standalone class (`Item`) plus external machine wrapper, not `ItemBase`.
- `category`, `catalog`, `basket-day`, `basket` are machine-actor factories, not mixin-based component classes.

### Quotation package

- Most quotation classes extend mixin-based base classes (`ViewBase`, `UIContainerBase`, `ModalControllerBase`).
- However, active Step-04 playground runtime is assembled in `apps/quotation/state/createQuotationInternalRuntime.js` from catalog/basket actors, bypassing most package quotation classes.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.