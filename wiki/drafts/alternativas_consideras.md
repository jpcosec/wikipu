---
identity:
  node_id: "doc:wiki/drafts/alternativas_consideras.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

1. **No extraer, solo documentar**: Mantener todo en PhD2, documentar que son reutilizables

## Details

1. **No extraer, solo documentar**: Mantener todo en PhD2, documentar que son reutilizables
   - *Rechazado*: El usuario específicamente pidió crear una library separada

2. **Git worktree**: Crear un git worktree del repo
   - *Rechazado*: No tiene sentido para una library Python; los git worktrees son para trabajo paralelo en el mismo repo

3. **Monorepo style**: Crear workspace con PhD2 y determinista como packages separados
   - *Considerar*: Más complejo pero podría ser valioso a largo plazo
   - *Decisión*: Mantener como packages independientes por ahora

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.