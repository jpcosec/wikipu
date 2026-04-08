---
identity:
  node_id: "doc:wiki/drafts/task_5_c1_b_refactor_basecveditor_as_thin_knowledgegraph_wrapper.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Replace the complex 376-line `BaseCvEditor.tsx` with a thin wrapper that uses `KnowledgeGraph` with the CV adapter.

## Details

Replace the complex 376-line `BaseCvEditor.tsx` with a thin wrapper that uses `KnowledgeGraph` with the CV adapter.

**Files:**
- Modify: `apps/review-workbench/src/pages/global/BaseCvEditor.tsx`

- [ ] **Step 1: Replace BaseCvEditor.tsx entirely**

```tsx
// apps/review-workbench/src/pages/global/BaseCvEditor.tsx
import { useMemo } from 'react';
import { useCvProfileGraph, useSaveCvGraph } from '../../features/base-cv/api/useCvProfileGraph';
import { cvProfileToGraph, graphToCvProfile } from '../../features/base-cv/lib/cvToGraph';
import { KnowledgeGraph } from './KnowledgeGraph';
import { Spinner } from '../../components/atoms/Spinner';
import type { SimpleNode, SimpleEdge } from './KnowledgeGraph';

export function BaseCvEditor() {
  const query = useCvProfileGraph();
  const saveMutation = useSaveCvGraph();

  const { nodes, edges } = useMemo(
    () => query.data ? cvProfileToGraph(query.data) : { nodes: [], edges: [] },
    [query.data],
  );

  const handleSave = (savedNodes: SimpleNode[], savedEdges: SimpleEdge[]) => {
    if (!query.data) return;
    saveMutation.mutate(graphToCvProfile(savedNodes, savedEdges, query.data));
  };

  if (query.isLoading) {
    return <div className="flex items-center justify-center h-full"><Spinner size="md" /></div>;
  }

  if (query.isError || !query.data) {
    return (
      <div className="p-6">
        <p className="font-mono text-error text-sm">CV_PROFILE_GRAPH_NOT_FOUND</p>
      </div>
    );
  }

  return (
    <KnowledgeGraph
      initialNodes={nodes}
      initialEdges={edges}
      onSave={handleSave}
    />
  );
}
```

- [ ] **Step 2: Check that KnowledgeGraph is exported**

In `KnowledgeGraph.tsx`, verify the main function is exported. If it's wrapped in `ReactFlowProvider` and the outer function is named `KnowledgeGraph`, ensure it's exported with `export`.

- [ ] **Step 3: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -10
```
Expected: no errors.

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/pages/global/BaseCvEditor.tsx
git commit -m "feat(ui): replace BaseCvEditor with thin KnowledgeGraph wrapper (C1-B)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.