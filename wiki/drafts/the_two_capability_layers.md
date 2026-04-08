---
identity:
  node_id: "doc:wiki/drafts/the_two_capability_layers.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md", relation_type: "documents"}
---

| Layer  | Mixins                                                  | Concern                                                                  |

## Details

| Layer  | Mixins                                                  | Concern                                                                  |
|--------|---------------------------------------------------------|--------------------------------------------------------------------------|
| Domain | `Prizable`, `Aggregable`, `Rulable`, `Storable`         | Business calculations, quantity resolution, rule evaluation, persistence |
| UI     | `Actorlike`, `Alpineable`, `Eventable`, `Formable`, `Modalable`, `Serviceable` | Actor wiring, view sync, DOM events, form state, dialogs, service injection |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md`.