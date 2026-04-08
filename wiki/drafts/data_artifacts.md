---
identity:
  node_id: "doc:wiki/drafts/data_artifacts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md", relation_type: "documents"}
---

### Input Artifacts

## Details

### Input Artifacts

| Path | Consumed By | Meaning |
|------|-------------|---------|
| `raw/source_text.md` | `extract_understand` | Human-readable source text |
| `nodes/scrape/approved/canonical_scrape.json` | `extract_understand` | Canonical scrape envelope |
| `nodes/extract_understand/approved/state.json` | `match` | Structured requirements |
| `nodes/match/approved/state.json` | `review_match` | Match proposal |
| `nodes/match/review/decision.md` | `review_match` | Human review surface |

### Output Artifacts

| Path | Produced By | Meaning |
|------|-------------|---------|
| `nodes/scrape/input/fetch_metadata.json` | `scrape` | Fetch metadata |
| `nodes/scrape/input/raw_snapshot.json` | `scrape` | Raw snapshot |
| `nodes/scrape/input/source_extraction.json` | `scrape` | Extracted content |
| `nodes/scrape/approved/canonical_scrape.json` | `scrape` | Canonical scrape |
| `nodes/translate_if_needed/approved/state.json` | `translate_if_needed` | Translation state |
| `nodes/extract_understand/approved/state.json` | `extract_understand` | Requirements extraction |
| `nodes/match/approved/state.json` | `match` | Match proposal |
| `nodes/match/review/decision.md` | `match` | Review surface |
| `nodes/match/review/decision.json` | `review_match` | Parsed decision |
| `nodes/match/review/rounds/round_<NNN>/` | `match` | Per-round artifacts |
| `nodes/generate_documents/proposed/cv.md` | `generate_documents` | CV draft |
| `nodes/generate_documents/proposed/motivation_letter.md` | `generate_documents` | Letter draft |
| `nodes/generate_documents/proposed/application_email.md` | `generate_documents` | Email draft |
| `nodes/render/proposed/*.md` | `render` | Rendered copies |
| `nodes/render/approved/state.json` | `render` | Render state |
| `final/*.md` | `package` | Final deliverables |
| `final/manifest.json` | `package` | Artifact manifest |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md`.