---
identity:
  node_id: "doc:wiki/drafts/6_documentation_lifecycle_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

- Update the module README **at the same time** as the code change, not after.

## Details

- Update the module README **at the same time** as the code change, not after.
- When a Pydantic field changes meaning, update its `Field(description=...)` in the same commit.
- When a new fallback or retry mechanism is added, add the corresponding `[🤖]` or `[⚠️]` log line.
- When architectural patterns change, update the Architecture section and its file links.
- Documentation that describes removed behaviour must be deleted, not left as historical comment.

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.