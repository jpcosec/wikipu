---
identity:
  node_id: "doc:wiki/concepts/the_collection_step.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/trail_collect.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/trail_collect.md"
  source_hash: "b5310580e40950c0da96febcf8d445391a89da95cb9c5c05c5157e3032195588"
  compiled_at: "2026-04-14T16:50:28.665660"
  compiled_from: "wiki-compiler"
---

At natural breakpoints or session end:

## Details

At natural breakpoints or session end:

1. **Scan** the session for the artifact types above.
2. **Classify** each artifact: decision / gap / correction / new concept / rule patch.
3. **Route** each classified artifact to its destination (doc update, new issue, raw seed, hausordnung patch).
4. **Record** a one-line entry in the changelog: what was collected and where it went.

This step should be lightweight. If it takes more than a few minutes, it is doing too much — the valuable artifacts should be obvious.

---

Generated from `raw/trail_collect.md`.