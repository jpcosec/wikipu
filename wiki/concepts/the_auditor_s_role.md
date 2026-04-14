---
identity:
  node_id: "doc:wiki/concepts/the_auditor_s_role.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/facets_as_questions.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/facets_as_questions.md"
  source_hash: "1159abdd773043bbfb19f64dd1bb2058bf81d60b78a5f5954777a51ee89cc0ed"
  compiled_at: "2026-04-14T16:50:28.659680"
  compiled_from: "wiki-compiler"
---

The auditor is the inverse of the facet question:

## Details

The auditor is the inverse of the facet question:

> For each question, which nodes can't answer it when they should be able to?

A `file:` node that can't answer "what does this do?" → missing docstring.
A `file:` node that can't answer "what data does it produce?" → untyped I/O.
A `code:` node that can't answer "how is it tested?" → no test coverage.

---

Generated from `raw/facets_as_questions.md`.