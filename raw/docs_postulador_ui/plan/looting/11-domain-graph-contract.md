# Piece: DomainGraph — Typed Entry Contract for Translators

**Source:** Prismaliser pattern (external) + node-editor `schema-to-graph.ts`

---

## Where it goes

```
apps/review-workbench/src/features/graph-editor/lib/
  domain-graph.types.ts   ← new: DomainGraph interface
  schema-to-graph.ts      ← adapt to accept DomainGraph (node-editor has a version)
```

---

## What does it solve

`cvToGraph.ts` and `matchToGraph.ts` accept loosely-typed domain objects (raw API
responses, fixture JSON) and produce ReactFlow nodes/edges through implicit assumptions
about field names and shapes. If the API changes a field name, the translator silently
produces wrong output — no TypeScript error, no runtime error, just blank/wrong nodes.

A formal `DomainGraph` interface creates a typed boundary:
- The backend (or mock) contract maps to `DomainGraph` at the API layer.
- The translator is a **pure function**: `(DomainGraph) → { nodes: ASTNode[], edges: ASTEdge[] }`.
- TypeScript enforces the contract at every call site.
- The translator can be unit tested without mounting any component.

This also eliminates hardcoded field lookups (`entry.fields.role`, `e.score`, etc.)
from translator code — all data arrives via the declared `properties` bag.

---

## How we have it implemented

`cvToGraph.ts` — accepts `CvProfileGraphPayload` (a project-specific type) with inline
field access (`entry.fields.role`, `entry.fields.organization`, etc.). Not reusable.

`matchToGraph.ts` — accepts `GraphNode[]` / `GraphEdge[]` from `api.types.ts` directly.
Constructs ReactFlow nodes with `if (n.kind === 'requirement')` branching inside L2.

Neither has unit tests. Neither validates that the data it receives matches expectations.

---

## What will it affect (collateral modifications)

| File | Change needed |
|---|---|
| `api/client.ts` + `mock/client.ts` | Map API responses to `DomainGraph` before returning |
| `features/base-cv/api/useCvProfileGraph.ts` | Return `DomainGraph`, not `CvProfileGraphPayload` |
| `features/job-pipeline/api/useViewMatch.ts` | Return `DomainGraph` for the match graph |
| `features/base-cv/lib/cvToGraph.ts` | Rewrite to accept `DomainGraph`, emit `ASTNode[]` / `ASTEdge[]` |
| `features/job-pipeline/lib/matchToGraph.ts` | Same |
| `stores/graph-store.ts` | `loadGraph()` accepts `ASTNode[]` / `ASTEdge[]` (already correct) |
| `BaseCvEditor.tsx` + `Match.tsx` | Pages call translator, pass result to `loadGraph()` |

---

## Concrete code pieces + source

### `domain-graph.types.ts` (to be written, inspired by prismaliser + Chewbacca conversation)

```ts
export interface DomainEntity {
  id: string;
  typeId: string;                           // must match a registered NodeTypeDefinition
  properties: Record<string, string>;       // flat key-value, always strings
  parentId?: string;                        // for group membership
  visualToken?: string;                     // optional colour override
}

export interface DomainRelation {
  id?: string;
  sourceId: string;
  targetId: string;
  label?: string;                           // becomes edge relationType
  properties?: Record<string, string>;
}

export interface DomainSchema {
  [typeId: string]: {
    label: string;
    icon?: string;
    colorToken?: string;
    l3ComponentId?: string;                 // hint for which L3 renderer to use
  };
}

export interface DomainGraph {
  entities: DomainEntity[];
  relations: DomainRelation[];
  schema?: DomainSchema;                    // optional: overrides registry defaults
}
```

### Translator signature (pure function contract)

```ts
// schema-to-graph.ts
export function domainGraphToAst(
  input: DomainGraph,
): { nodes: ASTNode[]; edges: ASTEdge[]; errors: ValidationError[] } {
  // 1. For each entity: look up typeId in registry, build ASTNode
  // 2. For each relation: build ASTEdge
  // 3. Collect validation errors for unknown typeIds (produce FallbackNode data)
  // Never throws — errors go into the errors array
}
```

### node-editor reference (starting point to adapt)

`node-editor:apps/review-workbench/src/features/graph-editor/lib/schema-to-graph.ts`
already does steps 1–3 for the node-editor's internal `RawData` format. The main
adaptation is replacing `RawData` with `DomainGraph` at the entry point.

**External reference:** prismaliser `src/lib/layout.ts` + schema transform pattern
(schema → Prisma ERD nodes/edges, same structural idea).
