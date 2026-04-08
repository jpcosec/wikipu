---
identity:
  node_id: "doc:wiki/drafts/task_10_refactor_cvgraphcanvas_to_use_graphcanvas.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Read and modify: `src/features/base-cv/components/CvGraphCanvas.tsx`

CvGraphCanvas uses ReactFlow directly. Read the file first to understand node positioning strategy (likely manual/DnD-based). Then wrap the ReactFlow portion with GraphCanvas using `layout='manual'` and the existing custom nodeTypes.

- [ ] **Step 1: Read CvGraphCanvas**

```bash
cat apps/review-workbench/src/features/base-cv/components/CvGraphCanvas.tsx
```

- [ ] **Step 2: Identify what GraphCanvas replaces**

CvGraphCanvas likely uses `ReactFlow` directly. GraphCanvas with `layout='manual'` passes through positions as-is. Identify:
- Custom nodeTypes → pass to GraphCanvas's `nodeTypes` prop
- `onConnect` → pass via GraphCanvas's `onConnect` prop
- Any other ReactFlow props that GraphCanvas exposes

- [ ] **Step 3: Refactor CvGraphCanvas to use GraphCanvas**

Replace the internal `ReactFlow` component with `GraphCanvas` using `layout='manual'`. Keep DnD wrappers unchanged (they're outside ReactFlow).

Convert CvEntry/CvSkill data to the generic `GraphNode[]` and `GraphEdge[]` shapes expected by GraphCanvas.

- [ ] **Step 4: Verify build**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/src/features/base-cv/components/CvGraphCanvas.tsx
git commit -m "refactor(ui): CvGraphCanvas uses GraphCanvas organism (A3)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.