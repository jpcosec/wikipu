---
identity:
  node_id: "doc:wiki/drafts/2_role_base_classes_capability_bundles.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

- `ItemBase`: actor + pricing + rules + storage + display contract

## Details

- `ItemBase`: actor + pricing + rules + storage + display contract
- `ContainerBase`: actor + child aggregation + rules propagation + storage + display contract
- `ViewBase`: display + event emission
- `UIContainerBase`: view + event + actor bridge
- `ModalControllerBase`: modal state + form state + service injection + events + display

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.