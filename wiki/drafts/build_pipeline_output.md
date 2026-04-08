---
identity:
  node_id: "doc:wiki/drafts/build_pipeline_output.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### Local Bundle (Browser)

## Details

### Local Bundle (Browser)

```
npm run build:bundle
    │
    ├─→ generate_local_init_tables.mjs
    │   (Creates bundling/generated/localInitTables.js)
    │
    └─→ rollup bundler
        Input: bundling/entry.js
            │
            ├─ AlpineXStateBridge (frontend)
            ├─ createCotizadorActor (wires everything)
            │   ├─ XState machine
            │   ├─ Database store
            │   ├─ Domain/Pricing logic
            │   └─ Local init data
            │
            └─ Resolves all node_modules (@xstate/...)
            
        Output: dist/quotation-engine.iife.js
                (354KB, 10,989 lines, browser-ready)
```

### GAS Bundle (Google Apps Script)

```
npm run build:gas
    │
    ├─→ reset_gas_workspace.mjs
    │   (Cleans /gas directory)
    │
    ├─→ generate_gas_runtime_bundle.mjs
    │   (Creates GAS-compatible wrapper)
    │
    └─→ generate_gas_code.mjs
        (Generates gas/Code.gs with embedded logic)
        
        Output: gas/Code.gs (GAS-compatible runtime)
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.