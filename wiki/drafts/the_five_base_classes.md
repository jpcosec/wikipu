---
identity:
  node_id: "doc:wiki/drafts/the_five_base_classes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md", relation_type: "documents"}
---

These are the pre-composed entry points. Concrete components extend exactly one.

## Details

These are the pre-composed entry points. Concrete components extend exactly one.

```js
// Domain
ItemBase      = Alpineable(Storable(Rulable(Prizable(Actorlike(class {})))))
ContainerBase = Alpineable(Storable(Rulable(Aggregable(Actorlike(class {})))))

// UI
ModalControllerBase = Alpineable(Eventable(Serviceable(Formable(Modalable(class {})))))
UIContainerBase     = Alpineable(Eventable(Actorlike(class {})))
ViewBase            = Alpineable(Eventable(class {}))
```

Each base class is a fixed composition. Concrete classes only need to extend the appropriate base and implement the abstract methods (`toDisplayObject`, `toStorageObject`, `validate`).

Current usage reality:

- `ModalControllerBase`, `UIContainerBase`, and `ViewBase` are used by quotation modal/view classes.
- The `Item` runtime class follows a standalone pattern and does not currently extend `ItemBase`.
- Container runtimes (`category`, `catalog`, `basket-day`, `basket`) are actor-first modules and do not currently rely on `ContainerBase`.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md`.