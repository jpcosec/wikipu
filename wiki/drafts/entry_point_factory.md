---
identity:
  node_id: "doc:wiki/drafts/entry_point_factory.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### `bundling/createCotizadorActor.js`

## Details

### `bundling/createCotizadorActor.js`

The main factory function that wires everything together:

```javascript
export function createCotizadorActor(opts = {}) {
  // 1. Create machine from XState
  const machine = createQuotationXStateMachine(quotationAdapters);
  const actor = createActor(machine);

  // 2. Inject store (pluggable)
  const store = opts.store || createTableStoreFromTables(LOCAL_INIT_TABLES);
  actor.getSnapshot().context.store = store;

  // 3. Start actor & bootstrap
  actor.start();
  if (opts.bootstrap !== false) {
    actor.send({ type: 'START_NEW_QUOTATION' });
    // ... more bootstrap events
  }

  return actor;
}
```

**Usage:**
```javascript
// Browser/test
const actor = createCotizadorActor({ paxGlobal: 50 });

// With custom store
const actor = createCotizadorActor({ 
  store: new GasSheetStore(spreadsheet),
  paxGlobal: 100
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.