---
identity:
  node_id: "doc:wiki/drafts/7_definition_of_done.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

- La página se renderiza sin errores de consola ni TS.

## Details

- La página se renderiza sin errores de consola ni TS.
- Todos los estados visuales (loading, error, empty, data) están implementados.
- La mutación principal usa useMutation con invalidación de caché (no optimistic a menos que el spec lo pida explícitamente).
- El código está estrictamente dividido entre features/ (lógica y UI) y pages/ (entrypoint).
- Cada componente exporta su interface de Props.

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.