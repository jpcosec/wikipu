---
identity:
  node_id: "doc:wiki/drafts/7_common_mistakes_and_how_to_avoid_them.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

### Mistake 1: Composing Mixins Directly on a Concrete Class

## Details

### Mistake 1: Composing Mixins Directly on a Concrete Class

**Problem:** Instead of extending a pre-composed base class, developers apply mixins directly on the concrete class to "get just what they need" — skipping mixins they consider unnecessary.

**Before:**
```js
// Skips Actorlike — actor wiring will silently fail
export class SpecialItem extends Alpineable(Storable(Rulable(Prizable(class {})))) {
  toDisplayObject() { return {}; }
  toStorageObject() { return {}; }
}
```

**After:**
```js
// Always extend the canonical base class for your role
export class SpecialItem extends ItemBase {
  toDisplayObject() { return {}; }
  toStorageObject() { return {}; }
}
```

**Why:** The base classes encode approved composition orders and dependency pairs. Ad-hoc composition risks omitting a required mixin and getting silent failures. If a component genuinely needs fewer capabilities, discuss adding a new base class — don't compose ad-hoc.

---

### Mistake 2: Redeclaring Mixin-Owned Fields in a Subclass

**Problem:** A subclass redeclares a field that a mixin already initializes as a class field, shadowing the mixin's version at the instance level.

**Before:**
```js
export class ProductItem extends ItemBase {
  _rules = [];  // Shadows Rulable._rules on the instance.
                // setRules() sets the prototype-level field;
                // evaluateRules() reads the instance-level [] → always empty.
}
```

**After:**
```js
export class ProductItem extends ItemBase {
  // Only declare fields that no mixin owns.
  Nombre = null;
  _profile = null;
  _category = null;
}
```

**Why:** Mixin-owned fields (`_rules`, `_children`, `_actorRef`, `_services`, `_listeners`, `_formState`, `_formErrors`, `_isDirty`, `pax`, `cantidad`, `duracion`, etc.) must not appear as field declarations in any subclass. Treat them as a reserved namespace.

---

### Mistake 3: Calling `toDisplayObject()` Before the Full Update Cycle

**Problem:** Alpine calls `toDisplayObject()` reactively, but the component hasn't completed the full update cycle — returning stale or partially calculated state.

**Before:**
```js
// Only received context — rules not evaluated, price not calculated
item.receiveContext(env);
renderAlpine(item.toDisplayObject());  // price: 0, applied rules: []
```

**After:**
```js
// Always complete the full cycle before exposing display state
item
  .receiveContext(env)
  .evaluateRules(evaluator)
  .resolveQuantities()
  .calculatePrice();
renderAlpine(item.toDisplayObject());
```

**Why:** The domain update methods form a pipeline where each step depends on the previous. Skipping `calculatePrice()` leaves `_price` at `null`. `toDisplayObject()` faithfully returns `total: 0`. The full cycle must complete before reading display state.

---

### Mistake 4: Not Cleaning Up Actor Subscriptions

**Problem:** When a child component is removed, its actor subscription is not cancelled. The callback fires on subsequent actor state changes, operating on a domain object that no longer belongs to the tree.

**Before:**
```js
function addChild(def, childActor) {
  childActor.subscribe(() => container.aggregate()); // never cleaned up
  childActor.start();
}
// No removeChild that cancels the subscription
```

**After:**
```js
const subscriptions = new Map();

function addChild(id, childActor) {
  const sub = childActor.subscribe(() => container.aggregate());
  subscriptions.set(id, sub);
  childActor.start();
}

function removeChild(id) {
  subscriptions.get(id)?.unsubscribe();
  subscriptions.delete(id);
  childActors.get(id)?.stop();
}
```

**Why:** XState subscriptions hold a reference to the callback, which may close over domain objects, containers, or Alpine store references. A leaked subscription prevents garbage collection and causes phantom updates after the child is removed.

---

### Mistake 5: Putting Business Logic Inside `toDisplayObject()`

**Problem:** `toDisplayObject()` accumulates derived computations, conditional formatting, and business logic — making it a second calculation layer that can diverge from the domain object's actual state.

**Before:**
```js
toDisplayObject() {
  // Business logic here — wrong layer
  const effectivePax = this.paxIsUserSet ? this.pax : (this._inheritedContext.pax ?? 0);
  const adjustedPrice = this._profile?.tieneDescuento
    ? this._price * 0.9
    : this._price;
  return {
    pax:   effectivePax,
    price: adjustedPrice / effectivePax,
  };
}
```

**After:**
```js
// Business logic in domain methods:
// - resolveQuantities() determines effective pax
// - calculatePrice() applies pricing profile (via _pricingFn)
// toDisplayObject() only reads already-computed fields

toDisplayObject() {
  return {
    pax:   this.pax,           // resolved by resolveQuantities()
    price: this.displayPrice,  // computed by calculatePrice()
    total: this.total,
  };
}
```

**Why:** `toDisplayObject()` is called by Alpine on every render cycle — potentially dozens of times per user gesture. Business logic inside it runs redundantly, cannot be unit-tested independently of Alpine, and creates divergence between what the domain object "knows" and what Alpine "shows." All calculations belong in the domain update cycle; `toDisplayObject()` is a read-only projection.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.