---
identity:
  node_id: "doc:wiki/drafts/plan_de_trabajo.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

### Step 0 - Cerrar inventario y spec minima de UI

## Details

### Step 0 - Cerrar inventario y spec minima de UI

#### Objetivo

Confirmar que existe una lista completa de las superficies UI del minimal y como se van a ver antes de seguir agregando piezas sueltas.

#### Tareas

1. Enumerar todas las superficies UI involucradas en el minimal.
2. Confirmar cual de ellas reusa `NodeEditor`, cual reusa views existentes y cual necesita solo schema/adaptador nuevo.
3. Confirmar flujos exactos de operador por etapa.
4. Si falta una lista cerrada o un comportamiento no esta claro, detener implementacion y pedirle al usuario la spec faltante.

#### Lista minima que debe quedar cerrada

1. Job page como hub de navegacion.
2. Vista de outputs por stage.
3. `NodeEditor` para `extract_understand`.
4. `NodeEditor` para `match`.
5. Vista/editor de documentos para `generate_documents`.
6. Vista de scraping con modo usado, warnings, artifacts y screenshot si existe.

#### Gate

No seguir implementando UI si esta lista no esta cerrada y comprensible.

Este Step 0 es prerrequisito para todo el track UI.

### Fase A - Cerrar el puente UI <-> JSON local

#### Objetivo

Que cada job tenga una superficie clara para ver y editar los outputs relevantes del pipeline usando solo archivos locales.

#### Tareas

1. Consolidar la vista `Pipeline Outputs` como superficie principal de inspeccion por etapa.
2. Reusar el `NodeEditor` existente para `extract_understand` con affordances mas guiadas para campos clave.
3. Reusar el `NodeEditor` existente para `match` con affordances para score, reasoning y evidence links.
4. Agregar edicion y guardado de documentos de `generate_documents` desde la UI.
5. Mantener compatibilidad con el rumbo futuro: misma navegacion por job y por stage, pero sobre JSON local.

#### Pseudocodigo

```text
GET /jobs/{source}/{job_id}/stage/{stage}/outputs
  -> leer lista conocida de artefactos esperados por stage
  -> devolver solo archivos existentes

GET /jobs/{source}/{job_id}/editor/{node}/state
  -> leer nodes/<node>/approved/state.json

PUT /jobs/{source}/{job_id}/editor/{node}/state
  -> validar payload JSON
  -> sobrescribir state.json de forma atomica

GET /jobs/{source}/{job_id}/documents/{doc_key}
PUT /jobs/{source}/{job_id}/documents/{doc_key}
  -> leer/escribir markdown o JSON final de generate_documents
```

### Fase B - Endurecer `extract_understand`

#### Objetivo

Que la extraccion estructurada sea estable y util en los campos mas sensibles para review humana.

#### Tareas

1. Mantener `ChatGoogleGenerativeAI` y `with_structured_output()` como camino oficial.
2. Endurecer el schema con `contact_info` y `salary_grade: Optional[str]`.
3. Priorizar fiabilidad de PI/contacto y email.
4. Mantener `salary_grade` como null si no existe.
5. Mover TextSpan hacia `exact_quote` + resolucion determinista posterior.
6. Conectar LangSmith para trazabilidad de prompts, respuestas y errores.
7. Agregar casos de prueba con postings reales guardados localmente.
8. Instalar librerias faltantes si el runtime aun no las tiene.

#### Pseudocodigo

```text
run_logic(state)
  -> build prompt from current templates
  -> call ChatGoogleGenerativeAI.with_structured_output(schema)
  -> emit trace to LangSmith
  -> validate result
  -> enrich contact/salary only with deterministic post-processing if needed
  -> persist extracted_data compatible with current downstream consumers
```

### Fase C - Cerrar review determinista de evidencia

#### Objetivo

Que la UI pueda vincular requirement/evidence/source text sin offsets alucinados.

#### Tareas

1. Definir una utilidad comun de busqueda de texto por `exact_quote`.
2. Resolver linea, offset o fragmento visible desde texto fuente real.
3. Reusar esa resolucion en `View 2` y en el editor del job.
4. Mantener compatibilidad con una futura UI mas rica, pero sin depender de ella.

#### Explicacion operativa

Aqui `matching determinista` significa que el enlace entre evidencia y texto fuente se calcula con reglas reproducibles sobre el texto guardado en disco, no con posiciones estimadas por el modelo.

Ejemplos aceptables:

1. busqueda exacta de substring
2. busqueda normalizada ignorando espacios redundantes
3. derivacion de lineas a partir de una coincidencia encontrada

Ejemplos no aceptables:

1. pedirle al LLM `start_offset` y `end_offset`
2. inventar lineas si la cita no aparece
3. guardar spans que no puedan recalcularse desde el texto local

#### Pseudocodigo

```text
resolve_span(source_text, exact_quote)
  -> normalize source_text
  -> normalize exact_quote
  -> find first deterministic match
  -> derive line range and preview snippet
  -> return null if not found, never invent
```

### Fase D - Terminar el scraping minimal

#### Objetivo

Que el scraping sea suficientemente robusto para no dejar ciego al operador cuando una pagina JS falle.

#### Tareas

1. Verificar que `PlaywrightFetcher` siempre capture screenshot en fallo cuando exista job context.
2. Verificar que `bot_profile` persistente sea el default operacional documentado.
3. Endurecer la cascada HTTP -> Playwright -> LLM fallback.
4. Hacer visible en artifacts y UI que modo se uso, que fallo, y que warnings hubo.
5. Mantener artefactos en `nodes/scrape/` y `raw/source_text.md`.
6. Exponer una vista clara para revisar cada scraping y diagnosticar si esta funcionando.

#### Pseudocodigo

```text
scrape_detail(request)
  -> try http fetch
  -> if missing/blocked/failed then try playwright fetch
  -> on playwright exception save error_screenshot.png in trace/
  -> if deterministic extraction still fails escalate to LLM fallback
  -> persist fetch_metadata/raw_snapshot/source_extraction/canonical_scrape
```

### Fase E - Cerrar la experiencia minima de operador

#### Objetivo

Que el operador pueda recorrer el pipeline de un job sin salir de la superficie de trabajo minima.

#### Tareas

1. Desde la job page: ver timeline, elegir stage, inspeccionar outputs.
2. Editar `extract_understand` y `match` desde el editor.
3. Editar documentos finales desde UI.
4. Ver feedback suficiente para saber que se guardo en disco.
5. Mantener comandos CLI solo como complemento, no como unica forma de revisar.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.