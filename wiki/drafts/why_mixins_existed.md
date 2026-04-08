---
identity:
  node_id: "doc:wiki/drafts/why_mixins_existed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

Mixins were intended as behavior modules that can be composed into base classes:

## Details

Mixins were intended as behavior modules that can be composed into base classes:

- Domain: `Prizable`, `Aggregable`, `Rulable`, `Storable`
- UI: `Modalable`, `Formable`, `Eventable`, `Serviceable`, `Alpineable`, `Actorlike`

Then reused through base classes:

- `ItemBase`
- `ContainerBase`
- `ModalControllerBase`
- `UIContainerBase`
- `ViewBase`

Intended effect:

1. New components share the same shape.
2. Capabilities are explicit by composition.
3. Actor/UI/event contracts stay consistent.
4. Documentation and code evolve around one pattern.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.