---
identity:
  node_id: "doc:wiki/drafts/core_idea.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Create a single root `ComponentBase` and build a tree of role-specific base classes from it.

## Details

Create a single root `ComponentBase` and build a tree of role-specific base classes from it.

Today, base classes are composed from `class {}`. The proposal is to compose them from `ComponentBase` so all components share the same lifecycle and identity contract.

### Target base tree

```text
ComponentBase
├─ DomainComponentBase
│  ├─ ItemBase
│  └─ ContainerBase
├─ UIComponentBase
│  ├─ ViewBase
│  ├─ UIContainerBase
│  └─ ModalControllerBase
└─ FlowComponentBase
   └─ AppFlowBase
```

Notes:

- `ItemBase`, `ContainerBase`, `ViewBase`, `UIContainerBase`, and `ModalControllerBase` keep using mixins.
- The only structural change is the root they extend from (`ComponentBase` instead of `class {}`).
- `FlowComponentBase` / `AppFlowBase` gives a dedicated home to app-level orchestration (instead of overloading modal/controller roles).

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.