---
identity:
  node_id: "doc:wiki/drafts/task_8_c1_c_create_unmappedskillspanel.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

A collapsible right-rail panel that lists profile nodes with no edges.

## Details

A collapsible right-rail panel that lists profile nodes with no edges.

**Files:**
- Create: `apps/review-workbench/src/features/job-pipeline/components/UnmappedSkillsPanel.tsx`

- [ ] **Step 1: Create the component**

```tsx
// apps/review-workbench/src/features/job-pipeline/components/UnmappedSkillsPanel.tsx
import { useState } from 'react';
import { cn } from '../../../utils/cn';
import type { SimpleNode } from '../../../pages/global/KnowledgeGraph';

interface Props {
  unmappedNodes: SimpleNode[];
  onSelectNode: (nodeId: string) => void;
}

export function UnmappedSkillsPanel({ unmappedNodes, onSelectNode }: Props) {
  const [collapsed, setCollapsed] = useState(false);

  if (collapsed) {
    return (
      <div className="w-8 border-l border-outline/20 bg-surface flex flex-col items-center pt-3 cursor-pointer"
           onClick={() => setCollapsed(false)}>
        <span className="font-mono text-[9px] text-on-muted rotate-90 whitespace-nowrap mt-4">
          UNMAPPED ({unmappedNodes.length})
        </span>
      </div>
    );
  }

  return (
    <aside className="w-64 border-l border-outline/20 bg-surface flex flex-col overflow-hidden shrink-0">
      <div className="flex items-center justify-between px-3 py-2 border-b border-outline/20">
        <span className="font-mono text-[10px] text-on-muted uppercase tracking-widest">
          Unmapped ({unmappedNodes.length})
        </span>
        <button
          onClick={() => setCollapsed(true)}
          className="font-mono text-[10px] text-on-muted/60 hover:text-on-muted"
        >
          ›
        </button>
      </div>
      <div className="flex-1 overflow-y-auto p-2 flex flex-col gap-1">
        {unmappedNodes.length === 0 ? (
          <p className="font-mono text-[10px] text-on-muted/60 p-2">All skills mapped</p>
        ) : (
          unmappedNodes.map(node => (
            <button
              key={node.id}
              onClick={() => onSelectNode(node.id)}
              className={cn(
                'text-left px-2 py-1.5 border border-outline/20',
                'font-mono text-[11px] text-on-surface hover:border-primary/40',
                'hover:bg-primary/5 transition-colors',
              )}
            >
              {node.data.name}
              {node.data.properties['score'] && (
                <span className="ml-1 text-on-muted/60">{node.data.properties['score']}</span>
              )}
            </button>
          ))
        )}
      </div>
    </aside>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add apps/review-workbench/src/features/job-pipeline/components/UnmappedSkillsPanel.tsx
git commit -m "feat(ui): add UnmappedSkillsPanel component (C1-C)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.