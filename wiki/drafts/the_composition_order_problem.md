---
identity:
  node_id: "doc:wiki/drafts/the_composition_order_problem.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

The order `Outer(Middle(Inner(Base)))` determines which class is higher in the prototype chain. In most cases, order does not affect observable behavior — each mixin adds distinct fields and methods. But it matters when:

## Details

The order `Outer(Middle(Inner(Base)))` determines which class is higher in the prototype chain. In most cases, order does not affect observable behavior — each mixin adds distinct fields and methods. But it matters when:

- Two mixins both initialize a field with the same name (last one applied wins at prototype level, but instance-field initialization in class bodies runs at construction time, so the innermost constructor runs first — the opposite of what the wrapping order implies)
- Method resolution falls through the chain: if a method is defined in both an inner and an outer mixin, the outer definition (higher in the chain) shadows the inner one

The composition order is specified once in the base class definition and never verified thereafter. Swapping two mixin positions may produce subtly wrong behavior with no error. Without a documented rationale for each position in each base class, engineers cannot safely reorder compositions when adding new mixins.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.