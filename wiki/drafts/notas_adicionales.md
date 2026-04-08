---
identity:
  node_id: "doc:wiki/drafts/notas_adicionales.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

- La library no debe modificar `core/` durante ejecución (constraint de Pulpo)

## Details

- La library no debe modificar `core/` durante ejecución (constraint de Pulpo)
- `package` depende de `render.contract.RenderStateEnvelope` — debe mantenerse sincronizado
- `translate_if_needed` usa `deep-translator` que debe ser dependency opcional o lazy-imported

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.