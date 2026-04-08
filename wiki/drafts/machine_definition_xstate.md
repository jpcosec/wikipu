---
identity:
  node_id: "doc:wiki/drafts/machine_definition_xstate.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

```javascript

## Details

```javascript
// machine/itemMachine.js

const itemMachine = setup({
  types: {
    context: {
      itemId: string,
      definition: ItemDefinition,
      context: ItemContext,
      state: ItemState,
    },
    events: {
      INITIALIZE: { definition: ItemDefinition },
      SET_MODE: { mode: 'CATALOG' | 'BASKET' },
      SET_OVERRIDE: { field: string, value: any },
      CLEAR_OVERRIDE: { field: string },
      CALCULATE: {},
    },
  },
  actions: {
    initializeItem: assign(/* ... */),
    setMode: assign(/* ... */),
    applyOverride: assign(/* ... */),
    recalculate: assign(/* ... */),
  },
}).createMachine({
  id: 'item',
  initial: 'uninitialized',
  states: {
    uninitialized: {
      on: { INITIALIZE: 'idle' },
    },
    idle: {
      on: {
        SET_MODE: { actions: 'setMode' },
        SET_OVERRIDE: { actions: 'applyOverride', target: 'recalculating' },
        CLEAR_OVERRIDE: { actions: 'clearOverride', target: 'recalculating' },
      },
    },
    recalculating: {
      entry: 'recalculate',
      always: 'idle',
    },
  },
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.