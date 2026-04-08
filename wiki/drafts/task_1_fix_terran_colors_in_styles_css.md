---
identity:
  node_id: "doc:wiki/drafts/task_1_fix_terran_colors_in_styles_css.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

The `.ne-*` CSS classes hardcode light/white backgrounds that clash with the dark Terran theme.

## Details

The `.ne-*` CSS classes hardcode light/white backgrounds that clash with the dark Terran theme.

**Files:**
- Modify: `apps/review-workbench/src/styles.css`

- [ ] **Step 1: Replace the 5 offending CSS rules**

In `styles.css`, find and replace these rules exactly:

```css
/* FIND → REPLACE */

/* 1. .ne-section background */
background: rgba(255, 255, 255, 0.72);
/* → */
background: rgba(0, 242, 255, 0.03);

/* 2. .ne-section-toggle background */
background: linear-gradient(180deg, #fff, #f6f3ed);
/* → */
background: var(--panel);

/* 3. .ne-template-chip background */
background: #f8fbff;
/* → */
background: var(--panel);

/* 4. .ne-node-child background */
background: #fff;
/* → */
background: var(--panel);
```

- [ ] **Step 2: Add ReactFlow node background override**

At the end of `styles.css` (after all `.ne-*` rules), add:

```css
/* Suppress ReactFlow's white node background injection */
.react-flow__node { background: transparent !important; }
.ne-node-free     { background: transparent; }
```

- [ ] **Step 3: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -5
```
Expected: no errors.

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/styles.css
git commit -m "fix(ui): fix .ne-* light backgrounds for Terran dark theme"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.