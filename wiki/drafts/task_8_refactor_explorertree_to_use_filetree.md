---
identity:
  node_id: "doc:wiki/drafts/task_8_refactor_explorertree_to_use_filetree.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/explorer/components/ExplorerTree.tsx`

ExplorerTree and FileTree are nearly identical in structure. ExplorerTree uses `ExplorerEntry` type, FileTree uses `FileTreeNode`. Since they share the same shape (`name, path, is_dir, extension, child_count`), ExplorerTree can delegate to FileTree directly.

- [ ] **Step 1: Replace ExplorerTree with FileTree delegation**

```tsx
import { FileTree, type FileTreeNode } from '../../../components/organisms/FileTree';
import type { ExplorerEntry } from '../../../types/api.types';

interface Props {
  entries: ExplorerEntry[];
  activePath: string;
  onSelect: (path: string) => void;
  onLoadChildren?: (path: string) => void;
  childrenMap?: Record<string, ExplorerEntry[]>;
  indent?: number;
}

function toFileNodes(entries: ExplorerEntry[]): FileTreeNode[] {
  return entries.map(e => ({
    name: e.name,
    path: e.path,
    is_dir: e.is_dir,
    extension: e.extension,
    child_count: e.child_count,
  }));
}

export function ExplorerTree({ entries, activePath, onSelect, onLoadChildren, childrenMap = {}, indent = 0 }: Props) {
  const fileNodes = toFileNodes(entries);
  const fileChildrenMap: Record<string, FileTreeNode[]> = {};
  for (const [key, val] of Object.entries(childrenMap)) {
    fileChildrenMap[key] = toFileNodes(val);
  }

  return (
    <FileTree
      nodes={fileNodes}
      currentPath={activePath}
      onNavigate={path => onLoadChildren?.(path)}
      onFileSelect={onSelect}
      childrenMap={fileChildrenMap}
      indent={indent}
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
git add apps/review-workbench/src/features/explorer/components/ExplorerTree.tsx
git commit -m "refactor(ui): ExplorerTree delegates to FileTree organism (A2)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.