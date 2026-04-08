---
identity:
  node_id: "doc:wiki/drafts/data_plane_artifacts_currently_written_and_consumed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

All paths below are relative to `data/jobs/<source>/<job_id>/`.

## Details

All paths below are relative to `data/jobs/<source>/<job_id>/`.

| Path | Producer in current codebase | Meaning / usage |
| --- | --- | --- |
| `raw/raw.html` | scrape subsystem / legacy backfills | Raw fetched HTML source for audit/debug. |
| `raw/source_text.md` | scrape subsystem | Human-readable extracted source text. |
| `raw/language_check.json` | translation or legacy scrape utilities | Language detection/translation diagnostics when available. |
| `nodes/scrape/input/fetch_metadata.json` | `src/core/scraping/service.py` | Fetch mode, source URL, and fetch policy metadata. |
| `nodes/scrape/input/raw_snapshot.json` | `src/core/scraping/service.py` | Raw fetch snapshot metadata/content envelope. |
| `nodes/scrape/input/source_extraction.json` | `src/core/scraping/service.py` | Extracted text/structured scrape details before canonical normalization. |
| `nodes/scrape/input/listing_crawl.json` | `src/cli/run_scrape_probe.py` listing mode | Listing crawl results and discovered detail URLs for operator inspection. |
| `nodes/scrape/approved/canonical_scrape.json` | `src/core/scraping/service.py` | Canonical scrape envelope used by downstream scrape node compatibility logic. |
| `nodes/translate_if_needed/approved/state.json` | `src/nodes/translate_if_needed/logic.py` | Scrape payload plus translation flags (`translated`, `translated_to`). |
| `nodes/extract_understand/approved/state.json` | `src/nodes/extract_understand/logic.py` | Structured job understanding (`requirements`, `constraints`, `risk_areas`). |
| `nodes/match/approved/state.json` | `src/nodes/match/logic.py` | Canonical persisted match envelope (`matches`, `total_score`, recommendation, notes). |
| `nodes/match/review/decision.md` | `src/nodes/match/logic.py` and `src/nodes/review_match/logic.py` | Human review surface for checkbox decisions. |
| `nodes/match/review/decision.json` | `src/nodes/review_match/logic.py` | Parsed machine decision envelope used for routing and traceability. |
| `nodes/match/review/rounds/round_<NNN>/decision.md` | `src/nodes/match/logic.py` / `RoundManager` | Immutable per-round review surface snapshots. |
| `nodes/match/review/rounds/round_<NNN>/decision.json` | `src/nodes/review_match/logic.py` | Immutable per-round parsed decision snapshot. |
| `nodes/match/review/rounds/round_<NNN>/feedback.json` | `src/nodes/review_match/logic.py` | Regeneration feedback payload, including optional `patch_evidence`. |
| `nodes/generate_documents/approved/state.json` | `src/nodes/generate_documents/logic.py` | LLM-generated document deltas. |
| `nodes/generate_documents/proposed/cv.md` | `src/nodes/generate_documents/logic.py` | Generated CV markdown draft. |
| `nodes/generate_documents/proposed/motivation_letter.md` | `src/nodes/generate_documents/logic.py` | Generated motivation letter markdown draft. |
| `nodes/generate_documents/proposed/application_email.md` | `src/nodes/generate_documents/logic.py` | Generated email markdown draft. |
| `nodes/generate_documents/assist/proposed/state.json` | `src/nodes/generate_documents/logic.py` | Deterministic text-review indicators. |
| `nodes/generate_documents/assist/proposed/view.md` | `src/nodes/generate_documents/logic.py` | Human-readable text-review table. |
| `nodes/render/proposed/{cv,motivation_letter,application_email}.md` | `src/nodes/render/logic.py` | Render-stage markdown copies. |
| `nodes/render/approved/state.json` | `src/nodes/render/logic.py` | Render envelope with source refs, rendered refs, and content hashes. |
| `nodes/package/approved/state.json` | `src/nodes/package/logic.py` | Package-stage summary pointing to final manifest. |
| `final/{cv,motivation_letter,application_email}.md` | `src/nodes/package/logic.py` | Final packaged markdown deliverables for the current prep flow. |
| `final/manifest.json` | `src/nodes/package/logic.py` | Final artifact inventory and hashes. |
| `graph/run_summary.json` | `ObservabilityService` | Run-level execution summary written by CLI/runtime helpers. |

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.