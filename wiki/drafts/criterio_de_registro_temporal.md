---
identity:
  node_id: "doc:wiki/drafts/criterio_de_registro_temporal.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md", relation_type: "documents"}
---

Desde este punto la bitacora pasa a registrar los eventos como una secuencia temporal y no solo como notas estaticas, porque el sitio puede cambiar entre estados intermedios, redirects, overlays o pantallas transitorias.

## Details

Desde este punto la bitacora pasa a registrar los eventos como una secuencia temporal y no solo como notas estaticas, porque el sitio puede cambiar entre estados intermedios, redirects, overlays o pantallas transitorias.

Para cada accion importante se intenta registrar:

- timestamp
- URL observada
- titulo de la pagina cuando sea visible
- texto dominante o CTA visibles
- interpretacion del estado
- transiciones intermedias detectadas

Nota operativa:

- Si una accion gatilla varias transiciones, no basta con registrar el estado final.
- El objetivo es dejar una foto en el tiempo de cada paso del flujo, incluyendo estados intermedios si aparecen.

Generated from `raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md`.