---
identity:
  node_id: "doc:wiki/drafts/concrete_code_pieces_source.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/looting/01-zustand-stores.md", relation_type: "documents"}
---

### `stores/types.ts` (verbatim from node-editor)

## Details

### `stores/types.ts` (verbatim from node-editor)

```ts
export type NodeData = {
  typeId?: string;
  payload?: { typeId?: string; value?: unknown };
  properties?: Record<string, string>;
  visualToken?: string;
  label?: string;
  name?: string;
  [key: string]: unknown;
};

export interface ASTNode {
  id: string;
  type: string;
  position: { x: number; y: number };
  data: NodeData;
  parentId?: string;
  extent?: 'parent' | string;
  style?: React.CSSProperties;
  selected?: boolean;
  hidden?: boolean;
}

export interface ASTEdge {
  id: string;
  source: string;
  target: string;
  type: string;
  data?: {
    relationType: string;
    properties?: Record<string, string>;
    _originalSource?: string;
    _originalTarget?: string;
    _originalRelationType?: string;
  };
  selected?: boolean;
  hidden?: boolean;
}

export type SemanticAction = {
  type: 'CREATE_ELEMENTS' | 'DELETE_ELEMENTS' | 'UPDATE_NODE' | 'UPDATE_EDGE';
  payload: unknown;
  timestamp: number;
  affectedIds: string[];
};
```

### Key `graph-store` API (node-editor: `src/stores/graph-store.ts`)

```ts
interface GraphStore {
  nodes: ASTNode[];
  edges: ASTEdge[];
  undoStack: SemanticAction[];
  redoStack: SemanticAction[];

  isDirty: () => boolean;
  loadGraph: (nodes: ASTNode[], edges: ASTEdge[]) => void;
  markSaved: () => void;

  addElements: (nodes: ASTNode[], edges: ASTEdge[]) => void;
  removeElements: (nodeIds: string[], edgeIds: string[]) => void;
  updateNode: (id: string, patch: Partial<ASTNode>, opts?: { isVisualOnly?: boolean }) => void;
  updateEdge: (id: string, patch: Partial<ASTEdge>, opts?: { isVisualOnly?: boolean }) => void;

  onNodesChange: (changes: NodeChange[]) => void;   // feeds ReactFlow
  onEdgesChange: (changes: EdgeChange[]) => void;
  onConnect: (connection: Connection) => void;

  undo: () => void;
  redo: () => void;
}
```

### Key `ui-store` API (node-editor: `src/stores/ui-store.ts`)

```ts
type EditorState = 'browse' | 'focus' | 'edit_node' | 'edit_relation';

interface UIStore {
  editorState: EditorState;
  focusedNodeId: string | null;
  selectedNode: string | null;
  sidebarOpen: boolean;
  filters: { hiddenRelationTypes: string[]; filterText: string; hideNonNeighbors: boolean };
  deleteConfirmOpen: boolean;
  commandDialogOpen: boolean;

  setEditorState: (s: EditorState) => void;
  setFocusedNode: (id: string | null) => void;
  openDeleteConfirm: (target, nodeIds?, edgeIds?) => void;
  executePendingDelete: (removeFn) => void;
  openCommandDialog: () => void;
}
```

**Full source:** `node-editor:apps/review-workbench/src/stores/`

Generated from `raw/docs_postulador_ui/plan/looting/01-zustand-stores.md`.