---
identity:
  node_id: "doc:wiki/drafts/factory_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Components are created via factory functions to encapsulate setup:

## Details

Components are created via factory functions to encapsulate setup:

```javascript
// logic/createMyComponentComponent.js

export function createMyComponentComponent(definition, containerId, context = {}) {
  // 1. Create component instance
  const component = new MyComponent(definition, context);
  
  // 2. Initialize (sets up machine, domain logic)
  await component.initialize();
  
  // 3. Mount HTML
  const container = document.getElementById(containerId);
  container.innerHTML = MyComponentHTML;
  
  // 4. Connect Alpine.js
  Alpine.data('myComponentState', () => ({
    ...component.toDisplayObject(),
    updateField: (field, value) => {
      component.setOverride(field, value);
    },
  }));
  Alpine.initTree(container);
  
  // 5. Return public API
  return {
    getState: () => component.toDisplayObject(),
    setState: (newState) => MyComponent.fromSeed(newState, definition),
    setMode: (mode) => component.setMode(mode),
    on: (event, handler) => component.on(event, handler),
  };
}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.