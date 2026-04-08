---
identity:
  node_id: "doc:wiki/drafts/task_3_add_groupnode_subflowedge_initialnodes_onsave_props.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Add the `GroupNode` type (resizable parent container), `SubFlowEdge` (resolves absolute child positions), and wire up `initialNodes`/`initialEdges`/`onSave` props so KnowledgeGraph can be used as an embedded editor.

## Details

Add the `GroupNode` type (resizable parent container), `SubFlowEdge` (resolves absolute child positions), and wire up `initialNodes`/`initialEdges`/`onSave` props so KnowledgeGraph can be used as an embedded editor.

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`

- [ ] **Step 1: Add GroupNode component**

After the `SimpleNodeCard` component definition and before `const nodeTypes`, add:

```tsx
const GroupNode = memo(function GroupNode({ data, selected }: NodeProps<SimpleNode>) {
  const nodeData = data as unknown as SimpleNodeData;
  const color = CATEGORY_COLORS[nodeData.category] ?? { border: 'rgba(116,117,120,0.4)', bg: 'rgba(30,32,34,0.9)' };
  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        border: `2px dashed ${color.border}`,
        background: color.bg,
        borderRadius: 8,
        position: 'relative',
      }}
    >
      <Handle id="top" type="source" position={Position.Top} className="ne-node-handle" />
      <Handle id="right" type="source" position={Position.Right} className="ne-node-handle" />
      <Handle id="bottom" type="source" position={Position.Bottom} className="ne-node-handle" />
      <Handle id="left" type="source" position={Position.Left} className="ne-node-handle" />
      <div
        style={{
          position: 'absolute',
          top: -20,
          left: 0,
          fontSize: '0.72rem',
          fontWeight: 600,
          color: color.border,
          fontFamily: 'JetBrains Mono, monospace',
          textTransform: 'uppercase',
          letterSpacing: '0.08em',
          whiteSpace: 'nowrap',
        }}
      >
        {nodeData.name}
      </div>
    </div>
  );
});
```

- [ ] **Step 2: Add SubFlowEdge component**

After `GroupNode`, before `const nodeTypes`:

```tsx
const SubFlowEdge = memo(function SubFlowEdge({ id, source, target, style, markerEnd }: EdgeProps) {
  const sourceNode = useStore((store) => store.nodeLookup.get(source));
  const targetNode = useStore((store) => store.nodeLookup.get(target));

  if (!sourceNode || !targetNode) return null;

  // Resolve absolute positions (child nodes store position relative to parent)
  const getAbsPos = (node: InternalNode) => {
    if (node.parentId) {
      const parent = useStore.getState?.().nodeLookup.get(node.parentId);
      if (parent) {
        return {
          x: (parent.internals?.positionAbsolute?.x ?? 0) + node.position.x,
          y: (parent.internals?.positionAbsolute?.y ?? 0) + node.position.y,
        };
      }
    }
    return node.internals.positionAbsolute;
  };

  const srcAbs = getAbsPos(sourceNode);
  const tgtAbs = getAbsPos(targetNode);

  // Use same floating edge math as FloatingEdge
  const params = getFloatingEdgeParams(
    { ...sourceNode, internals: { ...sourceNode.internals, positionAbsolute: srcAbs } } as InternalNode,
    { ...targetNode, internals: { ...targetNode.internals, positionAbsolute: tgtAbs } } as InternalNode,
  );
  const [path] = getBezierPath({
    sourceX: params.sx,
    sourceY: params.sy,
    sourcePosition: params.sourcePosition,
    targetX: params.tx,
    targetY: params.ty,
    targetPosition: params.targetPosition,
  });

  return (
    <BaseEdge
      id={id}
      path={path}
      style={{ stroke: 'var(--line)', strokeWidth: 1.5, ...style }}
      markerEnd={markerEnd}
    />
  );
});
```

**Note:** `useStore.getState` is not part of the ReactFlow hook API. Use the store hook pattern from `FloatingEdge` instead — both `sourceNode` and `targetNode` already carry `internals.positionAbsolute` which ReactFlow resolves to canvas-absolute for all nodes (including children). So the simpler approach is:

```tsx
const SubFlowEdge = memo(function SubFlowEdge({ id, source, target, style, markerEnd }: EdgeProps) {
  const sourceNode = useStore((store) => store.nodeLookup.get(source));
  const targetNode = useStore((store) => store.nodeLookup.get(target));

  if (!sourceNode || !targetNode) return null;

  // ReactFlow stores positionAbsolute (canvas coords) for all nodes including children
  const params = getFloatingEdgeParams(sourceNode, targetNode);
  const [path] = getBezierPath({
    sourceX: params.sx,
    sourceY: params.sy,
    sourcePosition: params.sourcePosition,
    targetX: params.tx,
    targetY: params.ty,
    targetPosition: params.targetPosition,
  });

  return (
    <BaseEdge
      id={id}
      path={path}
      style={{ stroke: 'var(--line)', strokeWidth: 1.5, ...style }}
      markerEnd={markerEnd}
    />
  );
});
```

- [ ] **Step 3: Register GroupNode in nodeTypes and SubFlowEdge in edgeTypes**

Find:
```ts
const nodeTypes: NodeTypes = {
  simple: SimpleNodeCard,
};
```
Replace with:
```ts
const nodeTypes: NodeTypes = {
  simple: SimpleNodeCard,
  group: GroupNode,
};
```

Find the `edgeTypes` definition (search for `edgeTypes`) and add `subflow: SubFlowEdge`. If it doesn't exist yet, add after `nodeTypes`:
```ts
const edgeTypes = {
  floating: FloatingEdge,
  subflow: SubFlowEdge,
};
```
Then pass `edgeTypes={edgeTypes}` to the `<ReactFlow>` component (look for where `FloatingEdge` is passed).

- [ ] **Step 4: Add initialNodes/initialEdges/onSave props to KnowledgeGraph**

Find the `KnowledgeGraph` function signature (search for `export function KnowledgeGraph` or `function KnowledgeGraph`). Add props:

```tsx
interface KnowledgeGraphProps {
  initialNodes?: SimpleNode[];
  initialEdges?: SimpleEdge[];
  onSave?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
}

