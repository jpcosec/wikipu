---
identity:
  node_id: "doc:wiki/drafts/matrix_schema.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md", relation_type: "documents"}
---

Each entry contains:

## Details

Each entry contains:

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string | Technical domain (ui, api, pipeline, core, data, policy, practices) |
| `stage` | string | Pipeline stage (scrape, extract, match, strategy, drafting, render, package) or "all" for cross-cutting |
| `nature` | string | philosophy, implementation, development, testing, expected_behavior, **migration** |
| `doc_path` | string | Exact path to Markdown documentation |
| `target_code` | string[] | Glob patterns for source code (e.g., `["src/**/*.py"]`) |
| `keywords` | string[] | Triggers that route queries here |
| `description` | string | What this document contains |
| `not_contains` | string | What NOT to look for here + where to go |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md`.