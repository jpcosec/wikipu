# Piece: NodeTypeRegistry + register-defaults

**Source:** `node-editor` branch

---

## Where it goes

```
apps/review-workbench/src/schema/
  registry.types.ts       ← NodeTypeDefinition interface
  registry.ts             ← NodeTypeRegistry class + singleton
  register-defaults.ts    ← built-in type registrations (group, simple, entity, …)
```

---

## What does it solve

Currently there is no shared node type system. Each canvas hardcodes its node types as
a `const nodeTypes = { ... }` object and each node component is a one-off file. Adding
a new node type means editing both the canvas and creating a new component file with no
shared contract.

The registry solves:
- **Type safety** — each type declares a Zod `payloadSchema`; `registry.validatePayload()`
  catches malformed data before it reaches the renderer.
- **L2 agnosticism** — `NodeShell` looks up the renderer by `typeId` string; no
  `if (type === 'skill')` in canvas code.
- **`canConnect`** — each type declares `allowedConnections: string[]`; the canvas can
  validate new edges before creating them.
- **Zoom renderers** — each type has three renderers (`dot`, `label`, `detail`) for the
  three zoom tiers. The registry is the single place to change what a node type looks like.
- **FallbackNode contract** — unknown `typeId` → `registry.get()` returns `undefined`;
  `NodeShell` renders a raw debug card instead of crashing.

---

## How we have it implemented

No registry exists. Node types are:
- Registered per-canvas as plain objects (`const nodeTypes = { entry: EntryNode, ... }`).
- No validation.
- No zoom tiers (each component handles its own rendering unconditionally).
- No `canConnect` logic.
- Unknown types crash with a ReactFlow warning.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `NodeShell.tsx` | Must be present — reads from `registry` |
| `GroupShell.tsx` | Optionally reads `registry.get('group')` for label |
| `GraphEditorPage.tsx` (L1) | Calls `registry.register()` for domain-specific types on load |
| `CvGraphCanvas.tsx` | `EntryNode`, `SkillBallNode` become `detail` renderers registered for `'entry'` and `'skill'` types |
| `MatchGraphCanvas.tsx` | `RequirementNode`, `ProfileNode` become `detail` renderers for `'requirement'` and `'profile'` |
| `schema-to-graph.ts` / `cvToGraph.ts` | Must output `data.typeId` matching a registered type |

---

## Concrete code pieces + source

### `registry.types.ts` — NodeTypeDefinition

```ts
export interface NodeTypeDefinition {
  typeId: string;
  label: string;
  icon: string;
  category: string;
  colorToken: string;                          // CSS token for border/dot colour
  payloadSchema: z.ZodSchema;                  // validates data.payload
  sanitizer?: (payload: unknown) => unknown;   // optional normaliser before render
  renderers: {
    dot:    ComponentType<{ colorToken: string }>;
    label:  ComponentType<{ title: string; icon: string }>;
    detail: ComponentType<Record<string, unknown>>;
  };
  defaultSize: { width: number; height: number };
  allowedConnections: string[];                // typeIds this node may connect to
}
```

### `registry.ts` — class + singleton

```ts
export class NodeTypeRegistry {
  private readonly types = new Map<string, NodeTypeDefinition>();

  register(definition: NodeTypeDefinition): void { ... }
  get(typeId: string): NodeTypeDefinition | undefined { ... }
  validatePayload(typeId: string, payload: unknown): z.SafeParseReturnType<...> { ... }
  canConnect(sourceTypeId: string, targetTypeId: string): boolean { ... }
  getAll(): NodeTypeDefinition[] { ... }
}

export const registry = new NodeTypeRegistry(); // singleton
```

### `register-defaults.ts` — built-in types

Registers `group`, `simple`, `entity`, `person`, `skill`, `project`, `publication`,
`concept`, `document`, `section`, `entry` with `PlaceholderDot` / `PlaceholderLabel`
as dot/label renderers and `EntityCard` as the default detail renderer.

```ts
export function registerDefaultNodeTypes(): void {
  defaultNodeTypes.forEach((def) => {
    if (!registry.get(def.typeId)) registry.register(def);
  });
}
```

Called once in `main.tsx` or in the L1 page component before the canvas mounts.

**Full source:** `node-editor:apps/review-workbench/src/schema/`
