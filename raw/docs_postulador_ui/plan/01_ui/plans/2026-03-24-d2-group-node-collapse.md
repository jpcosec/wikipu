# D2 — Group Node Collapse/Expand Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add collapse/expand to `GroupNode` using ReactFlow-native primitives (`NodeToolbar`, `node.hidden`, `useNodeId`, `useReactFlow`, `NodeResizer`) with proxy edges, and remove the prop-threading anti-pattern from `SimpleNodeCard`.

**Architecture:** All changes are in one file (`KnowledgeGraph.tsx`). First, a `KnowledgeGraphContext` replaces the `onEditNode`/`nodeId` fields threaded through `node.data`. Then `GroupNode` is made fully self-contained: it uses `useNodeId()` to know its own ID and `useReactFlow()` to manipulate nodes/edges directly — no callbacks from the parent needed. Child visibility is managed via `node.hidden` / `edge.hidden`. Proxy edges (dashed) are injected on collapse and removed on expand.

**Tech Stack:** `@xyflow/react` (NodeToolbar, NodeResizer, useNodeId, useReactFlow, useStore), React 18, TypeScript, Vitest

---

## File Map

| File | Change |
|---|---|
| `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx` | All implementation changes |
| `apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts` | New — tests for pure helper functions |

---

## Background: What you need to know

### The prop-threading problem (Task 1)

`SimpleNodeCard` (line ~471) currently gets its own node ID and an edit callback via `node.data`:

```ts
// SimpleNodeData interface has these two fields:
nodeId?: string;
onEditNode?: (nodeId: string) => void;
```

These are injected into every node's data in the `displayNodes` useMemo (lines ~1249-1263):

```ts
data: { ...nodeData, nodeId: node.id, onEditNode: openNodeEditor }
```

This means every render of `displayNodes` re-creates the data object and potentially re-renders all nodes. ReactFlow provides `useNodeId()` to get the current node's ID without any prop. A React context replaces `onEditNode`.

### The collapse pattern (Task 2)

`GroupNode` (line ~511) is currently a passive container — dashed border, floating label, no interactivity. It needs to:

