---
identity:
  node_id: "doc:wiki/drafts/aclaracion_clave_que_significa_textspan_determinista.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md", relation_type: "documents"}
---

En esta fase no queremos que el LLM devuelva posiciones exactas dentro del texto, como `start_offset` o `end_offset`, porque esos offsets suelen ser inconsistentes o directamente inventados.

## Details

En esta fase no queremos que el LLM devuelva posiciones exactas dentro del texto, como `start_offset` o `end_offset`, porque esos offsets suelen ser inconsistentes o directamente inventados.

Lo que si aceptamos es que el modelo devuelva una cita verificable, por ejemplo `exact_quote`.

Luego el backend o la UI calculan la posicion real sobre el texto fuente local con reglas reproducibles:

1. leer el texto fuente guardado en disco
2. buscar la cita dentro de ese texto
3. si aparece, derivar lineas, snippet o posicion real
4. si no aparece, devolver `not found` y no inventar un span

Ejemplo:

- el modelo devuelve `exact_quote = "TV-L E13"`
- la UI o backend busca `TV-L E13` en `source_text.md`
- si lo encuentra, usa esa coincidencia real para highlight o linking
- si no lo encuentra, no crea offsets falsos

Esto hace que el linking entre texto fuente y evidencia sea auditable y repetible.

Generated from `raw/docs_postulador_langgraph/plan/minimal_viable_architecture_completion_plan.md`.