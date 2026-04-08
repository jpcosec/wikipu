# Bitacora Apply - Exploracion StepStone

Fecha: 2026-03-30

## Objetivo

Registrar paso a paso el camino real de exploracion del flujo `autoapply` para entender que pagina/modal aparece en cada etapa y poder cerrar el plan original con evidencia concreta.

## Criterio de registro temporal

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

## Nota de conversacion

Durante la exploracion se acuerdo explicitamente que:

- habia una pagina intermedia que no estaba quedando bien registrada
- era importante registrar las transiciones en el tiempo, no solo comentarios generales
- esta instruccion tambien debia quedar anotada en la propia bitacora
- se habilito ademas la opcion de grabar pantalla con `ffmpeg` para capturar secuencias completas cuando las transiciones sean demasiado rapidas o ambiguas para una bitacora basada solo en snapshots

---

## Paso 1 - Que se abre al entrar a una URL de job

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

## Estado actual

- Confirmado: la URL guardada en jobs permite llegar a la ficha del empleo.
- Pendiente: descubrir si `Ich bin interessiert` lleva al formulario real reutilizable para fixture/selectors.

---

## Paso 2 - Primer intento de click en `Ich bin interessiert`

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

## Estado actual

- Confirmado: el primer intento de click no sirve para abrir el apply.
- Siguiente paso: volver a la job ad e identificar el CTA correcto con mayor precision antes de hacer otro click.

---

## Traza temporal activa

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
