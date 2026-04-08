---
identity:
  node_id: "doc:wiki/drafts/quotation_components.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

| Component Group | Role | Recommended Base | Effective Mixins |

## Details

| Component Group | Role | Recommended Base | Effective Mixins |
|---|---|---|---|
| `quotation/modals/*` (initializer/selectors/viewers) | Modal controllers | `ModalControllerBase` | `Modalable + Formable + Serviceable + Eventable + Alpineable` |
| `quotation/views/QuotationView`, `quotation/views/Sidebar`, `quotation/views/Catalog`, `quotation/views/Basket` | UI containers | `UIContainerBase` | `Actorlike + Eventable + Alpineable` |
| `quotation/views/*` presentational (`DayTabs`, `DayAccordion`, `ItemAccordion`, `CatalogItemCard`, `CategoryGroup`, `QuotationHeader`, `QuotationTotals`, `ValidationSummary`, `CompletionSuccess`, `HomePage`) | Presentational views | `ViewBase` | `Eventable + Alpineable` |
| `quotation/modals/AppState` | Flow state controller | **New base recommended** (`FlowControllerBase`) | `Actorlike + Eventable + Serviceable + Alpineable` |

Note: `AppState` currently extends `ModalControllerBase`, which is semantically mismatched (it is flow state, not a modal/form controller).

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.