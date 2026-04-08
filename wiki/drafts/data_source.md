---
identity:
  node_id: "doc:wiki/drafts/data_source.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md", relation_type: "documents"}
---

The only source of truth for table data is `data/init/*.csv`.

## Details

The only source of truth for table data is `data/init/*.csv`.
Row shapes are defined by `packages/database/src/Config_Schema.js`.
Do not maintain a separate hand-written fixture for the playground or tests —
load data via `loadSeedFromCsvUrl()` (browser) or `loadSeedFromCsvDir()` (Node.js).

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/minimal_js_pseudo_code.md`.