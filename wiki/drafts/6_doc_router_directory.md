---
identity:
  node_id: "doc:wiki/drafts/6_doc_router_directory.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

Generated data stored locally:

## Details

Generated data stored locally:

| Path | Purpose | Git |
|------|---------|-----|
| `.doc-router/cache.json` | Scanned graph cache | `.gitignore` |
| `.doc-router/hashes.json` | Content hashes for drift detection | Commit (shared state) |
| `.doc-router/corrections/` | Correction history | Commit (team learning) |
| `.doc-router/history/` | Drift report snapshots over time | Optional |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.