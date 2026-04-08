---
identity:
  node_id: "doc:wiki/drafts/runtime_flow_example.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### Create a quotation:

## Details

### Create a quotation:

1. **User clicks "New Quotation"** (Alpine.js)
   ```
   AlpineXStateBridge.sendEvent('START_NEW_QUOTATION')
   ```

2. **XState processes event**
   ```
   Machine: idle → creating
   Action: loadCatalog() from database
   Action: initializeContext()
   ```

3. **Pricing engine calculates**
   ```
   Pricing.pipeline({
     header: { paxGlobal: 50, fechaEvento: '2026-02-24' },
     lineas: [],
     catalog: context.catalog,
     rules: context.rules
   }) → { lineas: [], totals: { ... } }
   ```

4. **State updated in context**
   ```
   context.lineas = [ ... ]
   context.totals = { subtotal: 0, total: 0 }
   ```

5. **AlpineXStateBridge syncs to UI**
   ```
   Alpine.js re-renders with new totals
   ```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.