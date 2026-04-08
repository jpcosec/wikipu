---
identity:
  node_id: "doc:wiki/drafts/when_to_add_a_new_mixin.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

Add a new mixin when:

## Details

Add a new mixin when:
- A capability is genuinely orthogonal — it could be meaningful on both domain and UI roles
- The capability has its own state fields that no existing mixin owns
- The capability is needed on 3 or more concrete components

Do not add a mixin for:
- Logic specific to a single component (put it in the component class)
- A helper utility with no instance state (use a plain function)
- A composition of two existing mixins (define a new base class instead)

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.