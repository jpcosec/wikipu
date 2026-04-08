---
identity:
  node_id: "doc:wiki/drafts/task_3_refactor_documenteditor_to_use_intelligenteditor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/job-pipeline/components/DocumentEditor.tsx`

DocumentEditor is just CodeMirror with markdown. Replace with IntelligentEditor (fold mode = editable markdown with syntax highlighting).

- [ ] **Step 1: Replace DocumentEditor**

```tsx
import { IntelligentEditor } from '../../../components/organisms/IntelligentEditor';

interface Props {
  content: string;
  onChange: (value: string) => void;
}

export function DocumentEditor({ content, onChange }: Props) {
  return (
    <IntelligentEditor
      mode="fold"
      content={content}
      language="markdown"
      onChange={onChange}
      className="h-full"
    />
  );
}
```

- [ ] **Step 2: Verify build**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/job-pipeline/components/DocumentEditor.tsx
git commit -m "refactor(ui): DocumentEditor uses IntelligentEditor (B4 fold mode)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.