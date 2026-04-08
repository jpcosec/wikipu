---
identity:
  node_id: "doc:wiki/drafts/step_7_create_factory_function.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `logic/createMyComponent.js`

## Details

**File:** `logic/createMyComponent.js`

```javascript
import { MyComponent } from '../MyComponent.js';
import templateHtml from '../ui/MyComponent.html?raw';

/**
 * Factory function to create and mount MyComponent
 * 
 * @param {Object} definition - Component configuration
 * @param {string} containerId - DOM element ID where to mount
 * @returns {Object} Public API for the mounted component
 */
export async function createMyComponent(definition = {}, containerId) {
  // 1. Create component instance
  const component = new MyComponent(definition);

  // 2. Initialize (async setup)
  await component.initialize();

  // 3. Mount DOM
  const container = document.getElementById(containerId);
  if (!container) {
    throw new Error(`Container #${containerId} not found`);
  }
  container.innerHTML = templateHtml;

  // 4. Connect Alpine.js
  const displayObject = component.toDisplayObject();
  
  Alpine.data('myComponentState', () => ({
    ...displayObject,

    // Public methods
    setValue(value) {
      component.setValue(value);
      Object.assign(this, component.toDisplayObject());
    },

    increment() {
      component.increment();
      Object.assign(this, component.toDisplayObject());
    },

    decrement() {
      component.decrement();
      Object.assign(this, component.toDisplayObject());
    },

    reset() {
      component.reset();
      Object.assign(this, component.toDisplayObject());
    },

    formatValue(val) {
      return val; // Or use domain logic here
    },
  }));

  Alpine.initTree(container);

  // 5. Return public API
  return {
    getState: () => component.toDisplayObject(),
    setState: (state) => component.loadFromSeed(state),
    getValue: () => component.getValue(),
    setValue: (val) => component.setValue(val),
    increment: () => component.increment(),
    decrement: () => component.decrement(),
    reset: () => component.reset(),
    on: (event, handler) => component.on(event, handler),
  };
}
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.