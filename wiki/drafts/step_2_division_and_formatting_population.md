---
identity:
  node_id: "doc:wiki/drafts/step_2_division_and_formatting_population.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/MIGRATION_INSTRUCTIONS.md", relation_type: "documents"}
---

Using the extracted information, generate or overwrite the corresponding Markdown files in `docs/runtime/`, `docs/core/`, `docs/api/`, etc.

## Details

Using the extracted information, generate or overwrite the corresponding Markdown files in `docs/runtime/`, `docs/core/`, `docs/api/`, etc.
- Must separate monolithic concepts into orthogonal files based on `11_routing_matrix.md` (e.g., separate UI logic from Pipeline logic).
- For API documentation, follow FastAPI standards.
- For Pipeline, document LangGraph transitions and `state.json` schemas.
- If code is unimplemented but planned, place it in `plan/` folder using `practices/planning_template_backend.md` or `practices/planning_template_ui.md` formats.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/MIGRATION_INSTRUCTIONS.md`.