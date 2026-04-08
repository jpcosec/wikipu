---
identity:
  node_id: "doc:wiki/drafts/modelo_de_error_fail_closed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md", relation_type: "documents"}
---

Todos los nodos deben fallar cerrado — ningún fallback silencioso. Tipos de error en `GraphState.ErrorContext`:

## Details

Todos los nodos deben fallar cerrado — ningún fallback silencioso. Tipos de error en `GraphState.ErrorContext`:

| Código | Causa |
|--------|-------|
| `MODEL_FAILURE` | LLM no retornó schema válido |
| `TOOL_FAILURE` | Scraper o translator falló |
| `IO_FAILURE` | Error de lectura/escritura en disco |
| `INPUT_MISSING` | State key requerido ausente |
| `SCHEMA_INVALID` | Pydantic validation falló |
| `POLICY_VIOLATION` | Violación de regla de negocio |
| `PARSER_REJECTED` | review_decision_service no pudo parsear |
| `REVIEW_LOCK_MISSING` | Hash de review no coincide |
| `INTERNAL_ERROR` | Error inesperado |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_pipeline_reference.md`.