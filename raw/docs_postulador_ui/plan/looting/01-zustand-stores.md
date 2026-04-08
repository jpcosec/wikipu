# Piece: Zustand Graph Store + UI Store

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/stores/
  graph-store.ts      ← new
  ui-store.ts         ← new
  types.ts            ← new
```

---

## What does it solve

Our current graph state lives in component-local `useNodesState` / `useEdgesState` hooks
(`CvGraphCanvas`, `MatchGraphCanvas`) and a `KnowledgeGraphContext` that couples data with
ReactFlow internals. Problems:

- No undo/redo — position drags and semantic edits are equally untrackable.
- Collapse/expand state lives inside the canvas component, making it impossible to drive
  from outside (e.g., a sidebar button).
- Multiple components re-read the same state via prop drilling or context re-renders.
- No separation between "visual-only" changes (drag, selection) and "semantic" changes
  (rename, delete, add edge), so a re-layout wipes the undo stack.

The Zustand stores solve all of this by owning graph truth globally with a semantic action
history. `isVisualOnly: true` keeps drag positions and selection out of the undo stack.

---

## How we have it implemented

- `CvGraphCanvas.tsx:15` — `useNodesState` / `useEdgesState` from ReactFlow (ephemeral).
- `pages/global/KnowledgeGraph.tsx` — `SimpleNode[]` / `SimpleEdge[]` state owned by the
  page, passed as props into ReactFlow. No undo. Collapse state is a local `Set<string>`.
- `MatchGraphCanvas.tsx` — nodes/edges derived via `useMemo` on every render from parent
  props; no store at all.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `CvGraphCanvas.tsx` | Replace `useNodesState`/`useEdgesState` with `useGraphStore` selectors |
| `pages/global/KnowledgeGraph.tsx` | Remove node/edge state; read from `graph-store` |
| `MatchGraphCanvas.tsx` | Remove `useMemo` node/edge derivation; use store |
| `BaseCvEditor.tsx` | Call `loadGraph()` on mount instead of passing raw arrays |
| `pages/job/Match.tsx` | Same as BaseCvEditor |
| `features/base-cv/lib/cvToGraph.ts` | Output must match `ASTNode[]` / `ASTEdge[]` |
| `features/job-pipeline/lib/matchToGraph.ts` | Same |

---

## Concrete code pieces + source

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
