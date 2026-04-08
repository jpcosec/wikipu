---
identity:
  node_id: "doc:wiki/drafts/what_is_true_today.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/core_io_and_provenance.md", relation_type: "documents"}
---

- The shared I/O layer exists and is used by current runtime nodes such as `review_match`, `render`, `package`, and the prep-match CLI observability writes.

## Details

- The shared I/O layer exists and is used by current runtime nodes such as `review_match`, `render`, `package`, and the prep-match CLI observability writes.
- Path construction, guarded job-relative resolution, atomic writes, JSON/text helpers, and run/node execution snapshots are implemented.
- The current runtime is still mixed: some older nodes continue to do inline file I/O while newer slices use `src/core/io/`.

Generated from `raw/docs_postulador_langgraph/docs/runtime/core_io_and_provenance.md`.