---
identity:
  node_id: "doc:wiki/drafts/step_6_create_html_template.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `ui/MyComponent.html`

## Details

**File:** `ui/MyComponent.html`

```html
<div id="my-component" x-data="myComponentState()" class="my-component">
  <!-- Display current value -->
  <div class="value-display">
    <span class="label">Value:</span>
    <span class="value" x-text="formatValue(value)"></span>
  </div>

  <!-- Controls -->
  <div class="controls">
    <button @click="decrement()" class="btn btn-decrement">-</button>
    <input 
      x-model.number="value" 
      @change="setValue($el.value)"
      type="number"
      class="input-value"
    />
    <button @click="increment()" class="btn btn-increment">+</button>
    <button @click="reset()" class="btn btn-reset">Reset</button>
  </div>

  <!-- Error message -->
  <template x-if="error">
    <div class="alert alert-error" x-text="error"></div>
  </template>
</div>

<script>
window.myComponentState = function() {
  return {
    value: 0,
    error: null,

    formatValue(val) {
      return `${val}`;
    },

    setValue(val) {
      this.value = parseInt(val, 10);
      // In real component, would send event to machine
    },

    increment() {
      this.value += 1;
    },

    decrement() {
      this.value -= 1;
    },

    reset() {
      this.value = 0;
      this.error = null;
    },
  };
};
</script>
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.