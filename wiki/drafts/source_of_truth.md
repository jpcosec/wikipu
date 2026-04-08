---
identity:
  node_id: "doc:wiki/drafts/source_of_truth.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/DEPLOYMENT/gas-bundling.md", relation_type: "documents"}
---

- GAS static templates: `apps/gas/*.html`

## Details

- GAS static templates: `apps/gas/*.html`
- GAS manifest: `apps/gas/appsscript.json`
- Quotation shell template: `apps/quotation/playground/QuotationFlowInternal.html`
- Runtime sections injected into quotation shell:
  - `packages/components/item/ui/playgroundItemSections.js`

Do not edit `gas/` manually. `npm run build:gas` recreates it.

Generated from `raw/docs_cotizador/docs/DEPLOYMENT/gas-bundling.md`.