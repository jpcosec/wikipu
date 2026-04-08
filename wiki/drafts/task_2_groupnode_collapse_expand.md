---
identity:
  node_id: "doc:wiki/drafts/task_2_groupnode_collapse_expand.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts`

---

- [ ] **Step 1: Write failing tests for `deduplicateByEndpoints`**

Update `KnowledgeGraph.test.ts`. Replace the placeholder with:

```ts
import { describe, test, expect } from 'vitest';
import { deduplicateByEndpoints } from './KnowledgeGraph';

describe('deduplicateByEndpoints', () => {
  test('removes duplicate source+target pairs, keeps first', () => {
    const edges = [
      { id: 'e1', source: 'a', target: 'b' },
      { id: 'e2', source: 'a', target: 'b' }, // duplicate — dropped
      { id: 'e3', source: 'a', target: 'c' },
    ];
    const result = deduplicateByEndpoints(edges);
    expect(result).toHaveLength(2);
    expect(result.map(e => e.id)).toEqual(['e1', 'e3']);
  });

  test('keeps all edges when no duplicates', () => {
    const edges = [
      { id: 'e1', source: 'a', target: 'b' },
      { id: 'e2', source: 'b', target: 'c' },
      { id: 'e3', source: 'c', target: 'a' },
    ];
    expect(deduplicateByEndpoints(edges)).toHaveLength(3);
  });

  test('direction is significant — a→b and b→a are not duplicates', () => {
    const edges = [
      { id: 'e1', source: 'a', target: 'b' },
      { id: 'e2', source: 'b', target: 'a' },
    ];
    expect(deduplicateByEndpoints(edges)).toHaveLength(2);
  });

  test('returns empty array for empty input', () => {
    expect(deduplicateByEndpoints([])).toEqual([]);
  });
});
```

- [ ] **Step 2: Run tests — expect failure on import**

```bash
cd apps/review-workbench && npm test -- --run KnowledgeGraph.test
```

Expected: FAIL — `deduplicateByEndpoints` is not exported yet.

- [ ] **Step 3: Export `deduplicateByEndpoints` helper in `KnowledgeGraph.tsx`**

Add this function just before the `GroupNode` component definition (~line 511):

```ts
export function deduplicateByEndpoints<T extends { source: string; target: string }>(edges: T[]): T[] {
  const seen = new Set<string>();
  return edges.filter((e) => {
    const key = `${e.source}→${e.target}`;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}
```

- [ ] **Step 4: Run tests — expect pass**

```bash
cd apps/review-workbench && npm test -- --run KnowledgeGraph.test
```

Expected: 4 tests pass.

- [ ] **Step 5: Add `NodeToolbar` and `NodeResizer` to the `@xyflow/react` imports**

Add `NodeToolbar` and `NodeResizer` to the named imports from `@xyflow/react`.

- [ ] **Step 6: Replace the `GroupNode` component**

Replace the entire `GroupNode` component (~line 511–549) with:

