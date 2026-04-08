---
identity:
  node_id: "doc:wiki/drafts/task_15_create_phd_2_0_project_config.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `doc-router.yml` (project root)

- [ ] **Step 1: Create config for this project**

```yaml
# doc-router.yml
project: phd-2.0
domains: [ui, api, pipeline, core, cli, data, policy, practices]
stages: [scrape, translate, extract, match, strategy, drafting, render, package]
natures: [philosophy, implementation, development, testing, design, migration]
doc_paths:
  central: docs/
  seed: docs/seed/
source_paths:
  - src/
  - apps/review-workbench/src/
```

- [ ] **Step 2: Smoke test against the project**

Run: `doc-router scan --project .`
Expected: Shows count of any already-tagged docs (the seed docs don't have frontmatter tags yet, so expect 0 or low numbers). No crashes.

Run: `doc-router lint --project .`
Expected: Clean pass (no nodes = no violations)

- [ ] **Step 3: Commit**

```bash
git add doc-router.yml
git commit -m "feat(doc-router): add PhD 2.0 project config"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.