---
identity:
  node_id: "doc:wiki/drafts/paso_1_que_se_abre_al_entrar_a_una_url_de_job.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md", relation_type: "documents"}
---

Timestamp de referencia:

## Details

Timestamp de referencia:

- `2026-03-30T09:50:31+02:00`

URL inspeccionada:

- `https://www.stepstone.de/stellenangebote--Junior-AI-Application-Engineer-AI-Products-LLM-RAG-m-w-d-Muenchen-Berlin-Reply--13815025-inline.html`

Observaciones iniciales:

- Lo que se abre es la ficha publica de la vacante en StepStone, no el formulario de postulacion.
- La sesion parece estar iniciada, porque en el header aparece `juan`.
- El CTA principal visible es `Ich bin interessiert`.
- En esta vista no aparecen inputs del formulario real de apply.
- No se observan campos de texto ni `input[type='file']` para subir CV.
- Por lo tanto, esta pagina corresponde al job ad / landing previa al apply, no al modal o formulario que necesita el adapter.

Interpretacion de este paso:

- Entrar a la URL del job no basta para obtener el DOM del apply flow.
- El siguiente paso exploratorio natural es activar `Ich bin interessiert` para ver si eso abre el formulario real, un modal intermedio, o redirige a otra ruta.

---

Generated from `raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md`.