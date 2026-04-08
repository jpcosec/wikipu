# Piece: Smart Edges — Dynamic Handles Pointing to Sub-components

**Source:** Dify Workflow Editor — `web/app/components/workflow/nodes/`

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L2-canvas/hooks/
  use-smart-handles.ts    ← measures sub-component positions, returns handle offsets

apps/review-workbench/src/features/graph-editor/L2-canvas/
  NodeShell.tsx           ← renders dynamic handles at computed positions
```

---

## What does it solve

All our current edges connect to a node's center (floating edges, piece 02) or a fixed
top/bottom handle. This is fine for atomic nodes (a person, a skill) but breaks down
for **structured document nodes** where the user needs an edge to connect to a specific
field — e.g., "this edge proves *this specific requirement*" or "this CV entry links to
*this skill slot*".

Dify's LLM nodes expose multiple named handles — one per input/output variable — and
edges connect to the exact handle for that variable. This gives semantic precision to
connections.

The pattern: each L3 content component can declare named connection points via a
`useRegisterHandles` call, and the `NodeShell` renders `<Handle>` elements at the
positions the L3 sub-components report (measured via `useRef` + `getBoundingClientRect`).

**Scope note:** This is an advanced piece, lower priority than pieces 01–12. Most graph
views in the workbench don't need sub-component handles. Implement when the Match graph
needs to link evidence to specific requirement fields, or when the schema explorer needs
field-level connections.

---

## How we have it implemented

Not implemented. All handles are at fixed `Position.Top` / `Position.Bottom`. There is
no mechanism for L3 components to declare connection points.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `NodeShell.tsx` | Replace fixed Handle pair with dynamically-positioned Handle array |
| `FloatingEdge.tsx` (piece 02) | `getEdgeParams` already handles arbitrary positions — no change needed |
| `L3-content/registry.ts` | Each L3 component that wants named handles exports a `handles` config |
| `DomainGraph` schema (piece 11) | `schema[typeId].handles?: Array<{ id: string; label: string; side: 'left'|'right'|'top'|'bottom' }>` |
| `stores/types.ts` | `ASTNode.data` may include `handles: HandleConfig[]` |

---

## Concrete code pieces + source

### Handle registration pattern (Dify-inspired)

```tsx
// In an L3 content component:
export function RequirementCard({ data, onRegisterHandles }) {
  const criteriaRef = useRef<HTMLDivElement>(null);
  const evidenceRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Report sub-element positions upward so NodeShell can place handles
    onRegisterHandles?.([
      { id: 'criteria', ref: criteriaRef, side: 'left' },
      { id: 'evidence', ref: evidenceRef, side: 'right' },
    ]);
  }, []);

  return (
    <div>
      <div ref={criteriaRef}>Criteria</div>
      <div ref={evidenceRef}>Evidence</div>
    </div>
  );
}
```

### `use-smart-handles.ts` — measure and expose handle positions

```ts
export function useSmartHandles(containerRef: RefObject<HTMLDivElement>) {
  const [handles, setHandles] = useState<ResolvedHandle[]>([]);

  const registerHandles = useCallback((declarations: HandleDeclaration[]) => {
    if (!containerRef.current) return;
    const containerRect = containerRef.current.getBoundingClientRect();

    const resolved = declarations.map((decl) => {
      const rect = decl.ref.current?.getBoundingClientRect();
      if (!rect) return null;
      return {
        id: decl.id,
        side: decl.side,
        // Position relative to the node container
        x: rect.left - containerRect.left + rect.width / 2,
        y: rect.top - containerRect.top + rect.height / 2,
      };
    }).filter(Boolean);

    setHandles(resolved as ResolvedHandle[]);
  }, [containerRef]);

  return { handles, registerHandles };
}
```

### NodeShell with dynamic handles

```tsx
// Instead of fixed <Handle type="target" position={Position.Top} />:
{handles.map((h) => (
  <Handle
    key={h.id}
    id={h.id}
    type={h.side === 'left' ? 'target' : 'source'}
    position={h.side === 'left' ? Position.Left : Position.Right}
    style={{ top: h.y, left: h.side === 'left' ? 0 : undefined, right: h.side === 'right' ? 0 : undefined }}
  />
))}
```

**Primary source:** [Dify Workflow Editor](https://github.com/langgenius/dify/tree/main/web/app/components/workflow/nodes)
— specifically how LLM nodes declare multiple source/target handles per input/output
variable and how the edge renderer connects to the correct handle ID.
