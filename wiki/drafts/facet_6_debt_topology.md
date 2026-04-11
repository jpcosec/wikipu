---
identity:
  node_id: "doc:wiki/drafts/facet_6_debt_topology.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.732119"
  compiled_from: "wiki-compiler"
---

**Question:** How is deferred work stored, aged, and promoted? What prevents accumulation?

## Details

**Question:** How is deferred work stored, aged, and promoted? What prevents accumulation?

**Consistent answer (postulador_refactor, postulador_v2, doc_methodology):**

- Deferred work lives in `future_docs/` with: why it's deferred, proposed direction, last-reviewed date.
- Inline `# TODO(future): <description> — see future_docs/<file>.md` at the exact code location.
- 6-month stale threshold: untouched entries must be promoted, deleted, or re-dated.
- When prioritized: promote to `plan_docs/`, delete `future_docs/` entry simultaneously.
- When complete: delete plan, remove inline TODO, update changelog.

**What prevents accumulation:** The 6-month rule + the fact that plans are automatically deleted on completion. There is no "archive" state. Resolved = deleted from the repo. History lives in git log and changelog.md.

---

Generated from `raw/methodology_synthesis.md`.