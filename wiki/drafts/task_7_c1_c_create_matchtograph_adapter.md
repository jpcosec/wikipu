---
identity:
  node_id: "doc:wiki/drafts/task_7_c1_c_create_matchtograph_adapter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Convert `MatchViewData` to the 2-column grouped KnowledgeGraph layout.

## Details

Convert `MatchViewData` to the 2-column grouped KnowledgeGraph layout.

**Files:**
- Create: `apps/review-workbench/src/features/job-pipeline/lib/matchToGraph.ts`

- [ ] **Step 1: Create the adapter**

```ts
// apps/review-workbench/src/features/job-pipeline/lib/matchToGraph.ts
import type { MatchViewData, GraphNode as ApiGraphNode, GraphEdge as ApiGraphEdge } from '../../../types/api.types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

export interface MatchEdits {
  addedEdges:   Array<{ source: string; target: string }>;
  removedEdges: Array<{ id: string }>;
  addedNodes:   Array<{ id: string; label: string; kind: 'profile'; category: string }>;
}

const LEFT_X = 0;
const RIGHT_X = 700;
const GROUP_WIDTH = 380;
const GROUP_HEADER = 40;
const ITEM_HEIGHT = 56;
const GROUP_GAP = 20;
const ITEM_PADDING = 8;

function groupByCategory(nodes: ApiGraphNode[]): Map<string, ApiGraphNode[]> {
  const map = new Map<string, ApiGraphNode[]>();
  for (const node of nodes) {
    const cat = node.category ?? 'general';
    const arr = map.get(cat) ?? [];
    arr.push(node);
    map.set(cat, arr);
  }
  return map;
}

export function matchPayloadToGraph(data: MatchViewData): { nodes: SimpleNode[]; edges: SimpleEdge[] } {
  const nodes: SimpleNode[] = [];
  const edges: SimpleEdge[] = [];

  const reqNodes = data.nodes.filter(n => n.kind === 'requirement');
  const profNodes = data.nodes.filter(n => n.kind === 'profile');

  const reqByCategory = groupByCategory(reqNodes);
  const profByCategory = groupByCategory(profNodes);

  // Build requirement groups (left column)
  let leftY = 0;
  for (const [cat, items] of reqByCategory) {
    const groupId = `req-group:${cat}`;
    const groupHeight = GROUP_HEADER + items.length * ITEM_HEIGHT + ITEM_PADDING;

    nodes.push({
      id: groupId,
      type: 'group',
      position: { x: LEFT_X, y: leftY },
      style: { width: GROUP_WIDTH, height: groupHeight },
      data: { name: cat, category: 'section', properties: { side: 'requirement' } },
    });

    for (let i = 0; i < items.length; i++) {
      const item = items[i]!;
      nodes.push({
        id: item.id,
        type: 'simple',
        parentId: groupId,
        extent: 'parent',
        position: { x: ITEM_PADDING, y: GROUP_HEADER + i * ITEM_HEIGHT },
        data: {
          name: item.label,
          category: 'entry',
          properties: { priority: item.priority ?? '', kind: 'requirement' },
          meta: { originalId: item.id, kind: 'requirement', category: cat },
        },
      });
    }

    leftY += groupHeight + GROUP_GAP;
  }

  // Build profile groups (right column)
  let rightY = 0;
  for (const [cat, items] of profByCategory) {
    const groupId = `prof-group:${cat}`;
    const groupHeight = GROUP_HEADER + items.length * ITEM_HEIGHT + ITEM_PADDING;

    nodes.push({
      id: groupId,
      type: 'group',
      position: { x: RIGHT_X, y: rightY },
      style: { width: GROUP_WIDTH, height: groupHeight },
      data: { name: cat, category: 'section', properties: { side: 'profile' } },
    });

    for (let i = 0; i < items.length; i++) {
      const item = items[i]!;
      nodes.push({
        id: item.id,
        type: 'simple',
        parentId: groupId,
        extent: 'parent',
        position: { x: ITEM_PADDING, y: GROUP_HEADER + i * ITEM_HEIGHT },
        data: {
          name: item.label,
          category: 'skill',
          properties: { score: String(item.score ?? ''), kind: 'profile' },
          meta: { originalId: item.id, kind: 'profile', category: cat },
        },
      });
    }

    rightY += groupHeight + GROUP_GAP;
  }

  // Edges
  for (const edge of data.edges) {
    edges.push({
      id: `match:${edge.source}->${edge.target}`,
      source: edge.source,
      target: edge.target,
      type: 'subflow',
      label: edge.score != null ? String(Math.round(edge.score * 100)) + '%' : undefined,
      data: {
        relationType: 'matched_by',
        properties: {
          score: String(edge.score ?? ''),
          reasoning: edge.reasoning ?? '',
        },
      },
    });
  }

  return { nodes, edges };
}

export function graphToMatchEdits(
  original: MatchViewData,
  nodes: SimpleNode[],
  edges: SimpleEdge[],
): MatchEdits {
  const originalEdgeIds = new Set(
    original.edges.map(e => `${e.source}->${e.target}`)
  );
  const currentEdgeIds = new Set(
    edges
      .filter(e => e.data?.relationType === 'matched_by')
      .map(e => `${e.source}->${e.target}`)
  );
  const originalNodeIds = new Set(original.nodes.map(n => n.id));

  const addedEdges = edges
    .filter(e => e.data?.relationType === 'matched_by' && !originalEdgeIds.has(`${e.source}->${e.target}`))
    .map(e => ({ source: e.source, target: e.target }));

  const removedEdges = original.edges
    .filter(e => !currentEdgeIds.has(`${e.source}->${e.target}`))
    .map(e => ({ id: `match:${e.source}->${e.target}` }));

  const addedNodes = nodes
    .filter(n => n.data.properties['kind'] === 'profile' && !originalNodeIds.has(n.id))
    .map(n => ({
      id: n.id,
      label: n.data.name,
      kind: 'profile' as const,
      category: n.data.meta
        ? (n.data.meta as { category: string }).category
        : 'general',
    }));

  return { addedEdges, removedEdges, addedNodes };
}
```

- [ ] **Step 2: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | grep -E "error" | head -20
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/job-pipeline/lib/matchToGraph.ts
git commit -m "feat(ui): add matchToGraph adapter with MatchEdits type (C1-C)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.