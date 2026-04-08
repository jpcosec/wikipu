---
identity:
  node_id: "doc:wiki/drafts/task_2_refactor_sourcetextpane_to_use_intelligenteditor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/job-pipeline/components/SourceTextPane.tsx`

SourceTextPane has custom DOM-based text selection + segment rendering. Replace with IntelligentEditor (tag-hover mode) that now supports `onSpanSelect`.

- [ ] **Step 1: Replace SourceTextPane**

```tsx
import { IntelligentEditor } from '../../../components/organisms/IntelligentEditor';
import type { RequirementItem, RequirementTextSpan } from '../../../types/api.types';

interface Props {
  markdown: string;
  highlight: RequirementTextSpan | null;
  requirements?: RequirementItem[];
  onSpanSelect?: (range: { start: number; end: number; text: string }) => void;
}

export function SourceTextPane({ markdown, highlight, requirements = [], onSpanSelect }: Props) {
  // Build highlight from active highlight prop (line-based fallback if no char spans)
  const highlights = highlight?.char_start != null && highlight?.char_end != null
    ? [{ from: highlight.char_start, to: highlight.char_end, className: 'cm-highlight-must' }]
    : [];

  return (
    <div className="flex flex-col h-full">
      <div className="px-3 py-2 border-b border-outline/20">
        <p className="font-mono text-[10px] text-on-muted uppercase tracking-[0.2em]">Source Text</p>
      </div>
      <div className="flex-1 overflow-hidden">
        <IntelligentEditor
          mode="tag-hover"
          content={markdown}
          language="markdown"
          highlights={highlights}
          requirements={requirements}
          readOnly={true}
          onSpanSelect={onSpanSelect}
        />
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Verify build passes**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/job-pipeline/components/SourceTextPane.tsx
git commit -m "refactor(ui): SourceTextPane uses IntelligentEditor (B2 tag-hover)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.