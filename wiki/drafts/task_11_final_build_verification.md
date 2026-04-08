---
identity:
  node_id: "doc:wiki/drafts/task_11_final_build_verification.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

- [ ] **Step 1: Full TypeScript check**

## Details

- [ ] **Step 1: Full TypeScript check**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1
```

Expected: no errors.

- [ ] **Step 2: Dev server smoke test**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npm run dev &
sleep 5 && curl -s http://localhost:5173 | head -5
```

Expected: HTML response (app running).

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.