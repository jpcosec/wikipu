---
identity:
  node_id: "doc:wiki/drafts/restricciones_no_negociables.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

1. Cero Neo4j como formato de trabajo actual.

## Details

1. Cero Neo4j como formato de trabajo actual.
2. La fuente de verdad es `data/jobs/`.
3. El backend solo expone read/write directo sobre artefactos locales.
4. LangChain se usa solo en la capa LLM, no para reescribir la orquestacion.
5. Los TextSpans deben resolverse por matching determinista, nunca por offsets inventados por el LLM.
6. Si falta una libreria necesaria para cerrar el minimal, se instala en esta fase.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.