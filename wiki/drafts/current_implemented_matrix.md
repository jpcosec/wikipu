---
identity:
  node_id: "doc:wiki/drafts/current_implemented_matrix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/node_io_matrix.md", relation_type: "documents"}
---

Current operational graph helper is `create_prep_match_app()` in `src/graph.py`:

## Details

Current operational graph helper is `create_prep_match_app()` in `src/graph.py`:

`scrape -> translate_if_needed -> extract_understand -> match -> review_match -> generate_documents -> render -> package`

with `review_match.approve -> generate_documents`.

| Node | Execution Class | Required Inputs (current code) | Outputs (current code) | Review Gate | Downstream Consumers | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `scrape` | `NLLM-ND` | `state.source_url` | GraphState: `ingested_data`; Data Plane: canonical scrape artifacts under `nodes/scrape/` plus `raw/source_text.md` | No | `translate_if_needed` | Uses the core scraping facade and persists JSON-first scrape artifacts. |
| `translate_if_needed` | `NLLM-ND` | `state.ingested_data.raw_text`, optional `state.target_language` | GraphState: updated `ingested_data`; Data Plane: `nodes/translate_if_needed/approved/state.json` | No | `extract_understand` | State and approved artifact flow are both active. |
| `extract_understand` | `LLM` | `state.job_id`, `state.ingested_data.raw_text`, optional `state.active_feedback` | GraphState: `extracted_data`; Data Plane: `nodes/extract_understand/approved/state.json` | No | `match` | Produces structured job understanding. |
| `match` | `LLM` | `state.job_id`, `state.extracted_data.requirements`, `state.my_profile_evidence`; optional regeneration context | GraphState: `matched_data`; Data Plane: `nodes/match/approved/state.json`, `nodes/match/review/decision.md`, `nodes/match/review/rounds/round_<NNN>/decision.md` | Yes (`review_match`) | `review_match` | Uses `RoundManager`; regeneration requires actionable patch feedback. |
| `review_match` | `NLLM-D` | `state.source`, `state.job_id`, `state.matched_data`, `nodes/match/review/decision.md` | GraphState: `review_decision`, `last_decision`, `active_feedback`, `artifact_refs`; Data Plane: `nodes/match/review/decision.json`, `rounds/round_<NNN>/decision.json`, `rounds/round_<NNN>/feedback.json` | Decision parser | `match` (regen), `generate_documents` (approve), `END` (reject) | Enforces stale-hash lock and writes machine-readable review outputs on resume. |
| `generate_documents` | `LLM` + deterministic rendering | `state.matched_data`, latest match decision (`state.last_decision` or `nodes/match/review/decision.json`), profile base data | Data Plane: `nodes/generate_documents/approved/state.json`, `nodes/generate_documents/proposed/*.md`, `nodes/generate_documents/assist/proposed/{state.json,view.md}`; GraphState: `document_deltas`, `text_review_indicators` | No | `render` | Produces CV/letter/email draft markdown and deterministic text-review indicators after approved matching. |
| `render` | `NLLM-D` | `nodes/generate_documents/proposed/{cv,motivation_letter,application_email}.md` | Data Plane: `nodes/render/proposed/*.md`, `nodes/render/approved/state.json`; GraphState: `rendered_documents` | No | `package` | Current render step is markdown-copy plus hash-recording, not PDF/DOCX generation. |
| `package` | `NLLM-D` | `nodes/render/approved/state.json`, `nodes/render/proposed/*.md` | Data Plane: `final/{cv,motivation_letter,application_email}.md`, `final/manifest.json`, `nodes/package/approved/state.json`; GraphState: `status=completed`, `package_manifest_ref` | No | End | Validates render hashes before writing final artifacts. |

Generated from `raw/docs_postulador_langgraph/docs/runtime/node_io_matrix.md`.