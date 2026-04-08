---
identity:
  node_id: "doc:wiki/drafts/types_and_data_modeling.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Add type hints everywhere practical.

## Details

- Add type hints everywhere practical.
- Prefer precise built-in generics like `list[str]`, `dict[str, Any]`, and `tuple[str, str]`.
- Use `TypedDict` for graph state and lightweight dictionaries.
- Use Pydantic models for external contracts, structured LLM outputs, persisted review payloads, and artifact schemas.
- Add meaningful `Field(description=...)` text on Pydantic fields, especially when the schema is consumed by an LLM.
- Prefer explicit return types on public functions.

Generated from `raw/docs_postulador_v2/AGENTS.md`.