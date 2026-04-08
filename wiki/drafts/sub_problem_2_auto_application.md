---
identity:
  node_id: "doc:wiki/drafts/sub_problem_2_auto_application.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md", relation_type: "documents"}
---

### Overview

## Details

### Overview

| Path | Crawl4AI feasibility | Deferred? |
|------|---------------------|-----------|
| **Email** (`application_method: email`) | N/A (SMTP, not browser) | Yes — deferred |
| **Inline portal form** (Easy Apply on XING/StepStone) | High | No |
| **Company portal form** (external ATS, no account) | Medium | No |
| **Company portal form** (external ATS, requires account) | Medium | Account creation = HITL once; session persisted via browser profile |

### Form interaction — two complementary tools

**Playwright hooks** (via `on_page_context_created`) — best for file uploads and multi-step flows:

```python
async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
    await page.fill("input[name='firstname']", profile.first_name)
    await page.fill("input[name='email']", profile.email)
    await page.set_input_files("input[type='file'][accept='.pdf']", str(cv_path))
    await page.select_option("select[name='experience']", "5+ years")
    await page.click("button[type='submit']")
    await page.wait_for_selector(".application-confirmation", timeout=15000)
```

**`js_code` in `CrawlerRunConfig`** — preferred for React/Vue SPAs where Playwright events sometimes fail to trigger framework state updates. The LLM can generate the JS snippet as part of form analysis:

```python
config = CrawlerRunConfig(
    js_code=llm_generated_js,   # e.g. React-friendly value setters + submit trigger
    wait_for="css:.success-message"
)
```

Use hooks for file uploads (no JS equivalent) and `js_code` when the SPA does not respond to synthetic Playwright events.

### Form analyzer (the missing piece)

The key non-trivial component is mapping candidate profile data to the specific fields of an unknown form. Proposed approach:

1. **Crawl the apply page** with LLM extraction to produce a `FormFieldMap`:
   ```python
   class FormField(BaseModel):
       selector: str       # CSS selector to the input
       label: str          # Human-visible label text
       field_type: str     # text, select, file, textarea, checkbox
       semantic: str       # LLM-inferred: "first_name", "cv_upload", "cover_letter", etc.
       required: bool
   ```

2. **Profile mapper** resolves `semantic → profile value`:
   - `"first_name"` → `profile.first_name`
   - `"cv_upload"` → `artifacts/render/cv.pdf` or `.docx` depending on what the portal accepts
   - `"cover_letter"` → `artifacts/render/letter.pdf`
   - `"linkedin_url"` → `profile.linkedin`
   - Unknown semantics → flag for human review before submission

3. **Form filler** executes fills via Playwright hook or `js_code` depending on the detected SPA type.

4. **Confirmation verifier** waits for a success indicator and persists the submission artifact.

### Account-required portals

The problem decomposes into two independent concerns:

**1. Account creation — HITL step**

Account creation (email verification, captchas, profile setup) is a one-time-per-domain operation that is not worth automating. The pipeline detects that a domain requires an account, pauses, and surfaces a `create_account.md` review file with the registration URL and the profile data to use. The human creates the account manually and resumes. This only happens once per ATS domain.

**2. Session persistence — browser profile**

Once an account exists, there is no need to store or inject credentials. Crawl4AI supports persistent browser profiles natively:

```python
browser_config = BrowserConfig(
    user_data_dir="data/profiles/workday_profile",
    use_persistent_context=True,
)
```

The browser profile stores cookies and session tokens exactly as a real browser would. After the human completes the HITL login step with this profile directory open, every subsequent run reuses the live session. No credentials touch the code, the artifacts, or the repo.

| Scenario | Feasibility |
|----------|-------------|
| Account creation | HITL (one-time per domain) |
| Subsequent runs | High — profile reuse, no credential handling in code |
| Session expiry | Triggers a new HITL re-login prompt |

### Artifacts produced by auto-application

After successful submission, write under `data/jobs/<source>/<job_id>/nodes/apply/`:

```
proposed/
  application_record.json    # what was filled, when, confirmation URL/text
  form_field_map.json        # the LLM-inferred form field map
  confirmation.md            # human-readable confirmation surface
meta/
  apply_meta.json            # success flag, method, timestamp, error if any
```

### Submission safety rules

- **Human approval gate before first submission to any new domain.** The system proposes the `FormFieldMap` and mapped values; a human confirms before the form is actually submitted. This gate can be relaxed per domain after first successful use.
- **Dry-run mode**: fills the form but does not submit (`skip_submit=True` flag). Produces a screenshot artifact for review.
- **No submitting the same job twice.** Check `apply_meta.json` existence before proceeding.

---

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md`.