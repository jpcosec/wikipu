---
identity:
  node_id: "doc:wiki/drafts/7_browser_profile_config_browser_os_default.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

The real Chromium user profile. Contains:

## Details

The real Chromium user profile. Contains:
- `Cookies` — login sessions for all portals (XING, StepStone, LinkedIn, etc.)
- `Local Storage/` — portal-specific app state
- `IndexedDB/` — heavier app storage

This is what makes BrowserOS already logged in to portals. We do not manage this — BrowserOS manages it. Our job is to not break it (don't clear cookies, don't open incognito).

**Persistence across restarts:** Cookies survive BrowserOS restarts because they live in the filesystem profile, not in memory. Login sessions persist as long as the portal's session expiry allows (typically weeks to months for "remember me" sessions).

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.