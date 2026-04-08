---
identity:
  node_id: "doc:wiki/drafts/ui_synchronization.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Alpine.js binds to component state via a reactive proxy:

## Details

Alpine.js binds to component state via a reactive proxy:

```javascript
// ui/MyComponent.html
<div x-data="componentState()" x-effect="syncState()">
  <!-- Mode-specific rendering -->
  <template x-if="mode === 'MODE_1'">
    <div class="component-view-1">
      <h3 x-text="title"></h3>
      <p x-text="description"></p>
    </div>
  </template>

  <!-- Alternative mode -->
  <template x-if="mode === 'MODE_2'">
    <div class="component-view-2">
      <input 
        x-model="state.field" 
        @change="updateField('field', $el.value)"
      />
      <span x-text="`Result: ${displayValue}`"></span>
    </div>
  </template>

  <!-- Errors & Warnings -->
  <template x-if="errors.length">
    <div class="alert alert-danger">
      <template x-for="error in errors">
        <div x-text="error.message"></div>
      </template>
    </div>
  </template>
</div>

<script>
window.componentState = function() {
  return {
    // Mirror component state
    mode: 'MODE_1',
    state: { /* component-specific fields */ },
    errors: [],
    warnings: [],
    
    // Sync updates
    syncState() {
      const display = component.toDisplayObject();
      Object.assign(this, display);
    },
    
    // Handle events
    updateField(fieldName, value) {
      component.setOverride(fieldName, value);
      this.syncState();
    },
  };
};
</script>
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.