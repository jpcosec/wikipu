---
identity:
  node_id: "doc:wiki/drafts/user_guide_isolated_browser_profile_for_auto_apply.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/bot_profile_setup.md", relation_type: "documents"}
---

To allow the bot to postulations using your account without manual login:

## Details

To allow the bot to postulations using your account without manual login:

1. **Create the profile:** Run Chrome once with a custom directory:
   `google-chrome --user-data-dir=$(pwd)/.browser_profiles/bot_profile`
2. **Login:** Manually log in to StepStone, LinkedIn, etc. Solve any Captchas.
3. **Accept Cookies:** Ensure you accept cookies so the session persists.
4. **Close Chrome:** Exit completely.
5. **Run the Bot:** The `PlaywrightFetcher` is configured to use this path. **CRITICAL:** Close your personal Chrome if it uses the same path, or better yet, keep them isolated.

Generated from `raw/docs_postulador_langgraph/docs/operations/bot_profile_setup.md`.