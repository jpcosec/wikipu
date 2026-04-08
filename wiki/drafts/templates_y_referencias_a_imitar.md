---
identity:
  node_id: "doc:wiki/drafts/templates_y_referencias_a_imitar.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

1. `apps/review-workbench/src/pages/JobStagePage.tsx` como centro de navegacion por job.

## Details

1. `apps/review-workbench/src/pages/JobStagePage.tsx` como centro de navegacion por job.
2. `apps/review-workbench/src/api/client.ts` como patron de cliente simple hacia FastAPI.
3. `src/interfaces/api/routers/jobs.py` como router principal de surfaces del job.
4. `src/interfaces/api/read_models.py` como capa de lectura/adaptacion de artefactos locales.
5. `src/nodes/extract_understand/prompt/system.md` y `src/nodes/extract_understand/prompt/user_template.md` como disciplina de prompts a preservar.
6. `apps/review-workbench/src/sandbox/pages/NodeEditorSandboxPage.tsx` como base funcional del editor, no como referencia descartable.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.