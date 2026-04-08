---
identity:
  node_id: "doc:wiki/drafts/paso_2_primer_intento_de_click_en_ich_bin_interessiert.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md", relation_type: "documents"}
---

Accion realizada:

## Details

Accion realizada:

- Se ejecuto un click automatizado sobre un boton visible en la pagina, intentando activar el CTA `Ich bin interessiert`.

Resultado observado:

- No se abrio un modal de postulacion.
- No aparecio un formulario con campos de apply.
- No aparecieron inputs de texto ni `input[type='file']`.
- La navegacion termino en `https://www.stepstone.de/jobs?searchOrigin=jobad`.
- La vista resultante fue un listado general de resultados/jobs, no la continuacion del flujo de candidatura.

Problema de registro detectado:

- No quedo capturada con suficiente precision la posible transicion intermedia entre el click y el estado final en `/jobs?searchOrigin=jobad`.
- Esto obliga a repetir el flujo con trazabilidad temporal mas fina.

Interpretacion de este paso:

- Un click ingenuo por tipo de elemento/indice no es suficiente para seguir el apply flow.
- En la pagina del job hay mas de un boton y al menos uno de ellos redirige al buscador/listado en vez de abrir candidatura.
- Necesitamos identificar con mas precision cual es el elemento correcto asociado al CTA de apply y no cualquier boton visible.

Aprendizaje util para `autoapply`:

- Un selector demasiado generico para el CTA inicial puede romper el flujo y sacar al usuario del contexto de la vacante.
- El adapter de StepStone no deberia apoyarse en selectores fragiles por posicion (`button` + indice), sino en un contrato mas especifico del bloque del job ad.

Generated from `raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md`.