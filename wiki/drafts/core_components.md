---
identity:
  node_id: "doc:wiki/drafts/core_components.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

| Component | Role | Recommended Base | Effective Mixins |

## Details

| Component | Role | Recommended Base | Effective Mixins |
|---|---|---|---|
| `item` | Domain leaf actor component | `ItemBase` | `Actorlike + Prizable + Rulable + Storable + Alpineable` |
| `category` | Domain container actor component | `ContainerBase` | `Actorlike + Aggregable + Rulable + Storable + Alpineable` |
| `catalog` | Domain container actor component | `ContainerBase` | `Actorlike + Aggregable + Rulable + Storable + Alpineable` |
| `basket-day` | Domain container actor component | `ContainerBase` | `Actorlike + Aggregable + Rulable + Storable + Alpineable` |
| `basket` | Domain container actor component | `ContainerBase` | `Actorlike + Aggregable + Rulable + Storable + Alpineable` |

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.