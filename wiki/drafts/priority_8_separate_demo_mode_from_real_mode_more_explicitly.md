---
identity:
  node_id: "doc:wiki/drafts/priority_8_separate_demo_mode_from_real_mode_more_explicitly.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

The Studio fallback chain is useful, but it should be very clear when the system is in demo mode.

### Recommended Change

Make demo mode explicit in state or metadata.

Possible additions:

- `mode: demo | live`
- a visible warning in the review surface
- explicit metadata in traces and persisted artifacts

### Suggested Steps

1. add a mode flag to `create_studio_graph()` output metadata or state
2. persist that mode in review artifacts
3. surface it in docs and review payload examples

Generated from `raw/docs_postulador_refactor/future_docs/issues/match_skill_hardening_roadmap.md`.