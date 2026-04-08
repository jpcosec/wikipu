---
identity:
  node_id: "doc:wiki/drafts/task_12_frontend_atom_components.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `ui/src/components/atoms/Badge.tsx`
- Create: `ui/src/components/atoms/Button.tsx`
- Create: `ui/src/components/atoms/Icon.tsx`
- Create: `ui/src/components/atoms/Spinner.tsx`
- Create: `ui/src/components/atoms/Tag.tsx`

- [ ] **Step 1: Copy atoms from review-workbench**

Copy these files from `/home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench/src/components/atoms/`:
- `Badge.tsx`
- `Button.tsx`
- `Icon.tsx`
- `Spinner.tsx`
- `Tag.tsx`

Update import paths: change `../../utils/cn` to `@/utils/cn` or relative paths matching the new structure.

- [ ] **Step 2: Verify typecheck**

Run: `cd ui && npx tsc --noEmit`
Expected: No errors

- [ ] **Step 3: Commit**

```bash
git add ui/src/components/atoms/
git commit -m "feat(doc-router): copy atom components from review-workbench"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.