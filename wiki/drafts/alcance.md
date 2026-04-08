---
identity:
  node_id: "doc:wiki/drafts/alcance.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

### Track 1: UI minimal

## Details

### Track 1: UI minimal

- reusar y terminar el `NodeEditor` ya existente como superficie HITL principal
- inspeccion por etapa del pipeline
- editor JSON-backed para `extract_understand`
- editor JSON-backed para `match`
- edicion final de documentos de `generate_documents`
- navegacion coherente desde la pagina del job
- lista completa y concreta de superficies UI involucradas

### Track 2: AI minimal

- `extract_understand` con `ChatGoogleGenerativeAI`
- `with_structured_output()` contra schema estricto
- conexion de LangSmith para trazabilidad de etapas y prompts
- `contact_info` fiable
- `salary_grade` opcional y nunca fatal
- eliminacion de offsets LLM

### Track 3: Scrapper minimal

- `PlaywrightFetcher` con `try/except`
- guardado de `error_screenshot.png`
- uso de `bot_profile` persistente
- cascada HTTP -> Playwright -> LLM fallback como ruta necesaria
- visibilidad clara en UI/API de como se hizo cada scraping y si esta funcionando

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.