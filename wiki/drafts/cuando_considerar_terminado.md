---
identity:
  node_id: "doc:wiki/drafts/cuando_considerar_terminado.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

El plan minimal puede considerarse terminado cuando se cumplan todas estas condiciones:

## Details

El plan minimal puede considerarse terminado cuando se cumplan todas estas condiciones:

1. `extract_understand` y `match` se pueden cargar, editar y guardar desde la UI contra JSON local.
2. Los documentos de `generate_documents` se pueden revisar y editar desde la UI.
3. La pagina de job permite inspeccionar outputs de cada etapa relevante.
4. `extract_understand` usa LangChain wrappers sin romper fail-closed ni `src/graph.py`.
5. LangSmith permite seguir al menos las etapas LLM relevantes del pipeline actual.
6. `contact_info` se comporta de forma estable y util para review humana.
7. `salary_grade` es estrictamente opcional: si no aparece o es ambiguo, queda en `null` sin romper el nodo.
8. TextSpan/evidence linking se hace por matching determinista.
9. `PlaywrightFetcher` guarda `error_screenshot.png` y usa `bot_profile` persistente.
10. La cascada HTTP -> Playwright -> LLM fallback es visible y auditable.
11. No se agregaron dependencias nuevas de Neo4j para esta fase.
12. `data/jobs/` sigue siendo la unica fuente de verdad operacional.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.