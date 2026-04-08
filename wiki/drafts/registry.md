---
identity:
  node_id: "doc:wiki/drafts/registry.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md", relation_type: "documents"}
---

### Job Data (per application)

## Details

### Job Data (per application)

| Data Type | Canonical Path | Notes |
|-----------|---------------|-------|
| Raw source text | `data/jobs/<source>/<job_id>/raw/source_text.md` | From scrape |
| Screenshots | `data/jobs/<source>/<job_id>/raw/` | `*.png`, `*.jpg` |
| Translated text | `data/jobs/<source>/<job_id>/translated/source_text.md` | Optional |
| **Extract state** | `data/jobs/<source>/<job_id>/nodes/extract/state.json` | Text Tagger output |
| **Match state** | `data/jobs/<source>/<job_id>/nodes/match/state.json` | Evidence links |
| **Strategy Delta** | `data/jobs/<source>/<job_id>/nodes/strategy/delta.json` | Document deltas |
| **Drafting docs** | `data/jobs/<source>/<job_id>/nodes/drafting/` | `cv.md`, `cover_letter.md`, `email.md` |
| Review nodes | `data/jobs/<source>/<job_id>/nodes/review/` | Generic review JSONs |
| Feedback | `data/jobs/<source>/<job_id>/feedback/` | Legacy feedback (deprecated) |
| Final output | `data/jobs/<source>/<job_id>/final/` | PDFs, ZIPs |

### Candidate Data (global)

| Data Type | Canonical Path | Notes |
|-----------|---------------|-------|
| CV Profile | `data/master/profile.json` | Structured knowledge graph |
| Evidence Bank | `data/master/evidence/` | Validated proofs |
| Master Templates | `data/master/templates/` | `master_cv.md`, `master_cover_letter.md`, `master_email.md` |
| Learned Filters | `data/master/filters/` | REJECTION rules learned |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md`.