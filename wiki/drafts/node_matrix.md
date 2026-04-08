---
identity:
  node_id: "doc:wiki/drafts/node_matrix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md", relation_type: "documents"}
---

| Node | Execution | Inputs | Outputs | Review Gate | Downstream |

## Details

| Node | Execution | Inputs | Outputs | Review Gate | Downstream |
|------|-----------|--------|---------|-------------|------------|
| `scrape` | NLLM-ND | `state.source_url` | `state.ingested_data` + `nodes/scrape/` | No | `translate_if_needed` |
| `translate_if_needed` | NLLM-ND | `state.ingested_data.raw_text` | `nodes/translate_if_needed/approved/state.json` | No | `extract_understand` |
| `extract_understand` | LLM | `state.ingested_data`, `state.active_feedback` | `nodes/extract_understand/approved/state.json` | No | `match` |
| `match` | LLM | `state.extracted_data`, `state.my_profile_evidence` | `nodes/match/approved/state.json` | **Yes** (`review_match`) | `review_match` |
| `review_match` | NLLM-D | `nodes/match/review/decision.md` | `decision.json`, routes flow | Decision parser | `match`, `generate_documents`, END |
| `generate_documents` | LLM + D | `state.matched_data`, `state.last_decision` | `nodes/generate_documents/proposed/*.md` | No | `render` |
| `render` | NLLM-D | `nodes/generate_documents/proposed/*.md` | `nodes/render/proposed/*.md` | No | `package` |
| `package` | NLLM-D | `nodes/render/proposed/*.md` | `final/*.md`, `final/manifest.json` | No | END |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/node_matrix.md`.