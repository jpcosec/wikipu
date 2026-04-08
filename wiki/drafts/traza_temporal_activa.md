---
identity:
  node_id: "doc:wiki/drafts/traza_temporal_activa.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md", relation_type: "documents"}
---

### Evento T0 - Reingreso controlado a la job ad

## Details

### Evento T0 - Reingreso controlado a la job ad

Timestamp:

- `2026-03-30T09:50:31+02:00`

Estado observado:

- URL: `https://www.stepstone.de/stellenangebote--Junior-AI-Application-Engineer-AI-Products-LLM-RAG-m-w-d-Muenchen-Berlin-Reply--13815025-inline.html`
- Titulo: `(Junior) AI Application Engineer || AI Products LLM & RAG (m/w/d) - Job bei der Firma Reply in München, Berlin`
- CTA visible en texto: `Ich bin interessiert`
- Sesion visible en header: `juan`

Interpretacion:

- Estamos nuevamente en la ficha publica del job.
- Aun no hay evidencia del formulario real de apply en el DOM visible.
- El siguiente intento debe registrar la transicion completa y no solo el resultado final.

### Evento T1 - Click sobre contenedor visible del CTA

Timestamp inicio:

- `2026-03-30T09:51:15+02:00`

Accion:

- Click sobre `div.job-ad-display-upetvv`
- Motivo: era el contenedor visible mas claro asociado al texto `Ich bin interessiert` en el bloque principal del job ad

Timestamp observacion posterior:

- `2026-03-30T09:51:27+02:00`

Estado posterior:

- URL: `https://www.stepstone.de/stellenangebote--Junior-AI-Application-Engineer-AI-Products-LLM-RAG-m-w-d-Muenchen-Berlin-Reply--13815025-inline.html`
- Titulo: sin cambio aparente; se mantiene la job ad de Reply
- CTA visible: `Ich bin interessiert`
- No aparecen `Lebenslauf`, `CV`, `E-Mail`, `Telefon`, `Anschreiben`, `Bewerben` ni otros indicios de formulario real
- No hay evidencia de modal ni de redirect

Interpretacion:

- El nodo clickeado pertenece al area visual correcta del CTA, pero no parece ser el elemento interactivo final.
- Es probable que `div.job-ad-display-upetvv` sea un contenedor/wrapper y que el target real sea un hijo mas especifico.
- Esta prueba confirma que incluso un selector visualmente razonable todavia puede ser insuficiente para abrir el flujo.

Estado actual:

- Confirmado: el contenedor visible del CTA no abre el apply.
- Siguiente paso: identificar el elemento clickable interno exacto dentro del bloque `Ich bin interessiert`.

### Evento T2 - Habilitacion de captura de video de escritorio

Timestamp cierre:

- `2026-03-30T09:58:34+02:00`

Verificacion tecnica:

- Sesion grafica detectada: `X11`
- Display detectado: `:1`
- Resolucion detectada: `1920x1080`
- `ffmpeg` quedo disponible en el sistema

Accion realizada:

- Se grabo una captura de escritorio de 30 segundos para validar que el enfoque de screencast funciona para esta exploracion.

Artefacto generado:

- `bitacora_apply/stepstone-session-30s.mkv`

Resultado:

- La grabacion se genero correctamente.
- Tamano del archivo: aproximadamente `4.3M`.

Interpretacion:

- Ya no dependemos solo de snapshots y observaciones manuales.
- Cuando haya transiciones fugaces o estados intermedios dudosos, se puede complementar la bitacora con video real del escritorio.
- Esto mejora bastante la trazabilidad temporal del flujo `autoapply`.

Generated from `raw/docs_postulador_refactor/bitacora_apply/stepstone_apply_exploration.md`.