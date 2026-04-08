---
identity:
  node_id: "doc:wiki/drafts/graph_changes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

| action | target | comment |

## Details

| action | target | comment |
|--------|--------|---------|
| add_touch | src/core/io/artifact_writer.py | also needs update for new schema |
| remove_touch | tests/old_test.py | superseded by new test file |
| add_dependency | policy-methodology | plan must comply with this policy |
```

### Parsing Strategy

The structured data (file tags, graph changes) lives in YAML frontmatter as arrays, not as markdown tables in the body. The tables shown above are the **rendered** view in the UI. The actual storage format:

```yaml
---
# ... other frontmatter fields ...
file_tags:
  - file: src/nodes/extract/logic.py:run_logic
    lines: [45, 52]
    comment: needs edge case handling for empty input
  - file: src/nodes/extract/logic.py
    lines: [80, 85]
    comment: "refactor: extract into helper"
graph_changes:
  - action: add_touch
    target: src/core/io/artifact_writer.py
    comment: also needs update for new schema
  - action: remove_touch
    target: tests/old_test.py
    comment: superseded by new test file
---

# Plan Content (edited inline)

The full plan markdown, with user modifications...
```

This keeps structured data machine-parseable (YAML) and free-form content human-editable (markdown body). No fragile table parsing needed.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.