---
identity:
  node_id: "doc:wiki/drafts/workflow_expectations.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Prefer small, targeted changes.

## Details

- Prefer small, targeted changes.
- Follow existing module boundaries instead of introducing cross-cutting helpers casually.
- For major workflow changes, update relevant docs and append an entry to `changelog.md`.
- Keep runtime state and heavy payloads on disk; keep graph state thin.
- Do not revive deleted legacy modules just to satisfy old tests unless the task explicitly requires it.

Generated from `raw/docs_postulador_v2/AGENTS.md`.