---
identity:
  node_id: "doc:wiki/drafts/6_session_management.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

Session persistence is handled via crawl4ai's native `BrowserConfig`:

## Details

Session persistence is handled via crawl4ai's native `BrowserConfig`:

```python
BrowserConfig(
    user_data_dir=str(adapter.get_session_profile_dir()),
    use_persistent_context=True,
    headless=True,
)
```

Profile directories:
```
data/profiles/
  xing_profile/
  stepstone_profile/
```

These directories are `.gitignore`d — they contain live session cookies, never committed.

**First-time setup (HITL):** User runs `python -m src.apply.main --source xing --setup-session`, which opens a visible browser pointing at the profile dir. User logs in manually and closes. Subsequent runs reuse the session headlessly. When the session expires, the portal redirects to login and `_validate_selectors` raises `PortalStructureChangedError` with a message indicating session refresh is needed.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.