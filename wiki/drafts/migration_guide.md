---
identity:
  node_id: "doc:wiki/drafts/migration_guide.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/README.md", relation_type: "documents"}
---

### From dev branch

## Details

### From dev branch

Cada spec tiene una sección **Migration Notes** que indica:
- Legacy source path en branch `dev`
- Legacy components a extraer
- Hook de API a usar

### Steps

1. Leer spec completo
2. Revisar legacy source en branch `dev`
3. Extraer shape de JSON de fixtures en `mock/fixtures/`
4. Crear componentes en `features/<feature>/`
5. Conectar via hooks de React Query
6. Aplicar estética Terran Command
7. Seguir anti-patrones de `component_templates.md`

Generated from `raw/docs_postulador_ui/plan/01_ui/README.md`.