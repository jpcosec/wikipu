---
identity:
  node_id: "doc:wiki/drafts/step_4_create_the_component_class.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `MyComponent.js`

## Details

**File:** `MyComponent.js`

```javascript
import { createActor } from 'xstate';
import { myMachine } from './machine/myMachine.js';

/**
 * MyComponent - manages the component lifecycle and public API
 */
export class MyComponent {
  #definition;      // Component configuration
  #actor;           // XState actor
  #state;           // Current state

  constructor(definition = {}) {
    this.#definition = definition;
  }

  /**
   * Initialize the component (async setup)
   */
  async initialize() {
    // Create actor from machine
    this.#actor = createActor(myMachine);
    this.#actor.start();

    // Send initialization event
    this.#actor.send({
      type: 'INITIALIZE',
      definition: this.#definition,
    });

    // Store current state
    this.#state = this.#actor.getSnapshot();
  }

  /**
   * Get current state as display object (UI-friendly)
   */
  toDisplayObject() {
    const snapshot = this.#actor?.getSnapshot();
    if (!snapshot) return {};

    return {
      value: snapshot.context.value,
      error: snapshot.context.error,
      isValid: !snapshot.context.error,
      state: snapshot.status,
    };
  }

  /**
   * Load state from seed (serialized state)
   */
  loadFromSeed(seed) {
    if (seed.value !== undefined) {
      this.#actor.send({
        type: 'SET_VALUE',
        value: seed.value,
      });
    }
  }

  /**
   * Serialize component state
   */
  toSeed() {
    return {
      value: this.#state.context.value,
    };
  }

  // === Public API ===

  setValue(value) {
    this.#actor.send({
      type: 'SET_VALUE',
      value,
    });
    this.#state = this.#actor.getSnapshot();
  }

  increment() {
    this.#actor.send({ type: 'INCREMENT' });
    this.#state = this.#actor.getSnapshot();
  }

  decrement() {
    this.#actor.send({ type: 'DECREMENT' });
    this.#state = this.#actor.getSnapshot();
  }

  reset() {
    this.#actor.send({ type: 'RESET' });
    this.#state = this.#actor.getSnapshot();
  }

  // === Introspection ===

  getValue() {
    return this.#state.context.value;
  }

  getError() {
    return this.#state.context.error;
  }

  isValid() {
    return !this.#state.context.error;
  }

  // === Event handling ===

  on(eventName, handler) {
    if (!this.#actor.subscribe) return;
    
    const unsubscribe = this.#actor.subscribe((snapshot) => {
      if (snapshot.status === eventName) {
        handler(snapshot);
      }
    });

    return unsubscribe;
  }
}
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.