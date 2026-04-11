---
identity:
  node_id: "doc:wiki/drafts/where_it_fits.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/socratic_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/socratic_protocol.md"
  source_hash: "1ecd4801eb5667e7d2265db07683a47f662dafe281c76a92522cdfe19f2a5a99"
  compiled_at: "2026-04-10T17:47:33.733842"
  compiled_from: "wiki-compiler"
---

```

## Details

```
raw/          →  [ingest]  →  wiki/
                                 ↓
                         Socratic Protocol    ←— runs here, before any plan is created
                                 ↓
                         desk/socratic/Board.md   (open questions, pending human resolution)
                                 ↓
                         desk/issues/ or proposals/   (resolved → actionable)
```

Socratic runs before `desk/issues/` — it is the step that validates a design before it becomes a plan.

---

Generated from `raw/socratic_protocol.md`.