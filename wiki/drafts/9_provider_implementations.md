---
identity:
  node_id: "doc:wiki/drafts/9_provider_implementations.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

Each provider implements only:

## Details

Each provider implements only:
- `source_name` property
- `get_form_selectors()` — CSS selectors discovered by sampling real apply pages
- `get_open_modal_script()` — C4A-Script that only clicks apply and waits for modal
- `get_fill_form_script(profile)` — C4A-Script for filling text fields and dropdowns (runs after validation)
- `get_submit_script()` — C4A-Script for the submit action (separated for dry-run support)
- `get_success_text()` — expected confirmation copy
- `get_session_profile_dir()` — path to the persistent browser profile

**Precondition:** The C4A-Script and selectors for XING and StepStone Easy Apply must be discovered by sampling real apply pages before implementation. This sampling step is also what produces the HTML fixtures needed for integration tests.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.