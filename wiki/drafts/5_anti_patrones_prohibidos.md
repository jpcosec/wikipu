---
identity:
  node_id: "doc:wiki/drafts/5_anti_patrones_prohibidos.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

1. NO uses useState para estado del servidor. Todo GET/PUT pasa por React Query.

## Details

1. NO uses useState para estado del servidor. Todo GET/PUT pasa por React Query.
2. NO escribas lógica de negocio en pages/. Solo useParams + importar de features/.
3. NO escribas CSS inline (style={{...}}) ni archivos .css nuevos.
4. NO inventes librerías. Iconos: lucide-react. Colores: tokens del tema (text-primary, bg-surface, etc.).
5. NO uses clases Tailwind hardcodeadas sin cn() si el componente acepta className externo.

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.