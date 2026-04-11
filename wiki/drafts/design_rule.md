---
identity:
  node_id: "doc:wiki/drafts/design_rule.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/facets_as_questions.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/facets_as_questions.md"
  source_hash: "1159abdd773043bbfb19f64dd1bb2058bf81d60b78a5f5954777a51ee89cc0ed"
  compiled_at: "2026-04-10T17:47:33.730974"
  compiled_from: "wiki-compiler"
---

**Every facet must declare its question explicitly.**

## Details

**Every facet must declare its question explicitly.**
No facet should be added to contracts.py without a one-sentence question
that defines what it answers. This question is the facet's contract —
it governs what data belongs in it, how the injector populates it,
and what the auditor checks against it.

Generated from `raw/facets_as_questions.md`.