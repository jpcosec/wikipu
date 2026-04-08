---
identity:
  node_id: "doc:wiki/drafts/priority_5_improve_review_validation_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

Some validation lives directly in graph node logic.

That is fine for now, but the validation path could become cleaner.

### Recommended Change

Introduce a small validation service or helper for review application, for example:

- `validate_review_payload(payload, expected_hash)`

This keeps graph nodes orchestration-focused rather than validation-heavy.

### Suggested Steps

1. extract payload + hash validation from `apply_review_decision`
2. centralize row-to-feedback conversion logic
3. keep `apply_review_decision` focused on persistence + routing

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.