---
identity:
  node_id: "doc:wiki/drafts/librerias_y_templates_a_usar.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

### Backend / pipeline

## Details

### Backend / pipeline

- FastAPI para endpoints de lectura y escritura directa.
- Pydantic para contratos y validacion.
- `WorkspaceManager` y `ArtifactWriter` para acceso seguro a artefactos locales.

### AI

- `langchain-google-genai`
- `langchain-core`
- `langsmith`
- `ChatPromptTemplate`
- `ChatGoogleGenerativeAI`
- `.with_structured_output()`

### Frontend

- React
- `NodeEditor` existente como base de la UI HITL
- fetch API existente en `apps/review-workbench/src/api/client.ts`

### Prompts y templates

- mantener `system.md`
- mantener `user_template.md`
- envolver prompts existentes, no duplicarlos ni reescribir la disciplina de prompts

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.