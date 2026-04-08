---
identity:
  node_id: "doc:wiki/drafts/task_9_refactor_jsonpreview_and_markdownpreview_to_use_intelligenteditor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/explorer/components/JsonPreview.tsx`
- Modify: `src/features/explorer/components/MarkdownPreview.tsx`

Both components render read-only text. IntelligentEditor (fold mode) with respective language provides syntax highlighting + fold gutter.

- [ ] **Step 1: Replace JsonPreview**

```tsx
import { IntelligentEditor } from '../../../components/organisms/IntelligentEditor';

interface Props { content: string; }

export function JsonPreview({ content }: Props) {
  return (
    <div className="h-full overflow-hidden">
      <IntelligentEditor mode="fold" content={content} language="json" readOnly />
    </div>
  );
}
```

- [ ] **Step 2: Replace MarkdownPreview**

```tsx
import { IntelligentEditor } from '../../../components/organisms/IntelligentEditor';

interface Props { content: string; }

export function MarkdownPreview({ content }: Props) {
  return (
    <div className="h-full overflow-hidden">
      <IntelligentEditor mode="fold" content={content} language="markdown" readOnly />
    </div>
  );
}
```

- [ ] **Step 3: Verify build**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/features/explorer/components/JsonPreview.tsx \
        apps/review-workbench/src/features/explorer/components/MarkdownPreview.tsx
git commit -m "refactor(ui): JsonPreview + MarkdownPreview use IntelligentEditor (A2 fold)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.