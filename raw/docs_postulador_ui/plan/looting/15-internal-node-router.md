# Piece: InternalNodeRouter (L3 Content Dispatch)

**Source:** agentok pattern — `agentok/frontend/src/nodes/index.ts`

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/L3-content/
  registry.ts              ← COMPONENT_REGISTRY: l3ComponentId → React component
  InternalNodeRouter.tsx   ← dispatches to the right L3 component via registry
```

---

## What does it solve

This is distinct from the `NodeTypeRegistry` (piece 07), which handles schema validation
and zoom-level renderers. The `InternalNodeRouter` handles **runtime rendering dispatch**:
given a node's `data.typeId` and `config.l3ComponentId`, it looks up and mounts the
correct content component inside the `NodeShell` wrapper.

Without this, every canvas has its own `nodeTypes = { skill: SkillNode, entry: EntryNode }`
hardcoded mapping. Adding a new node type means editing the canvas file. The router
breaks that coupling:

- Only **one** ReactFlow node type is registered: `internalRouter`.
- All content differentiation happens inside the router, driven by the `COMPONENT_REGISTRY`.
- The `FallbackNode` (piece 12) is the default when no matching component is found.

This is the piece that makes the system truly extensible: adding a `MarkdownNode` is
one line in `registry.ts`, no canvas code changes.

---

## How we have it implemented

`CvGraphCanvas.tsx` registers `{ entry: EntryNode, skill: SkillBallNode, group: GroupNode }`.
`MatchGraphCanvas.tsx` registers `{ requirement: RequirementNode, profile: ProfileNode }`.

Each canvas is a different hardcoded dispatch table. There is no shared router, no
fallback component, and no way to add a new type without touching the canvas file.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `GraphCanvas.tsx` | Register only `{ default: NodeShell, group: GroupShell }` — NodeShell calls InternalNodeRouter internally |
| `NodeShell.tsx` | Instead of calling `registry.get(typeId).renderers.detail`, render `<InternalNodeRouter data={data} />` |
| `L3-content/registry.ts` | One entry per content component (`'cv_entry'` → `EntryCard`, etc.) |
| `cvToGraph.ts` / `matchToGraph.ts` | Must set `data.config.l3ComponentId` on each node |
| `DomainGraph` schema field | `schema[typeId].l3ComponentId` is the registry key (piece 11) |
| `features/base-cv/components/EntryNode.tsx` | Becomes a pure L3 content component, no ReactFlow Handle imports |
| `features/base-cv/components/SkillBallNode.tsx` | Same |
| `features/job-pipeline/components/RequirementNode.tsx` | Same |

---

## Concrete code pieces + source

### `L3-content/registry.ts`

```ts
import type { ComponentType } from 'react';
import { DefaultJsonView } from './DefaultJsonView';

// Add one line per content type — zero changes to canvas code
export const COMPONENT_REGISTRY: Record<string, ComponentType<{ data: unknown; isExpanded?: boolean }>> = {
  cv_entry:       lazy(() => import('./CvEntryCard')),
  cv_skill:       lazy(() => import('./SkillBadge')),
  requirement:    lazy(() => import('./RequirementCard')),
  profile:        lazy(() => import('./ProfileCard')),
  markdown_doc:   lazy(() => import('./MarkdownViewer')),
  json_schema:    lazy(() => import('./SchemaCard')),
  // unknown typeId falls through to DefaultJsonView
};
```

### `InternalNodeRouter.tsx`

```tsx
import { NodeShell } from '../L2-canvas/NodeShell';
import { COMPONENT_REGISTRY } from './registry';
import { DefaultJsonView } from './DefaultJsonView';
import type { NodeProps } from '@xyflow/react';

export function InternalNodeRouter(props: NodeProps) {
  const { typeId, config, props: contentData } = props.data as {
    typeId: string;
    config: { l3ComponentId: string; variant?: 'card' | 'ghost' | 'expanded' };
    props: unknown;
  };

  const ContentComponent = COMPONENT_REGISTRY[config?.l3ComponentId] ?? DefaultJsonView;

  return (
    <NodeShell {...props}>
      <ContentComponent
        data={contentData}
        isExpanded={config?.variant === 'expanded'}
      />
    </NodeShell>
  );
}
```

### `DefaultJsonView.tsx` (FallbackNode content)

```tsx
export function DefaultJsonView({ data }: { data: unknown }) {
  return (
    <pre className="max-h-32 overflow-auto p-2 text-[10px] text-red-400">
      {JSON.stringify(data, null, 2)}
    </pre>
  );
}
```

**Primary source:** `agentok/frontend/src/nodes/index.ts`
— centralised `nodeTypes` map where each entry wraps its content in a shared shell.

**Secondary source:** Arquitecto Técnico Directo conversation, Phase 4.
