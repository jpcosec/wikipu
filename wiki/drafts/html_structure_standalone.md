---
identity:
  node_id: "doc:wiki/drafts/html_structure_standalone.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

**Location:** `ui/ItemDisplay.html` (production view)

## Details

**Location:** `ui/ItemDisplay.html` (production view)

```html
<div id="item-container" x-data="itemComponent()" class="item">
  <!-- CATALOG MODE -->
  <template x-if="mode === 'CATALOG'">
    <div class="item-catalog-card">
      <div class="card-header">
        <h3 x-text="name"></h3>
        <span class="category-badge" x-text="category"></span>
      </div>
      <div class="card-body">
        <p class="formula" x-text="priceFormula"></p>
        <p class="policy" x-text="policy"></p>
        <button @click="addToBasket()">Add to Order</button>
      </div>
    </div>
  </template>

  <!-- BASKET MODE -->
  <template x-if="mode === 'BASKET'">
    <div class="item-basket-container">
      <h4 x-text="name"></h4>
      
      <!-- Quantity Controls -->
      <div class="quantity-controls">
        <label>Pax:</label>
        <input x-model.number="quantities.pax" 
               :class="{ 'user-set': isUserSetPax }"
               @change="setOverride('pax', $el.value)" />
        <span x-show="isUserSetPax" class="badge">manual</span>
      </div>

      <div class="quantity-controls">
        <label>Units:</label>
        <input x-model.number="quantities.cantidad" 
               :class="{ 'user-set': isUserSetCantidad }"
               @change="setOverride('cantidad', $el.value)" />
        <span x-show="isUserSetCantidad" class="badge">manual</span>
      </div>

      <!-- Price Display -->
      <div class="pricing-display">
        <span>Subtotal: <strong x-text="`$${pricing.subtotal}`"></strong></span>
        <span>Total: <strong x-text="`$${pricing.total}`"></strong></span>
      </div>

      <!-- Rules Display -->
      <div x-show="appliedRules.length">
        <h6>Applied Rules</h6>
        <template x-for="rule in appliedRules">
          <div class="rule-item">
            <span x-text="rule.description"></span>
          </div>
        </template>
      </div>

      <!-- Errors/Warnings -->
      <div x-show="errors.length" class="alert alert-danger">
        <template x-for="error in errors">
          <div x-text="error.message"></div>
        </template>
      </div>

      <button @click="remove()">Remove Item</button>
    </div>
  </template>
</div>
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.