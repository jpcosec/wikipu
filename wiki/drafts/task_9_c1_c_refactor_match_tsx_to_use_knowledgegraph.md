---
identity:
  node_id: "doc:wiki/drafts/task_9_c1_c_refactor_match_tsx_to_use_knowledgegraph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Replace `MatchGraphCanvas` + search toolbar with `KnowledgeGraph` seeded from `matchPayloadToGraph`. Keep `MatchDecisionModal`.

## Details

Replace `MatchGraphCanvas` + search toolbar with `KnowledgeGraph` seeded from `matchPayloadToGraph`. Keep `MatchDecisionModal`.

**Files:**
- Modify: `apps/review-workbench/src/pages/job/Match.tsx`

- [ ] **Step 1: Replace Match.tsx**

```tsx
// apps/review-workbench/src/pages/job/Match.tsx
import { useState, useMemo, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import { useViewMatch } from '../../features/job-pipeline/api/useViewMatch';
import { useGateDecide } from '../../features/job-pipeline/api/useGateDecide';
import { KnowledgeGraph } from '../global/KnowledgeGraph';
import { UnmappedSkillsPanel } from '../../features/job-pipeline/components/UnmappedSkillsPanel';
import { MatchDecisionModal } from '../../features/job-pipeline/components/MatchDecisionModal';
import { Spinner } from '../../components/atoms/Spinner';
import { matchPayloadToGraph, graphToMatchEdits } from '../../features/job-pipeline/lib/matchToGraph';
import type { GateDecisionPayload } from '../../types/api.types';
import type { SimpleNode, SimpleEdge } from '../global/KnowledgeGraph';

export function Match() {
  const { source, jobId } = useParams<{ source: string; jobId: string }>();
  const matchQuery = useViewMatch(source!, jobId!);
  const gateDecide = useGateDecide(source!, jobId!, 'review_match');

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentNodes, setCurrentNodes] = useState<SimpleNode[]>([]);
  const [currentEdges, setCurrentEdges] = useState<SimpleEdge[]>([]);

  const { nodes: initialNodes, edges: initialEdges } = useMemo(() => {
    if (matchQuery.data?.view === 'match') {
      return matchPayloadToGraph(matchQuery.data.data);
    }
    return { nodes: [], edges: [] };
  }, [matchQuery.data]);

  const unmappedNodes = useMemo(() => {
    const mappedTargets = new Set(currentEdges.map(e => e.target));
    return currentNodes.filter(
      n => n.data.properties['kind'] === 'profile' &&
           n.type === 'simple' &&
           !mappedTargets.has(n.id)
    );
  }, [currentNodes, currentEdges]);

  const handleGraphChange = useCallback((nodes: SimpleNode[], edges: SimpleEdge[]) => {
    setCurrentNodes(nodes);
    setCurrentEdges(edges);
  }, []);

  const handleSelectUnmapped = useCallback((_nodeId: string) => {
    // KnowledgeGraph doesn't expose a programmatic select yet — no-op for now
  }, []);

  const handleDecide = (payload: GateDecisionPayload) => {
    gateDecide.mutate(payload, {
      onSuccess: () => setIsModalOpen(false),
    });
  };

  if (matchQuery.isLoading) {
    return <div className="flex items-center justify-center h-full"><Spinner size="md" /></div>;
  }

  if (matchQuery.isError || !matchQuery.data || matchQuery.data.view !== 'match') {
    return <div className="p-6"><p className="font-mono text-error text-sm">MATCH_DATA_NOT_FOUND</p></div>;
  }

  return (
    <div className="flex h-full overflow-hidden">
      <div className="flex-1 min-w-0">
        <KnowledgeGraph
          initialNodes={initialNodes}
          initialEdges={initialEdges}
          onSave={handleGraphChange}
        />
      </div>

      <UnmappedSkillsPanel
        unmappedNodes={unmappedNodes}
        onSelectNode={handleSelectUnmapped}
      />

      <MatchDecisionModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onDecide={handleDecide}
        isLoading={gateDecide.isPending}
      />
    </div>
  );
}
```

**Note:** The "DECIDE" button to open the modal needs to be accessible. Since KnowledgeGraph has its own sidebar, add a floating DECIDE button at the bottom of the left edge of the Match layout as a temporary measure:

```tsx
{/* Floating DECIDE button */}
<button
  onClick={() => setIsModalOpen(true)}
  className="absolute bottom-6 left-6 z-50 font-mono text-[11px] tracking-widest border border-primary/60 text-primary bg-surface px-4 py-2 hover:bg-primary/10 transition-colors"
>
  DECIDE
</button>
```

Wrap the outer `<div>` with `className="relative flex h-full overflow-hidden"` for positioning.

- [ ] **Step 2: Add KnowledgeGraph onChange callback**

`KnowledgeGraph` doesn't have an `onChange` prop yet. For the unmapped panel to work, we need live node/edge state. Add an `onChange?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void` prop to `KnowledgeGraph`:

In KnowledgeGraph.tsx, add `onChange?` to `KnowledgeGraphProps`:
```ts
interface KnowledgeGraphProps {
  initialNodes?: SimpleNode[];
  initialEdges?: SimpleEdge[];
  onSave?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
  onChange?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
}
```

Then in the `onNodesChange`/`onEdgesChange` handlers, call `onChange?.(nodes, edges)` after each change. The simplest approach: add a `useEffect` that fires whenever `nodes` or `edges` changes:

```ts
useEffect(() => {
  onChange?.(nodes, edges);
}, [nodes, edges, onChange]);
```

- [ ] **Step 3: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -10
```
Expected: no errors.

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/pages/job/Match.tsx \
        apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "feat(ui): replace Match page with KnowledgeGraph + UnmappedSkillsPanel (C1-C)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.