---
identity:
  node_id: "doc:wiki/drafts/what_is_a_functional_mixin.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md", relation_type: "documents"}
---

A functional mixin is a higher-order function that accepts a base class and returns a new class that extends it with additional methods and fields. Unlike classical inheritance (`extends SomeConcreteClass`), mixins add capabilities orthogonally — any class can receive any mixin regardless of its existing ancestry. The mixin owns its fields and methods; the base it wraps is irrelevant to its logic.

## Details

A functional mixin is a higher-order function that accepts a base class and returns a new class that extends it with additional methods and fields. Unlike classical inheritance (`extends SomeConcreteClass`), mixins add capabilities orthogonally — any class can receive any mixin regardless of its existing ancestry. The mixin owns its fields and methods; the base it wraps is irrelevant to its logic.

```js
// Pattern
const WithCapability = (Base) => class extends Base {
  /* methods and fields */
};

// Composition (applied innermost first)
class MyClass extends WithCapabilityC(WithCapabilityB(WithCapabilityA(class {}))) {}
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md`.