---
identity:
  node_id: "doc:wiki/drafts/what_belongs_near_code.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/index/conceptual_tree.md", relation_type: "documents"}
---

Move heavier implementation docs close to the code when they are mainly about:

## Details

Move heavier implementation docs close to the code when they are mainly about:

- module internals
- maintenance notes
- subsystem-specific runtime contracts
- edge cases and implementation tradeoffs
- testing notes for a specific subsystem

Central docs should point to these instead of duplicating them.

Examples:

- `src/core/scraping/README.md`
- `src/core/io/README.md`
- `src/nodes/review_match/README.md`
- `src/nodes/render/README.md`
- `src/nodes/package/README.md`
- `apps/review-workbench/src/sandbox/README.md`

Generated from `raw/docs_postulador_langgraph/docs/index/conceptual_tree.md`.