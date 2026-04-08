---
identity:
  node_id: "doc:wiki/drafts/priority_4_improve_hitl_input_ux_status_completed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

The workflow is semantically correct, but Studio is not yet a polished review UI.

Today the real review action is the submission of `review_payload`, not just pressing `Continue`.

### Why It Matters

- operators need a clearer review experience
- raw payload editing is error-prone
- Studio is good for debugging, but not ideal as a production review surface

### Recommended Change: Textual TUI

Building a reactive terminal-based review TUI allows for structured decisions and evidence patching without manual JSON editing.

**Implementation Details:**
- `src.review_ui.app.MatchReviewApp`: Main Textual application.
- `src.review_ui.screens.ReviewScreen`: Structured review form with `MatchRow` widgets.
- `src.review_ui.bus.MatchBus`: Async bridge for LangGraph thread resumption.
- CLI entry point for human reviewers: planned, see `future_docs/issues/review_ui_wiring.md`.

### Minimum Useful UX

The reviewer should be able to:

- see requirement rows
- see matched evidence and reasoning
- choose `approve`, `request_regeneration`, or `reject`
- attach patch evidence when needed
- submit a valid `ReviewPayload`

### Suggested Steps

1. treat `review/current.json` as the UI source payload
2. build a form/table that maps directly to `ReviewPayload`
3. keep hash validation in the backend
4. preserve round history exactly as it works now

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.