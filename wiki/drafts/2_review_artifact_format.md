---
identity:
  node_id: "doc:wiki/drafts/2_review_artifact_format.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

The `review_{group}_N.md` is a single file containing all review output: inline edits to the plan text, file span tags, and graph edit comments.

## Details

The `review_{group}_N.md` is a single file containing all review output: inline edits to the plan text, file span tags, and graph edit comments.

```markdown
---
id: review-{group}-{version}
type: review
group: {group}
version: {version}
parent: plan-{group}-{version}
status: active
touches:
  - path: src/nodes/extract/logic.py
    symbol: run_logic
  - path: docs/runtime/node_io_matrix.md
---

# Plan Content (edited inline)

The full plan markdown, with user modifications...

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.