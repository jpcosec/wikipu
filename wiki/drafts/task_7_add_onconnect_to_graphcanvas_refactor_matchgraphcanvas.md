---
identity:
  node_id: "doc:wiki/drafts/task_7_add_onconnect_to_graphcanvas_refactor_matchgraphcanvas.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/components/organisms/GraphCanvas.tsx`
- Modify: `src/features/job-pipeline/components/MatchGraphCanvas.tsx`

GraphCanvas needs `onConnect` support so MatchGraphCanvas can delegate to it.

- [ ] **Step 1: Add onConnect to GraphCanvas interface and wiring**

In `GraphCanvas.tsx`, add to Props:
```ts
onConnect?: (connection: { source: string; target: string }) => void;
```
And add to ReactFlow props:
```tsx
import { addEdge, type Connection } from '@xyflow/react';
// ...
onConnect={onConnect ? (conn: Connection) => {
  if (conn.source && conn.target) onConnect({ source: conn.source, target: conn.target });
} : undefined}
```

- [ ] **Step 2: Refactor MatchGraphCanvas to use GraphCanvas**

MatchGraphCanvas delegates node/edge data transformation and layout to GraphCanvas, but passes its custom nodeTypes/edgeTypes and uses GraphCanvas's onConnect.

```tsx
import { useMemo } from 'react';
import { GraphCanvas } from '../../../components/organisms/GraphCanvas';
import { RequirementNode } from './RequirementNode';
import { ProfileNode } from './ProfileNode';
import { EdgeScoreBadge } from './EdgeScoreBadge';
import type { GraphNode, GraphEdge } from '../../../types/api.types';

const MATCH_NODE_TYPES = { requirement: RequirementNode, profile: ProfileNode };
const MATCH_EDGE_TYPES = { scoreEdge: EdgeScoreBadge };

interface Props {
  graphNodes: GraphNode[];
  graphEdges: GraphEdge[];
  onNodeClick: (node: GraphNode) => void;
  onEdgeClick: (edge: GraphEdge) => void;
  onAddEdge: (connection: { source: string; target: string }) => void;
  searchQuery: string;
  focusedNodeId: string | null;
}

export function MatchGraphCanvas({
  graphNodes, graphEdges, onNodeClick, onEdgeClick, onAddEdge, searchQuery, focusedNodeId,
}: Props) {
  const reqScores = useMemo(() => {
    const scores: Record<string, number> = {};
    graphEdges.forEach(e => {
      const s = e.score ?? 0;
      if (!scores[e.target] || s > scores[e.target]) scores[e.target] = s;
    });
    return scores;
  }, [graphEdges]);

  const nodes = useMemo(() => {
    const q = searchQuery.toLowerCase();
    return graphNodes.map(n => {
      const dimmed = q.length > 0 && !n.label.toLowerCase().includes(q);
      const highlighted = (q.length > 0 && n.label.toLowerCase().includes(q)) || focusedNodeId === n.id;
      return {
        id: n.id,
        label: n.label,
        type: n.kind === 'requirement' ? 'requirement' : 'profile',
        data: {
          score: n.kind === 'requirement' ? (reqScores[n.id] ?? 0) : undefined,
          dimmed,
          highlighted,
        },
      };
    });
  }, [graphNodes, reqScores, searchQuery, focusedNodeId]);

  const edges = useMemo(() => graphEdges.map((e, i) => ({
    id: `edge-${i}`,
    source: e.source,
    target: e.target,
    score: e.score,
    data: { score: e.score, reasoning: e.reasoning, edgeType: 'llm' as const },
  })), [graphEdges]);

  return (
    <GraphCanvas
      nodes={nodes}
      edges={edges}
      nodeTypes={MATCH_NODE_TYPES}
      edgeTypes={MATCH_EDGE_TYPES}
      layout="LR"
      direction="LR"
      showControls={true}
      onNodeClick={node => {
        const gn = graphNodes.find(n => n.id === node.id);
        if (gn) onNodeClick(gn);
      }}
      onEdgeClick={edge => {
        const ge = graphEdges.find((_, i) => `edge-${i}` === edge.id);
        if (ge) onEdgeClick(ge);
      }}
      onConnect={onAddEdge}
    />
  );
}
```

- [ ] **Step 3: Verify build**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/components/organisms/GraphCanvas.tsx \
        apps/review-workbench/src/features/job-pipeline/components/MatchGraphCanvas.tsx
git commit -m "refactor(ui): MatchGraphCanvas uses GraphCanvas organism (B3)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.