---
identity:
  node_id: "doc:wiki/drafts/contexto.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

PhD 2.0 se esta reorientando desde una vision mas pesada y futura hacia una arquitectura minima viable que permita dos cosas cuanto antes:

## Details

PhD 2.0 se esta reorientando desde una vision mas pesada y futura hacia una arquitectura minima viable que permita dos cosas cuanto antes:

1. estabilizar el pipeline LLM
2. hacer review humana rapida sobre artefactos locales reales

La prioridad no es Neo4j ni una UI final de conocimiento global. La prioridad es trabajar sobre los JSON reales que ya viven en `data/jobs/<source>/<job_id>/` y cerrar un flujo util de inspeccion, correccion y guardado para las etapas que hoy importan.

Las fuentes de verdad para este plan son:

- `plan/01_ui/fase1_minimal_json_editor.md`
- `plan/02_langchain/fase1_llm_wrappers_y_structured_output.md`
- `plan/03_scrapper/phase1_scraping_and_autoapply.md`
- `plan/index_checklist.md`

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.