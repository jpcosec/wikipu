---
identity:
  node_id: "doc:wiki/drafts/step_3_define_the_xstate_machine.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `machine/myMachine.js`

## Details

**File:** `machine/myMachine.js`

```javascript
import { setup } from 'xstate';

/**
 * Machine definition for MyComponent
 * Manages state transitions and context updates
 */
export const myMachine = setup({
  types: {
    context: {
      definition: { /* component config */ },
      value: 0,
      prevValue: 0,
      error: null,
    },
    events: {
      SET_VALUE: { value: 'number' },
      INCREMENT: {},
      DECREMENT: {},
      RESET: {},
      VALIDATE: {},
    },
  },
  actions: {
    initializeContext: ({ context }, params) => {
      // Initialize context from definition
      return {
        definition: params.definition,
        value: params.definition.initial ?? 0,
        prevValue: params.definition.initial ?? 0,
        error: null,
      };
    },
    setValue: ({ context }, params) => {
      return {
        ...context,
        prevValue: context.value,
        value: params.value,
      };
    },
    setError: ({ context }, params) => {
      return {
        ...context,
        error: params.message,
      };
    },
    clearError: ({ context }) => {
      return {
        ...context,
        error: null,
      };
    },
  },
  guards: {
    isValidValue: ({ context }, params) => {
      const { min = -Infinity, max = Infinity } = context.definition;
      return params.value >= min && params.value <= max;
    },
  },
}).createMachine({
  id: 'my-component',
  initial: 'uninitialized',
  context: {
    definition: {},
    value: 0,
    prevValue: 0,
    error: null,
  },
  states: {
    uninitialized: {
      on: {
        INITIALIZE: {
          target: 'idle',
          actions: 'initializeContext',
        },
      },
    },
    idle: {
      on: {
        SET_VALUE: {
          guard: 'isValidValue',
          target: 'validating',
          actions: 'setValue',
        },
        INCREMENT: {
          target: 'validating',
          actions: ({ context }) => ({
            ...context,
            value: context.value + (context.definition.step ?? 1),
          }),
        },
        DECREMENT: {
          target: 'validating',
          actions: ({ context }) => ({
            ...context,
            value: context.value - (context.definition.step ?? 1),
          }),
        },
        RESET: {
          actions: ({ context }) => ({
            ...context,
            value: context.definition.initial ?? 0,
            error: null,
          }),
        },
      },
    },
    validating: {
      entry: 'clearError',
      always: 'idle',
    },
    error: {
      on: {
        RESET: {
          target: 'idle',
          actions: 'clearError',
        },
      },
    },
  },
});
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.