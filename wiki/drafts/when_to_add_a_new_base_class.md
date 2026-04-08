---
identity:
  node_id: "doc:wiki/drafts/when_to_add_a_new_base_class.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

Add a new base class when:

## Details

Add a new base class when:
- A cluster of components shares a mixin composition that does not match any existing base
- You find yourself applying the same 3+ mixins in the same order in multiple concrete classes

Keep base classes thin — they should only contain the `extends` line. No methods, no fields, no logic.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.