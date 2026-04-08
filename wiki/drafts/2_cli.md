---
identity:
  node_id: "doc:wiki/drafts/2_cli.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

```bash

## Details

```bash
# Apply to a job
python -m src.apply.main \
  --source xing \
  --job-id 12345 \
  --cv path/to/cv.pdf \
  [--letter path/to/letter.pdf] \
  [--dry-run]

# First-time session setup for a portal (mutually exclusive with the above)
python -m src.apply.main --source xing --setup-session
```

**Apply mode inputs:**
- `--source` + `--job-id`: locates the job. Reads `data/jobs/<source>/<job_id>/nodes/ingest/proposed/state.json` to get `application_url`, `job_title`, `company_name`.
- `--cv`: path to the CV PDF. Passed explicitly — the module does not search for it in artifacts.
- `--letter`: optional. If the portal does not request it, it is ignored.
- `--dry-run`: activates marcha blanca mode (see Section 5).

**`--setup-session` mode** is mutually exclusive with `--job-id` / `--cv`. When present:
1. Opens `BrowserConfig(user_data_dir=profile_dir, use_persistent_context=True, headless=False)`
2. Navigates to the portal's base URL
3. Prints "Log in manually. Press Enter when done." and waits for input
4. Closes the context — cookies and session tokens are now persisted in the profile dir
No validation, no C4A-Script, no artifacts written.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.