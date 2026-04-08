---
identity:
  node_id: "doc:wiki/drafts/task_12_testsprite_e2e.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Run TestSprite to validate all refactored pages.**

## Details

**Run TestSprite to validate all refactored pages.**

- [ ] **Step 1: Check TestSprite account**

Use `mcp__TestSprite__testsprite_check_account_info` tool.

- [ ] **Step 2: Generate code summary for TestSprite**

Use `mcp__TestSprite__testsprite_generate_code_summary` — this gives TestSprite context about the current codebase.

- [ ] **Step 3: Generate/update frontend test plan**

Use `mcp__TestSprite__testsprite_generate_frontend_test_plan` targeting the refactored pages:
- B1: `/jobs/tu_berlin/201397/scrape`
- B1b: `/jobs/tu_berlin/201397/translate`
- B2: `/jobs/tu_berlin/201397/extract`
- B3: `/jobs/tu_berlin/201397/match`
- B4: `/jobs/tu_berlin/201397/sculpt`
- A2: `/explorer`
- A3: `/cv`

- [ ] **Step 4: Execute tests**

Use `mcp__TestSprite__testsprite_generate_code_and_execute` to run the tests.

- [ ] **Step 5: Review results**

Use `mcp__TestSprite__testsprite_open_test_result_dashboard` to inspect failures.

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.