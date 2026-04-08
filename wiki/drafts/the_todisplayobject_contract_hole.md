---
identity:
  node_id: "doc:wiki/drafts/the_todisplayobject_contract_hole.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

`Alpineable` enforces its abstract method by throwing at runtime. The enforcement happens when Alpine attempts to render the component — not at construction time or initialization time. A component that is constructed and tested without ever calling `toDisplayObject()` will pass all its tests and fail only in a browser rendering context.

## Details

`Alpineable` enforces its abstract method by throwing at runtime. The enforcement happens when Alpine attempts to render the component — not at construction time or initialization time. A component that is constructed and tested without ever calling `toDisplayObject()` will pass all its tests and fail only in a browser rendering context.

This creates a false sense of confidence. A component can have a full passing test suite and still break at the only moment that matters to a user. A construction-time assertion (e.g., checking that `toDisplayObject` has been overridden during the base class constructor) would catch the omission earlier. JavaScript does not have abstract methods or static abstract method proposals at the language level (as of current stage), but a runtime check in the constructor is straightforward.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.