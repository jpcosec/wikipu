---
identity:
  node_id: "doc:wiki/drafts/riesgos_y_decisiones_explicitas.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

### Riesgo 1

## Details

### Riesgo 1

El editor puede quedarse demasiado centrado en JSON crudo.

Decision:

- reusar el `NodeEditor` real en vez de crear otra UI
- cerrar utilidad real sobre JSON local
- luego reducir friccion con affordances guiadas para campos clave

### Riesgo 2

LangChain puede introducir nueva fragilidad si se expande demasiado pronto o sin observabilidad.

Decision:

- limitar la fase actual a `extract_understand`
- conectar LangSmith desde el inicio
- evaluar `match` despues de estabilizar extraccion

### Riesgo 3

El scraping puede crecer demasiado por auto-apply.

Decision:

- priorizar robustez y trazabilidad
- dejar auto-apply fuera del cierre del minimal si amenaza foco o tiempo
- no dejar fuera la visibilidad del modo de scraping y del fallback, porque eso si es parte del minimal

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.