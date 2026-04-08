---
identity:
  node_id: "doc:wiki/drafts/quotation_package_internal_breakdown.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

| Quotation Subsystem | Drift | Notes |

## Details

| Quotation Subsystem | Drift | Notes |
|---|---:|---|
| `modals/AppState` | **75** | Uses mixin base but wrong role; no actor ownership; mostly outside active step-04 runtime path |
| `modals/*` (excluding `AppState`) | **50** | Good mixin alignment, but not primary runtime path right now |
| `views/UI containers` | **50** | Base alignment good; actor bridge is mostly not exercised in active runtime |
| `views/presentational` | **30** | Mostly aligned to `ViewBase`; lower drift than stateful layers |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.