1. Know its own ID → `useNodeId()`
2. Access the full node/edge graph → `useReactFlow()` gives `getNodes()`, `getEdges()`, `setNodes()`, `setEdges()`
3. Show a collapse toggle → `NodeToolbar` (renders outside node DOM, zoom-invariant, won't intercept drag)
4. Hide children → `node.hidden = true` on all nodes where `n.parentId === id`
5. Hide child edges → `edge.hidden = true` on edges where either endpoint is a child
6. Show proxy edges → dashed edges from/to the group itself, replacing the hidden child edges
7. Resize automatically → `NodeResizer` inside group

### Proxy edge deduplication

When a group has 3 children each connected to node X, collapsing creates 3 edges from the group to X. We deduplicate by `source+target` pair, keeping the first.

---

## Task 1: `KnowledgeGraphContext` + remove prop threading from `SimpleNodeCard`

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`
- Create: `apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts`

---

- [ ] **Step 1: Create the test file (it will grow in Task 2)**

Create `apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts`:

```ts
import { describe, test, expect } from 'vitest';

// Placeholder — deduplicateByEndpoints will be imported once exported in Task 2
describe('KnowledgeGraph helpers (placeholder)', () => {
  test('test suite boots', () => {
    expect(true).toBe(true);
  });
});
```

- [ ] **Step 2: Run the test to confirm the suite boots**

```bash
cd apps/review-workbench && npm test -- --run KnowledgeGraph.test
```

Expected: `1 test passed`

- [ ] **Step 3: Add `collapsed?: boolean` to `SimpleNodeData`, remove the prop-threading fields**

In `KnowledgeGraph.tsx`, find the `SimpleNodeData` interface (~line 34). Make these changes:

**Remove:**
```ts
nodeId?: string;
onEditNode?: (nodeId: string) => void;
```

**Add (after `meta?: unknown;`):**
```ts
collapsed?: boolean;
```

- [ ] **Step 4: Add `KnowledgeGraphContext` after the `SimpleNodeData` interface**

After the closing `}` of `SimpleNodeData`, add:

```ts
interface KnowledgeGraphCtx {
  openNodeEditor: (nodeId: string) => void;
}
const KnowledgeGraphContext = createContext<KnowledgeGraphCtx>({
  openNodeEditor: () => {},
});
```

- [ ] **Step 5: Update the React named imports to include `createContext` and `useContext`**

Line 1 currently reads:
```ts
import { memo, useCallback, useEffect, useMemo, useRef, useState } from "react";
```

Change to:
```ts
import { createContext, memo, useCallback, useContext, useEffect, useMemo, useRef, useState } from "react";
```

- [ ] **Step 6: Add `useNodeId` to the `@xyflow/react` imports**

Find the `@xyflow/react` import block (~line 3). Add `useNodeId` to the named imports list.

- [ ] **Step 7: Refactor `SimpleNodeCard` to use `useNodeId()` + context**

Find `SimpleNodeCard` (~line 471). Replace the entire component body:

```tsx
const SimpleNodeCard = memo(function SimpleNodeCard({ data, selected }: NodeProps<SimpleNode>) {
  const nodeData = data as unknown as SimpleNodeData;
  const id = useNodeId();
  const { openNodeEditor } = useContext(KnowledgeGraphContext);
  const color = CATEGORY_COLORS[nodeData.category] ?? { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' };
  return (
    <div
      className={cn(
        "group border-2 border-outline-variant rounded-[10px] px-4 py-2.5 text-[0.83rem] font-medium text-center min-w-[110px] relative",
        selected && "ring-2 ring-primary/40",
      )}
      style={{ borderLeft: `4px solid ${color.border}`, background: color.bg, color: '#e2e2e5' }}
      title={tooltipFromProperties(nodeData.properties)}
    >
      <Handle id="top" type="source" position={Position.Top} className="opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity" />
      <Handle id="right" type="source" position={Position.Right} className="opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity" />
      <Handle id="bottom" type="source" position={Position.Bottom} className="opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity" />
      <Handle id="left" type="source" position={Position.Left} className="opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity" />
      <span>{nodeData.name}</span>
      <button
        type="button"
        className={cn(
          "absolute -top-2 -right-2 text-[0.65rem] bg-surface border border-outline-variant px-1 py-0.5 transition-opacity",
          selected ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto",
        )}
        onMouseDown={(e) => e.stopPropagation()}
        onClick={(e) => {
          e.stopPropagation();
          if (id) openNodeEditor(id);
        }}
      >
        Edit
      </button>
    </div>
  );
});
```

- [ ] **Step 8: Remove `nodeId` and `onEditNode` injection from `displayNodes`**

In the `displayNodes` useMemo (~line 1227), there are two `.map()` branches that inject `nodeId: node.id` and `onEditNode: openNodeEditor` into `data`. Remove those two fields from both branches.

The branches look like:
```ts
data: {
  ...nodeData,
  nodeId: node.id,        // ← remove this line
  onEditNode: openNodeEditor,  // ← remove this line
},
```

Do this in both the `inFocusModes` branch and the non-focus branch.

Also remove `openNodeEditor` from the `displayNodes` dependency array (it's no longer used there).

- [ ] **Step 9: Wrap `NodeEditorInner` return JSX with the context provider**

In `NodeEditorInner`'s return statement, wrap the outermost `<div>` with:

```tsx
<KnowledgeGraphContext.Provider value={{ openNodeEditor }}>
  {/* existing outer div and all children */}
</KnowledgeGraphContext.Provider>
```

- [ ] **Step 10: Type-check**

```bash
cd apps/review-workbench && npx tsc --noEmit
```

Expected: 0 errors

- [ ] **Step 11: Run tests**

```bash
cd apps/review-workbench && npm test -- --run
```

Expected: all tests pass

- [ ] **Step 12: Manual smoke test — Edit button still works**

```bash
cd apps/review-workbench && npm run dev
```

Navigate to `http://localhost:5173/graph`. Click a node. Verify the Edit button appears and opens the edit panel in the sidebar. The node name/properties should be editable as before.

- [ ] **Step 13: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx apps/review-workbench/src/pages/global/KnowledgeGraph.test.ts
git commit -m "refactor(graph): remove prop threading from SimpleNodeCard — KnowledgeGraphContext + useNodeId"
```

---

## Task 2: `GroupNode` collapse/expand

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

## Task 3: Changelog + checklist

**Files:**
- Modify: `plan/index_checklist.md`
- Modify: `changelog.md` (worktree root)

---

- [ ] **Step 1: Mark D2 complete in `plan/index_checklist.md`**

Find the D2 entry and mark it `[x]`.

- [ ] **Step 2: Add changelog entry**

In `changelog.md`, add at the top:

```markdown
## [D2] Group Node Collapse/Expand — 2026-03-24

- `GroupNode` now has a `NodeToolbar` (▼/▶) at top-left with child count badge
- Collapsing hides children via `node.hidden` and injects dashed proxy edges
- Expanding restores children and removes proxy edges
- `NodeResizer` inside `GroupNode` — auto-resizes when selected, collapses to 48px height
- `GroupNode` is now self-contained: uses `useNodeId()` + `useReactFlow()`, no parent callbacks
- `SimpleNodeCard` Edit button now uses `KnowledgeGraphContext` + `useNodeId()` — no prop threading
- Removed `nodeId`/`onEditNode` from `SimpleNodeData` interface
- Exported `deduplicateByEndpoints` helper with 4 unit tests
```

- [ ] **Step 3: Commit**

```bash
git add plan/index_checklist.md changelog.md
git commit -m "docs: D2 group node collapse — changelog and checklist"
```
