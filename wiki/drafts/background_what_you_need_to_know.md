---
identity:
  node_id: "doc:wiki/drafts/background_what_you_need_to_know.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md", relation_type: "documents"}
---

### The prop-threading problem (Task 1)

## Details

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

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-24-d2-group-node-collapse.md`.