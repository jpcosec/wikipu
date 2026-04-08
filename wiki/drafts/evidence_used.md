---
identity:
  node_id: "doc:wiki/drafts/evidence_used.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-11-vistas-design-map.md", relation_type: "documents"}
---

- Product intent source: `/home/jp/CotizadorLodge/Vistas.md`.

## Details

- Product intent source: `/home/jp/CotizadorLodge/Vistas.md`.
- Runtime validation (not code-only): GAS preview app at `http://localhost:8082` tested with Playwright.
  - Verified flow: start quotation -> select client -> basket/day editor -> copy/duplicate/remove -> validation preview.
- Workspace contracts reviewed for traceability:
  - `apps/quotation/playground/QuotationFlowInternal.html`
  - `apps/quotation/state/createQuotationInternalRuntime.js`
  - `packages/components/basket/machine/basketMachine.js`
  - `apps/sandbox/playground/database/DatabasePlayground.html`
  - `packages/database/src/machine/databaseMachine.js`

Generated from `raw/docs_cotizador/docs/plans/2026-03-11-vistas-design-map.md`.