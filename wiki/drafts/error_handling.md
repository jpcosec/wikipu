---
identity:
  node_id: "doc:wiki/drafts/error_handling.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Fail closed; do not silently convert failure into success.

## Details

- Fail closed; do not silently convert failure into success.
- Prefer domain-specific exceptions over bare `Exception` for control flow.
- If you catch a broad exception for a fallback, log it first and re-raise with `from exc` when appropriate.
- Preserve stack traces.
- Validate required inputs early and raise fast when missing.
- Treat missing review payloads or interrupted HITL resumes as explicit states, not undefined behavior.

Generated from `raw/docs_postulador_v2/AGENTS.md`.