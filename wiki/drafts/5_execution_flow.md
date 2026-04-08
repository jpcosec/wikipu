---
identity:
  node_id: "doc:wiki/drafts/5_execution_flow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

The flow uses crawl4ai natively throughout. Each step is a separate `arun()` call sharing the same `session_id`. Raw Playwright is used **only** for file uploads inside a hook, because `set_input_files` has no browser-JS equivalent for security reasons.

## Details

The flow uses crawl4ai natively throughout. Each step is a separate `arun()` call sharing the same `session_id`. Raw Playwright is used **only** for file uploads inside a hook, because `set_input_files` has no browser-JS equivalent for security reasons.

```
read ingest artifact → get application_url, job_title, company_name
    ↓
idempotency check:
  status=submitted  → abort with warning (already applied)
  status=dry_run    → allow (dry-run artifacts will be overwritten by real run)
  status=failed / portal_changed → allow retry (prior artifacts overwritten)
    ↓
build BrowserConfig(user_data_dir=profile_dir, use_persistent_context=True)
    ↓  session carries prior login cookies — no credential handling in code
    ↓  if session expired → portal redirects to login → PortalStructureChangedError
    ↓  (human re-logs in via --setup-session and retries)
    ↓
[try block starts here]
    ↓
Step 1 — open modal only (C4A-Script):
  CrawlerRunConfig(
    c4a_script=adapter.get_open_modal_script(),   ← CLICK apply button + WAIT modal container
    wait_for=f"css:{selectors.cv_upload or selectors.first_name}",
    session_id="apply_{job_id}",
  )
    ↓  modal open, form fields now exist in DOM — safe to validate
    ↓
_validate_selectors(selectors)   ← runtime check #1 — queries DOM via js_code
    ↓ missing mandatory selector → PortalStructureChangedError
    ↓
Step 2 — fill form + upload CV (single arun() call):
  CrawlerRunConfig(
    js_only=True,
    c4a_script=_render_script(adapter.get_fill_form_script(profile)),
    hooks={"before_retrieve_html": _file_upload_hook(cv_path, letter_path, selectors)},
    screenshot=True,
    session_id="apply_{job_id}",
  )
    ↓  C4A-Script fills text fields and dropdowns
    ↓  before_retrieve_html hook runs after script, same browser state — no re-evaluation
    ↓    page.set_input_files(cv_upload, cv_path)  ← no browser-JS equivalent
    ↓    if cv_upload absent and cv_select_existing present:
    ↓      page.click(cv_select_existing)
    ↓      page.wait_for_timeout(500)  ← stabilize DOM if click triggers submenu/animation
    ↓  screenshot saved → proposed/screenshot.png
    ↓
[dry-run] → write ApplicationRecord + ApplyMeta(status=dry_run) → exit
    ↓
[auto] Step 3 — submit + verify (C4A-Script):
  CrawlerRunConfig(
    js_only=True,
    c4a_script=adapter.get_submit_script(),
    wait_for=f"css:{selectors.success_indicator}",
    screenshot=True,
    session_id="apply_{job_id}",
  )
    ↓
_validate_success_text(result)           ← runtime check #2
    ↓ text not found → LogTag.WARN only (copy changes are common)
    ↓
write ApplicationRecord + ApplyMeta(status=submitted)

[except block]
    → CrawlerRunConfig(js_only=True, screenshot=True, session_id=...) → error_state.png
    → write ApplyMeta(status=portal_changed or failed, error=str(exc))
    → raise
```

### Why C4A-Script for portal-specific behavior

Each adapter expresses its interaction sequence in readable, self-documenting DSL. `IF/THEN` handles conditional fields (e.g. salutation dropdowns that only appear on certain locales) without Python branching. `WAIT` with element readiness avoids the flaky "element in DOM but not interactive" problem naturally. `EVAL` is the escape hatch for edge cases that need raw JS.

### Profile value sanitization

`_render_script(template, profile)` in the base class interpolates `{{field}}` placeholders using `json.dumps(value)` for each profile value before injection. This ensures apostrophes, quotes, and other special characters are properly escaped and never break C4A-Script parsing.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.