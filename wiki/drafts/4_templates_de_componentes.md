---
identity:
  node_id: "doc:wiki/drafts/4_templates_de_componentes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

Seguir ESTRICTAMENTE los templates en plan/01_ui/proposals/component_templates.md:

## Details

Seguir ESTRICTAMENTE los templates en plan/01_ui/proposals/component_templates.md:
- Átomo: forwardRef + cn() + variants dict + ...props
- Molécula: dumb component + props interface exportada
- Organismo: estado UI local permitido, early returns para loading/empty
- Layout/Shell: sin lógica de negocio, solo grid/flexbox + Outlet o children

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.