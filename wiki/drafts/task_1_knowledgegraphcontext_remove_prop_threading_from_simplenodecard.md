---
identity:
  node_id: "doc:wiki/drafts/task_1_knowledgegraphcontext_remove_prop_threading_from_simplenodecard.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md", relation_type: "documents"}
---

**Files:**

## Details

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

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md`.