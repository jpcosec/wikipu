---
identity:
  node_id: "doc:wiki/drafts/prototype_chain_depth_and_its_costs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

Each mixin application creates one additional link in the prototype chain. Five mixins applied to an empty class produces a six-level chain before `Object.prototype`. Modern JS engines (V8, SpiderMonkey, JavaScriptCore) optimize long chains well, so runtime performance is not a meaningful concern. The costs are tooling and debugging costs.

## Details

Each mixin application creates one additional link in the prototype chain. Five mixins applied to an empty class produces a six-level chain before `Object.prototype`. Modern JS engines (V8, SpiderMonkey, JavaScriptCore) optimize long chains well, so runtime performance is not a meaningful concern. The costs are tooling and debugging costs.

**`instanceof` is unreliable across module boundaries.** If a mixin is imported from two different module instances (e.g., two bundled copies of the same package), `instanceof` checks against the anonymous inner class return false even when the object was created with the "same" mixin. Anonymous inner classes make this especially hard to diagnose.

**Stack traces show anonymous class names.** Each `(Base) => class extends Base { ... }` produces an anonymous class. When an error originates in a mixin method, the stack trace shows the anonymous wrapper name (often an empty string or the variable name at the assignment site), not the component's name. Debugging across a five-deep chain of anonymous classes is tedious.

**`constructor.name` is not reliable.** The concrete class has a name, but intermediate anonymous classes do not. Tooling that uses constructor names for display or serialization may behave unexpectedly on mixin-composed objects.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.