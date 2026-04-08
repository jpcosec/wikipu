---
identity:
  node_id: "doc:wiki/drafts/task_2_fix_category_colors_in_knowledgegraph_tsx.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Replace the flat pastel string map with dark border+bg pairs and update SimpleNodeCard rendering.

## Details

Replace the flat pastel string map with dark border+bg pairs and update SimpleNodeCard rendering.

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`

- [ ] **Step 1: Replace CATEGORY_COLORS constant**

Find:
```ts
const CATEGORY_COLORS: Record<string, string> = {
  person: "#e8d5b7",
  skill: "#d5e8b7",
  project: "#b7d5e8",
  publication: "#e8b7d5",
  concept: "#d9d6f8",
};
```

Replace with:
```ts
const CATEGORY_COLORS: Record<string, { border: string; bg: string }> = {
  person:      { border: 'rgba(0,242,255,0.5)',   bg: 'rgba(0,242,255,0.07)' },
  skill:       { border: 'rgba(255,170,0,0.5)',   bg: 'rgba(255,170,0,0.07)' },
  project:     { border: 'rgba(0,242,255,0.25)',  bg: 'rgba(0,242,255,0.04)' },
  publication: { border: 'rgba(255,180,171,0.5)', bg: 'rgba(255,180,171,0.07)' },
  concept:     { border: 'rgba(116,117,120,0.5)', bg: 'rgba(116,117,120,0.07)' },
  document:    { border: 'rgba(0,242,255,0.6)',   bg: 'rgba(0,242,255,0.06)' },
  section:     { border: 'rgba(255,170,0,0.4)',   bg: 'rgba(255,170,0,0.05)' },
  entry:       { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' },
};
```

- [ ] **Step 2: Update SimpleNodeCard to use color.border and color.bg**

Find the `SimpleNodeCard` component (currently around line 445). It currently does:
```ts
const bg = CATEGORY_COLORS[nodeData.category] ?? "#e5e7eb";
```
and renders:
```tsx
style={{ backgroundColor: bg }}
```

Replace those two with:
```ts
const color = CATEGORY_COLORS[nodeData.category] ?? { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' };
```
and update the `<div>` style:
```tsx
style={{
  borderLeft: `4px solid ${color.border}`,
  background: color.bg,
  color: 'var(--text-main)',
}}
```

- [ ] **Step 3: Extend CATEGORY_OPTIONS and NODE_TEMPLATES**

Find:
```ts
const CATEGORY_OPTIONS = ["person", "skill", "project", "publication", "concept"];
```
Replace with:
```ts
const CATEGORY_OPTIONS = ["person", "skill", "project", "publication", "concept", "document", "section", "entry"];
```

Find `NODE_TEMPLATES` array and add at the end:
```ts
  { name: 'Document', category: 'document', defaults: { title: 'Untitled', type: 'cv' } },
  { name: 'Section',  category: 'section',  defaults: { title: 'New Section' } },
  { name: 'Entry',    category: 'entry',    defaults: { title: '', date: '' } },
```

- [ ] **Step 4: Extend SimpleNodeData with meta passthrough**

Find:
```ts
interface SimpleNodeData extends Record<string, unknown> {
  name: string;
  category: string;
  properties: Record<string, string>;
  nodeId?: string;
  onEditNode?: (nodeId: string) => void;
}
```
Add `meta?: unknown;` as the last field before the closing brace.

- [ ] **Step 5: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -5
```

- [ ] **Step 6: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "fix(ui): replace CATEGORY_COLORS with Terran dark pairs in KnowledgeGraph"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.