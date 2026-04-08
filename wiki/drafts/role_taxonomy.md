---
identity:
  node_id: "doc:wiki/drafts/role_taxonomy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

| Role | Description | Base class |

## Details

| Role | Description | Base class |
|------|-------------|------------|
| Domain leaf | A single priceable, ruleable, storable unit | `ItemBase` |
| Domain container | A collection manager that aggregates children and propagates context | `ContainerBase` |
| Modal controller | A dialog/wizard with form state, service access, and emitted events | `ModalControllerBase` |
| UI container | A stateful view that bridges an XState actor to Alpine rendering | `UIContainerBase` |
| Presentational view | A display-only component that emits events but holds no domain state | `ViewBase` |

Choosing the wrong role creates structural problems. A component that acts as a container but extends `ItemBase` will have pricing machinery with no children. A component that acts as a leaf but extends `ContainerBase` will have child management with no pricing.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.