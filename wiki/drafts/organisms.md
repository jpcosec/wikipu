---
identity:
  node_id: "doc:wiki/drafts/organisms.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

### `<IntelligentEditor>`

## Details

### `<IntelligentEditor>`

**Path:** `components/organisms/IntelligentEditor.tsx`

**Props:**
```ts
interface IntelligentEditorProps {
  mode: 'fold' | 'tag-hover' | 'diff';
  content: string;
  language?: 'markdown' | 'json';
  onChange?: (value: string) => void;
  readOnly?: boolean;
  highlights?: TextSpan[];
  onSpanHover?: (id: string) => void;
  onSpanClick?: (id: string) => void;
}
```

**Modes:**
| Mode | View | Behavior |
|------|------|----------|
| `fold` | A2 Data Explorer | Read-only, fold JSON keys |
| `tag-hover` | B2 Extract | Tags highlight on hover |
| `diff` | B4 Generate | Show proposed vs approved diff |

---

### `<GraphCanvas>`

**Path:** `components/organisms/GraphCanvas.tsx`

**Props:**
```ts
interface GraphCanvasProps {
  nodes: GraphNode[];
  edges: GraphEdge[];
  onNodeClick?: (node: GraphNode) => void;
  onEdgeClick?: (edge: GraphEdge) => void;
  layout?: 'dagre' | 'manual';
}
```

**Usage:**
```tsx
<GraphCanvas
  nodes={requirementNodes}
  edges={evidenceEdges}
  layout="dagre"
  onNodeClick={(node) => setSelected(node.id)}
/>
```

---

### `<FileTree>`

**Path:** `components/organisms/FileTree.tsx`

**Props:**
```ts
interface FileTreeProps {
  entries: ExplorerEntry[];
  selectedPath?: string;
  onSelect: (path: string) => void;
  onExpand: (path: string) => void;
}
```

**Usage:**
```tsx
<FileTree
  entries={directoryEntries}
  selectedPath={currentPath}
  onSelect={(path) => navigate(path)}
/>
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.