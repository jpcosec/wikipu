---
identity:
  node_id: "doc:wiki/drafts/task_7_readonly_prop_new_category_colors.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`

- [ ] **Step 1: Add new tokens to `CATEGORY_COLORS` (line ~136)**

Add after the existing entries:
```ts
// Schema explorer tokens
root:      { border: 'rgba(255,255,255,0.5)',  bg: 'rgba(255,255,255,0.04)' },
abstract:  { border: 'rgba(116,117,120,0.4)',  bg: 'rgba(116,117,120,0.05)' },
edge_node: { border: 'rgba(255,180,171,0.5)',  bg: 'rgba(255,180,171,0.07)' },
value:     { border: 'rgba(116,117,120,0.3)',  bg: 'rgba(116,117,120,0.03)' },
```

- [ ] **Step 2: Add `readOnly` to `KnowledgeGraphProps` (line ~768)**

```ts
export interface KnowledgeGraphProps {
  initialNodes?: SimpleNode[];
  initialEdges?: SimpleEdge[];
  onSave?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
  onChange?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
  readOnly?: boolean;
}
```

- [ ] **Step 3: Thread `readOnly` through `NodeEditorInner`**

In `function NodeEditorInner({ initialNodes, initialEdges, onSave, onChange }: KnowledgeGraphProps)` (line ~775), add `readOnly = false` to destructuring:

```ts
function NodeEditorInner({ initialNodes, initialEdges, onSave, onChange, readOnly = false }: KnowledgeGraphProps)
```

- [ ] **Step 4: Suppress edit controls when `readOnly`**

All changes are in the JSX returned by `NodeEditorInner`. Apply each gate:

**4a — Save / Discard / Undo toolbar (around line 2133)**
```tsx
{/* gate the entire save/discard/undo row */}
{!readOnly && (
  <>
    <button ... onClick={onSaveWorkspace}>Save workspace</button>
    <button ... onClick={onDiscardWorkspace}>Discard</button>
    <button ... onClick={onUndo}>Undo</button>
    <button ... onClick={onRedo}>Redo</button>
  </>
)}
```

**4b — ReactFlow connection handlers (around line 2422)**
```tsx
onConnect={readOnly ? undefined : onConnect}
onConnectStart={readOnly ? undefined : onConnectStart}
onConnectEnd={readOnly ? undefined : onConnectEnd}
nodesDraggable={!readOnly}
nodesConnectable={!readOnly}
```

**4c — Vacant-node connect buttons (around line 2396)**
```tsx
{!readOnly && vacantCandidateNodes.map((node) => ( ... ))}
```

**4d — Edit node/edge panels (the `editorState === 'edit_node'` and `editorState === 'edit_relation'` blocks)**
```tsx
{!readOnly && editorState === 'edit_node' && ( ... )}
{!readOnly && editorState === 'edit_relation' && ( ... )}
```

- [ ] **Step 5: Verify TypeScript compiles and dev server runs**

```bash
cd apps/review-workbench && npx tsc --noEmit
npm run dev
# Open browser, check /cv still works normally
```

- [ ] **Step 6: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "feat(knowledge-graph): add readOnly prop + schema color tokens"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.