---
identity:
  node_id: "doc:wiki/drafts/formatting_and_file_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/AGENTS.md", relation_type: "documents"}
---

- Use ASCII by default unless the target file already uses Unicode or Unicode is clearly needed.

## Details

- Use ASCII by default unless the target file already uses Unicode or Unicode is clearly needed.
- Add a short module docstring at the top of each file describing its role.
- Every public function, method, and class should have a structured docstring.
- Prefer short functions with one responsibility.
- If a function accumulates too much state or too many local variables, consider extracting helpers or introducing a class.
- Avoid comments unless they clarify a non-obvious invariant or workflow detail.

Generated from `raw/docs_postulador_v2/AGENTS.md`.