```tsx
const GroupNode = memo(function GroupNode({ data, selected }: NodeProps<SimpleNode>) {
  const nodeData = data as unknown as SimpleNodeData;
  const id = useNodeId()!;
  const { setNodes, setEdges, getNodes, getEdges } = useReactFlow();
  const collapsed = nodeData.collapsed ?? false;
  const color = CATEGORY_COLORS[nodeData.category] ?? { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' };

  // Reactive child count — useStore gives live updates when nodes change.
  // In @xyflow/react v12, nodeLookup values are InternalNode which extends Node and carries parentId.
  // If you get a type error, cast: (n as unknown as SimpleNode).parentId
  const childCount = useStore(
    useCallback((s) => [...s.nodeLookup.values()].filter((n) => (n as unknown as SimpleNode).parentId === id).length, [id])
  );

  const toggleCollapse = useCallback(() => {
    // Read live collapsed state from getNodes() — avoids stale closure bug on rapid clicks
    const currentNode = getNodes().find((n) => n.id === id);
    const currentCollapsed = (currentNode?.data as SimpleNodeData | undefined)?.collapsed ?? false;
    const next = !currentCollapsed;
    const childIds = new Set(getNodes().filter((n) => n.parentId === id).map((n) => n.id));

    if (next) {
      // Collapsing: hide child edges, inject deduplicated proxy edges
      const proxyEdges = deduplicateByEndpoints(
        getEdges()
          .filter((e) => childIds.has(e.source) || childIds.has(e.target))
          .map((e) => ({
            ...e,
            id: `proxy:${id}:${e.id}`,
            source: childIds.has(e.source) ? id : e.source,
            target: childIds.has(e.target) ? id : e.target,
            data: { ...e.data, relationType: 'proxy' },
            style: { strokeDasharray: '4 3', opacity: 0.5 },
          }))
      ).filter((e) => e.source !== e.target); // drop self-loops

      setEdges((all) => [
        ...all.map((e) =>
          childIds.has(e.source) || childIds.has(e.target) ? { ...e, hidden: true } : e
        ),
        ...proxyEdges,
      ]);
    } else {
      // Expanding: remove proxy edges, restore child edges
      setEdges((all) =>
        all
          .filter((e) => !e.id.startsWith(`proxy:${id}:`))
          .map((e) =>
            childIds.has(e.source) || childIds.has(e.target) ? { ...e, hidden: false } : e
          )
      );
    }

    setNodes((all) =>
      all.map((n) => {
        if (n.parentId === id) return { ...n, hidden: next };
        if (n.id === id) {
          return {
            ...n,
            data: { ...n.data, collapsed: next },
            style: next
              ? { ...n.style, height: 48 }
              : { ...n.style, height: undefined },
          };
        }
        return n;
      })
    );
  }, [id, getNodes, getEdges, setNodes, setEdges]); // `collapsed` intentionally omitted — read live from getNodes()

  return (
    <>
      <NodeToolbar position={Position.Top} align="start" isVisible>
        <div className="flex items-center gap-2 px-2 py-1 bg-surface border border-outline-variant rounded text-[0.7rem]">
          <button
            type="button"
            className="text-primary hover:text-primary-dim transition-colors font-mono leading-none"
            onClick={toggleCollapse}
          >
            {collapsed ? '▶' : '▼'}
          </button>
          <span className="font-semibold text-on-surface font-headline">{nodeData.name}</span>
          <span className="text-on-muted">{childCount} nodes</span>
        </div>
      </NodeToolbar>
      <div
        style={{
          width: '100%',
          height: '100%',
          border: `2px dashed ${color.border}`,
          background: color.bg,
          borderRadius: 8,
          position: 'relative',
          outline: selected ? `2px solid ${color.border}` : undefined,
        }}
      >
        <NodeResizer isVisible={selected && !collapsed} minWidth={160} minHeight={60} />
        <Handle id="top" type="source" position={Position.Top} className="opacity-0 hover:opacity-100 transition-opacity" />
        <Handle id="right" type="source" position={Position.Right} className="opacity-0 hover:opacity-100 transition-opacity" />
        <Handle id="bottom" type="source" position={Position.Bottom} className="opacity-0 hover:opacity-100 transition-opacity" />
        <Handle id="left" type="source" position={Position.Left} className="opacity-0 hover:opacity-100 transition-opacity" />
      </div>
    </>
  );
});
```

- [ ] **Step 7: Type-check**

```bash
cd apps/review-workbench && npx tsc --noEmit
```

Expected: 0 errors. If there are type errors on `n.parentId` (it's on `Node` in newer @xyflow/react versions), cast as needed: `(n as SimpleNode).parentId`.

- [ ] **Step 8: Run all tests**

```bash
cd apps/review-workbench && npm test -- --run
```

Expected: all tests pass (including the 4 new helper tests).

- [ ] **Step 9: Manual smoke test — collapse/expand**

```bash
cd apps/review-workbench && npm run dev
```

On `/graph` or `/cv`, if the initial graph has group nodes with children:
- ▼/▶ toolbar is visible above every group node
- Child count badge shows the correct number
- Click ▼: children disappear, group shrinks to ~48px height, dashed proxy edges appear from the group to external nodes
- Click ▶: children reappear, group expands, proxy edges gone
- `NodeResizer` handles appear on selected non-collapsed groups

If the initial graph has no group nodes, add one manually via the editor (category: `section`, then create child nodes by setting `parentId` in a fixture or via drag).

- [ ] **Step 10: Verify no regressions on `/schema` and `/cv`**

- `/schema`: readOnly mode — no group nodes in the schema view, so no toggle appears. Confirm the page looks unchanged.
- `/cv`: if any group nodes exist, verify the ▼/▶ toggle works — the spec requires collapse to work in **both** readOnly and edit modes. `setNodes`/`setEdges` from `useReactFlow()` are not blocked by `readOnly` (which only gates drag and connection). No extra guard needed.
- `/cv`: check that `SimpleNodeCard` Edit button still works in non-readOnly mode.

- [ ] **Step 11: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts
git commit -m "feat(graph): D2 — GroupNode collapse/expand (NodeToolbar, node.hidden, proxy edges, NodeResizer)"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md`.