---
identity:
  node_id: "doc:wiki/drafts/que_no_hacer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

1. No mover persistencia a Neo4j.

## Details

1. No mover persistencia a Neo4j.
2. No redisenar la UI completa antes de cerrar los minimals.
3. No reescribir `src/graph.py` ni el routing LangGraph.
4. No pedir offsets al LLM.
5. No introducir una capa de abstraccion nueva que esconda `data/jobs/`.
6. No convertir esta fase en una migracion full-pipeline a LangChain.
7. No expandir auto-apply hasta que el scraping baseline quede robusto.
8. No crear un editor paralelo si el `NodeEditor` actual ya puede cubrir la necesidad con vistas y schemas nuevos.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.