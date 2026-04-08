---
identity:
  node_id: "doc:wiki/drafts/3_scenario_context_layer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Introduce a scenario owner class (e.g., `ScenarioContext`):

## Details

Introduce a scenario owner class (e.g., `ScenarioContext`):

- owns environment/session inputs (`paxGlobal`, `dia`, `hora`, etc.)
- applies patch updates
- broadcasts context changes to root container components
- can switch scenario profiles (browse, basket, validation) without rewriting components

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.