function KnowledgeGraphInner({ initialNodes, initialEdges, onSave }: KnowledgeGraphProps) {
```

Inside the component, find where `buildInitialGraph()` is called (typically in a `useState` initializer). Change it to use the prop when provided:

```ts
const [nodes, setNodes, onNodesChange] = useNodesState(
  initialNodes ?? buildInitialGraph().nodes
);
const [edges, setEdges, onEdgesChange] = useEdgesState(
  initialEdges ?? buildInitialGraph().edges
);
```

- [ ] **Step 5: Wire onSave to sidebar Save button**

Find the sidebar in KnowledgeGraph. Search for a Save button or Ctrl+S handler. In the Actions section, add a Save button that calls `onSave?.(nodes, edges)` when `onSave` is present:

In the keyboard shortcut handler (search for `ctrlKey && key === 's'`), after the existing logic, add:
```ts
if (e.ctrlKey && e.key === 's' && onSave) {
  e.preventDefault();
  onSave(nodes, edges);
}
```

In the sidebar Actions section, conditionally render:
```tsx
{onSave && (
  <button className="ne-btn ne-btn-primary" onClick={() => onSave(nodes, edges)}>
    Save
  </button>
)}
```

- [ ] **Step 6: Add Document template expansion logic**

Find where template nodes are created (search for `NODE_TEMPLATES` usage in the drop handler — likely `onDrop` or a drag-from-template handler). When the dropped template has `category === 'document'`, instead of creating one node, create the 3-level structure:

```ts
if (template.category === 'document') {
  const docId = createEntityId('doc');
  const sec1Id = createEntityId('sec');
  const sec2Id = createEntityId('sec');
  const ent1Id = createEntityId('entry');
  const ent2Id = createEntityId('entry');

  const newNodes: SimpleNode[] = [
    {
      id: docId,
      type: 'group',
      position: dropPosition,
      style: { width: 600, height: 400 },
      data: { name: 'Untitled CV', category: 'document', properties: { type: 'cv' } },
    },
    {
      id: sec1Id,
      type: 'group',
      parentId: docId,
      extent: 'parent',
      position: { x: 20, y: 60 },
      style: { width: 560, height: 160 },
      data: { name: 'Introduction', category: 'section', properties: {} },
    },
    {
      id: sec2Id,
      type: 'group',
      parentId: docId,
      extent: 'parent',
      position: { x: 20, y: 240 },
      style: { width: 560, height: 140 },
      data: { name: 'Body', category: 'section', properties: {} },
    },
    {
      id: ent1Id,
      type: 'simple',
      parentId: sec1Id,
      extent: 'parent',
      position: { x: 20, y: 50 },
      data: { name: 'Entry 1', category: 'entry', properties: { date: '' } },
    },
    {
      id: ent2Id,
      type: 'simple',
      parentId: sec2Id,
      extent: 'parent',
      position: { x: 20, y: 50 },
      data: { name: 'Entry 2', category: 'entry', properties: { date: '' } },
    },
  ];
  setNodes(prev => [...prev, ...newNodes]);
  return;
}
```

- [ ] **Step 7: Verify build**

```bash
cd apps/review-workbench && npm run build 2>&1 | tail -5
```

- [ ] **Step 8: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "feat(ui): add GroupNode, SubFlowEdge, Document template, initialNodes/onSave props to KnowledgeGraph"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.