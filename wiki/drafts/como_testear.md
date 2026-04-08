---
identity:
  node_id: "doc:wiki/drafts/como_testear.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

### Backend

## Details

### Backend

- probar endpoints read/write de editor para `extract_understand` y `match`
- probar endpoints de outputs por stage
- verificar escrituras atomicas sobre `state.json`

### Frontend

- abrir un job real
- cambiar de stage
- inspeccionar artefactos
- editar extraccion
- editar match
- editar documentos
- guardar y recargar para verificar persistencia

### AI

- usar fixtures de postings reales con contacto y sin contacto
- usar fixtures con salary grade y sin salary grade
- verificar que null no rompe el nodo
- verificar que `exact_quote` se mantiene y no aparecen offsets generados por el modelo
- verificar que LangSmith recibe trazas de las etapas instrumentadas

### Scraping

- forzar un fallo JS y verificar `trace/error_screenshot.png`
- verificar uso del `bot_profile`
- verificar fallback HTTP -> Playwright -> LLM
- verificar que artefactos quedan bajo `nodes/scrape/` y `raw/source_text.md`
- verificar que el modo usado y warnings quedan visibles en artifacts y UI

### Comandos de verificacion sugeridos

```bash
python -m pytest tests/interfaces/api -q
python -m pytest tests/nodes/extract_understand -q
python -m pytest tests/core/scraping -q
python -m pytest tests/ -q
```

```bash
cd apps/review-workbench && npm run build
```

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.