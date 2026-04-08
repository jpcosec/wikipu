---
identity:
  node_id: "doc:wiki/drafts/1_componentbase_common_ground.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Shared contract for all components:

## Details

Shared contract for all components:

- stable ids (`componentId`, `kind`, optional domain ids)
- lifecycle (`start()`, `stop()`, `destroy()`, `isStarted`)
- wiring hooks (`wireScenario()`, `wireActor()`)
- snapshot contract (`toDisplayObject()` abstract)
- cleanup registry for subscriptions/timers

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.