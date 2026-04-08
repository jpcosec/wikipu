---
identity:
  node_id: "doc:wiki/drafts/state_management_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

### Machine Definition

## Details

### Machine Definition

```javascript
// machine/myComponentMachine.js

export const myComponentMachine = setup({
  types: {
    context: MyComponentContext,
    events: MyComponentEvents,
  },
  actions: {
    initializeContext: assign({ /* ... */ }),
    setMode: assign({ /* ... */ }),
    updateState: assign({ /* ... */ }),
    evaluateRules: assign({ /* ... */ }),
  },
  guards: {
    isValid: ({ context }, params) => { /* ... */ },
  },
}).createMachine({
  id: 'my-component',
  initial: 'uninitialized',
  states: {
    uninitialized: {
      on: { INITIALIZE: 'idle' },
    },
    idle: {
      on: {
        SET_MODE: { target: 'idle', actions: 'setMode' },
        UPDATE_STATE: { 
          target: 'recalculating',
          guard: 'isValid',
        },
      },
    },
    recalculating: {
      entry: 'evaluateRules',
      always: 'idle',
    },
  },
});
```

### Context Structure

```javascript
// Machine context contains:
{
  definition: { /* component config */ },
  
  // Display mode
  mode: 'DISPLAY_MODE_1' | 'DISPLAY_MODE_2',
  
  // Component-specific calculated values
  // (varies by component type; examples: quantities, pricing, aggregates)
  calculations: { /* domain-specific data */ },
  appliedRules: [ /* rules that matched */ ],
  
  // Tracking
  userSetFields: Set(['fieldName']),  // Fields manually set by user
  errors: [ /* blocking errors */ ],
  warnings: [ /* non-blocking warnings */ ],
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.