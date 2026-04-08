---
identity:
  node_id: "doc:wiki/drafts/state_field_namespace_collisions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

All mixin-added fields exist directly on the instance. There is no encapsulation between mixin-owned state. A subclass that accidentally declares a field with the same name as a mixin field — or a mixin that adds a field with the same name as an existing mixin — silently shadows the original.

## Details

All mixin-added fields exist directly on the instance. There is no encapsulation between mixin-owned state. A subclass that accidentally declares a field with the same name as a mixin field — or a mixin that adds a field with the same name as an existing mixin — silently shadows the original.

Example scenario: an engineer adds `_rules = []` in a concrete component's constructor body, intending it as a local array for a different purpose. This re-declares the field initialized by the rules mixin on the instance. The rules mixin's `evaluateRules` will now iterate the empty array even after `setRules()` was called, because the instance-level field shadows the prototype-level one. No error is thrown. The component appears to evaluate no rules.

Prefixing mixin-private fields (e.g., `_Rulable_rules`) would eliminate collision risk at the cost of readability. The current pattern accepts the collision risk in exchange for clean field names.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.