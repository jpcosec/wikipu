---
identity:
  node_id: "doc:wiki/drafts/gas_app.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/runtime-environments.md", relation_type: "documents"}
---

- Purpose: full integrated quotation application development

## Details

- Purpose: full integrated quotation application development
- Source: `apps/gas/`
- Local development: `npm run dev:gas`
- Runtime contract: integrated app only, no sandbox-only controls
- Local persistence mode: `tools/serve-local.mjs` + `data/db.json`
- Real persistence mode: Apps Script backend in `gas/Code.gs` + Google Sheets
- Rule: any end-to-end business flow must be validated here

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/runtime-environments.md`.