---
identity:
  node_id: "doc:wiki/drafts/boundary_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/runtime-environments.md", relation_type: "documents"}
---

- `packages/` contains shared domain/runtime code used by both environments

## Details

- `packages/` contains shared domain/runtime code used by both environments
- `apps/quotation/playground/` is sandbox-oriented wiring and should not be the source of truth for GAS screens
- `apps/gas/Quotation_App_Source.html` is the source template for the GAS app shell
- `apps/gas/Stores_QuotationApp.html` must pass explicit GAS capabilities into the app component
- `apps/gas/Local_GAS_Shim.html` is for local GAS development only and proxies `google.script.run` to the Node local server
- Sandbox-only affordances must be capability-gated and hidden in GAS

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/runtime-environments.md`.