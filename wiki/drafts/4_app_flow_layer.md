---
identity:
  node_id: "doc:wiki/drafts/4_app_flow_layer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Introduce `AppFlow` (or `AppFlowBase` + concrete `QuotationAppFlow`):

## Details

Introduce `AppFlow` (or `AppFlowBase` + concrete `QuotationAppFlow`):

- owns stage transitions (`browse -> client -> basket -> validation -> completed`)
- owns active scenario and context policy
- coordinates root components (catalog, basket, quotation summary)
- replaces scattered runtime orchestration logic with a single, testable flow object

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.