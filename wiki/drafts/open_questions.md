---
identity:
  node_id: "doc:wiki/drafts/open_questions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md", relation_type: "documents"}
---

- Should company-portal-discovered jobs be treated as a new `source` value or as a sub-source under the originating aggregator?

## Details

- Should company-portal-discovered jobs be treated as a new `source` value or as a sub-source under the originating aggregator?
- Which ATS platforms to prioritize first? Greenhouse and Lever are the cleanest; Workday is the most common but hardest (SPA + Cloudflare).
- What is the right HITL gate for auto-application? Per-domain once for form approval, per-job always for final submission confirmation, or opt-in per run?
- File formats: some portals only accept `.docx`, others only `.pdf`. The render pipeline already supports both — this needs to be wired into the form analyzer's `cv_upload` resolution.
- Where do browser profiles live? `data/profiles/` is convenient but should not be committed. Add to `.gitignore`.

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md`.