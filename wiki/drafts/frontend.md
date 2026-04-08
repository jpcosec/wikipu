---
identity:
  node_id: "doc:wiki/drafts/frontend.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md", relation_type: "documents"}
---

- Add TabNav component

## Details

- Add TabNav component
- Add Plans tab with list, timeline, editor
- Add Files tab with tree and preview
```

- [ ] **Step 2: Verify backend serves the plan**

Run: `curl http://127.0.0.1:8030/api/plans`
Expected: JSON array containing `doc-router-phase2` group

Run: `curl http://127.0.0.1:8030/api/plans/doc-router-phase2`
Expected: Chain with one entry (plan, version 0)

Run: `curl http://127.0.0.1:8030/api/plans/doc-router-phase2/plan_0`
Expected: metadata + content of the plan

- [ ] **Step 3: Verify file tree endpoint**

Run: `curl "http://127.0.0.1:8030/api/files?path=src/doc_router"`
Expected: JSON array listing doc_router module files

Run: `curl "http://127.0.0.1:8030/api/files/content?path=src/doc_router/plans.py"`
Expected: File content with language "python"

- [ ] **Step 4: Run all backend tests**

Run: `python -m pytest tests/ -v`
Expected: ALL PASS

- [ ] **Step 5: Verify frontend builds and tabs work**

Run: `cd ui && npx vite build 2>&1 | tail -5`
Expected: Build succeeds

Start dev servers and navigate to http://127.0.0.1:6680:
- Graph tab should show the existing 3 nodes
- Plans tab should list `doc-router-phase2` group
- Clicking it should show the iteration timeline with `plan_0`
- Clicking `plan_0` should show the plan content in the editor
- Files tab should show the project file tree

- [ ] **Step 6: Commit the sample plan**

```bash
git add docs/plans/
git commit -m "feat(doc-router): add sample plan for phase 2 E2E validation"
```

---

### Task 16: Port change + dev script update

**Files:**
- Already done: `ui/vite.config.ts` (port 6680)
- Already done: `scripts/dev-doc-router.sh` (port 6680)

- [ ] **Step 1: Verify port changes are committed**

Check `git diff` for uncommitted port changes. If any:

```bash
git add ui/vite.config.ts scripts/dev-doc-router.sh
git commit -m "fix(doc-router): change frontend port to 6680 (avoid conflict with PhD pipeline)"
```

- [ ] **Step 2: Done**

This task covers the port changes already made earlier in this session.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md`.