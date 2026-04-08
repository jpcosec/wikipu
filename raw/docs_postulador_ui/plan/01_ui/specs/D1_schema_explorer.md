# Spec D1 — Schema Explorer

**Feature:** `src/features/schema-explorer/`
**Page:** `src/pages/global/SchemaExplorer.tsx`
**Route:** `/schema`
**Libraries:** `@xyflow/react` · `@dagrejs/dagre` · `lucide-react`

---

## Purpose

A read-only graph view for exploring the data schemas of any pipeline domain. The operator selects a domain (CV, Job, Match) and sees its structure rendered as a graph — which types are nodes, which are subflow groups, which fields are attributes, what connects to what, and what each color means.

The schema format is a **domain-agnostic view mapping language**: a declarative JSON contract that fully describes how any structured document maps to the graph view, without any hardcoded assumptions about the domain.

---

## Core Concepts

The schema answers five questions for any document:

| Question | Schema key | Graph effect |
|----------|-----------|--------------|
| What kind of document is this? | `document` block | Page title, domain selector label |
| What is a node? | `render_as: "node"` | Rendered as a standalone ReactFlow node |
| What is a subflow (group of nodes)? | `render_as: "group"` | Rendered as a ReactFlow group node with children inside (subflow) |
| What is an attribute? | `render_as: "attribute"` | Shown as a property row in the node inspector, not as a separate node |
| What connects to what? | `edge_types` | Rendered as ReactFlow edges with labels |
| What does colour mean? | `color_token` + `visual_encoding` | Node border/bg color, edge stroke color |

---

## Schema JSON Format

### TypeScript contracts — `src/schemas/types.ts`

```ts
export type RenderAs = "group" | "node" | "attribute";
export type RelationType = "contains" | "extends" | "semantic_edge" | "references";

export interface SchemaAttribute {
  name: string;
  type: string;       // "string" | "boolean" | "number" | "date" | "enum" | "object" | "string[]" | type ref
  required: boolean;
  values?: string[];  // for enum
  note?: string;
}

export interface SchemaChild {
  type: string;       // id of the child node_type
  via: string;        // field name on the parent that holds these children
  group_by?: string;  // if set, children are grouped into sub-subflows by this field value
}

export interface SchemaNodeType {
  id: string;
  label: string;
  render_as: RenderAs;
  color_token: string;      // key into visual_encoding.color_tokens
  abstract?: boolean;       // true → this type has variants; not directly instantiated
  variant_of?: string;      // id of the abstract parent type
  attributes: SchemaAttribute[];
  children?: SchemaChild[];  // only for render_as: "group"
}

export interface SchemaEdgeType {
  id: string;
  label: string;
  from: string;       // SchemaNodeType.id
  to: string;         // SchemaNodeType.id
  color_token: string;
  animated?: boolean;
  cardinality?: string;
  note?: string;
}

export interface ColorToken {
  border: string;
  bg: string;
}

export interface EdgeColorToken {
  stroke: string;
}

export interface VisualEncoding {
  color_tokens: Record<string, ColorToken>;
  edge_color_tokens: Record<string, EdgeColorToken>;
}

export interface DocumentSchema {
  document: {
    id: string;
    label: string;
    version: string;
    description: string;
    root_type: string;  // id of the top-level node_type
  };
  node_types: SchemaNodeType[];
  edge_types: SchemaEdgeType[];
  visual_encoding: VisualEncoding;
}
```

---

### Top-level structure

```json
{
  "document": {
    "id": "cv_profile_graph",
    "label": "CV Profile Graph",
    "version": "1.0",
    "description": "Structured CV with entries grouped by category, connected to skills.",
    "root_type": "CvProfileGraphPayload"
  },
  "node_types": [ ... ],
  "edge_types": [ ... ],
  "visual_encoding": { ... }
}
```

---

### `node_types` — how each type renders

**`render_as: "group"`** — a subflow container. Contains child nodes visually nested inside it.
Children are declared in `children[]`. Supports `group_by` to create sub-subflows per field value
(e.g., group entries by `category` to create section subflows).

```json
{
  "id": "CvProfileGraphPayload",
  "label": "CV Profile",
  "render_as": "group",
  "color_token": "root",
  "attributes": [
    { "name": "profile_id",       "type": "string", "required": true },
    { "name": "snapshot_version", "type": "string", "required": true },
    { "name": "captured_on",      "type": "date",   "required": true }
  ],
  "children": [
    { "type": "CvEntry",             "via": "entries",      "group_by": "category" },
    { "type": "CvSkill",             "via": "skills" },
    { "type": "CvDemonstratesEdge",  "via": "demonstrates" }
  ]
}
```

`group_by: "category"` means: create one sub-subflow per distinct value of `entry.category`,
then place entries inside their respective sub-subflow. This is how `CvSection` emerges as a
view-layer grouping without existing in the stored payload.

---

**`render_as: "node"`** — a standalone node. May have `abstract: true` with variants.

```json
{
  "id": "CvEntry",
  "label": "CV Entry",
  "render_as": "node",
  "color_token": "entity",
  "abstract": true,
  "attributes": [
    { "name": "id",        "type": "string",  "required": true },
    { "name": "essential", "type": "boolean", "required": true }
  ]
}
```

```json
{
  "id": "CvEntry.education",
  "label": "Education Entry",
  "render_as": "node",
  "color_token": "entity",
  "variant_of": "CvEntry",
  "attributes": [
    { "name": "degree",           "type": "string", "required": true  },
    { "name": "specialization",   "type": "string", "required": false },
    { "name": "institution",      "type": "string", "required": true  },
    { "name": "location",         "type": "string", "required": false },
    { "name": "start_date",       "type": "date",   "required": true  },
    { "name": "end_date",         "type": "date",   "required": false },
    { "name": "level_reference",  "type": "string", "required": false },
    { "name": "equivalency_note", "type": "string", "required": false }
  ]
}
```

---

**`render_as: "attribute"`** — shown in the node inspector panel only, not as a graph node.

```json
{
  "id": "CvDescription",
  "label": "Description",
  "render_as": "attribute",
  "color_token": "value",
  "attributes": [
    { "name": "key",    "type": "string", "required": true },
    { "name": "text",   "type": "string", "required": true },
    { "name": "weight", "type": "enum",   "required": true,
      "values": ["headline", "primary_detail", "supporting_detail", "footnote"] }
  ]
}
```

---

### `edge_types` — what connects to what

```json
{
  "id": "demonstrates",
  "label": "demonstrates",
  "from": "CvEntry",
  "to": "CvSkill",
  "color_token": "semantic",
  "animated": false,
  "cardinality": "N:M",
  "note": "Mediated by CvDemonstratesEdge. source=CvEntry.id, target=CvSkill.id, description_keys=evidence."
}
```

```json
{
  "id": "extends",
  "label": "variant of",
  "from": "CvEntry.education",
  "to": "CvEntry",
  "color_token": "structural",
  "cardinality": "N:1",
  "note": "Edge direction: child → parent (variant points up to abstract base)."
}
```

---

### `visual_encoding` — what colour means

The `visual_encoding` block is **part of every schema file**. Each domain defines its own token
palette. This makes the colour legend self-documenting and domain-specific.

```json
"visual_encoding": {
  "color_tokens": {
    "root":     { "border": "rgba(255,255,255,0.5)",  "bg": "rgba(255,255,255,0.04)" },
    "entity":   { "border": "rgba(0,242,255,0.5)",    "bg": "rgba(0,242,255,0.07)"   },
    "abstract": { "border": "rgba(116,117,120,0.4)",  "bg": "rgba(116,117,120,0.05)" },
    "edge_node":{ "border": "rgba(255,170,0,0.5)",    "bg": "rgba(255,170,0,0.07)"   },
    "skill":    { "border": "rgba(255,170,0,0.5)",    "bg": "rgba(255,170,0,0.07)"   },
    "value":    { "border": "rgba(116,117,120,0.3)",  "bg": "rgba(116,117,120,0.03)" }
  },
  "edge_color_tokens": {
    "structural": { "stroke": "rgba(116,117,120,0.5)" },
    "semantic":   { "stroke": "rgba(255,170,0,0.6)"   },
    "contains":   { "stroke": "rgba(0,242,255,0.3)"   }
  }
}
```

The graph renders a **colour legend** derived directly from this block — no hardcoded labels.

---

## CV Domain Schema — Full Inventory

### `node_types`

| id | label | render_as | color_token | abstract | variant_of |
|----|-------|-----------|-------------|----------|------------|
| CvProfileGraphPayload | CV Profile | group | root | — | — |
| CvEntry | CV Entry | node | abstract | true | — |
| CvEntry.personal_data | Personal Data | node | entity | — | CvEntry |
| CvEntry.contact | Contact | node | entity | — | CvEntry |
| CvEntry.legal_status | Legal Status | node | entity | — | CvEntry |
| CvEntry.education | Education | node | entity | — | CvEntry |
| CvEntry.job_experience | Job Experience | node | entity | — | CvEntry |
| CvEntry.project | Project | node | entity | — | CvEntry |
| CvEntry.publication | Publication | node | entity | — | CvEntry |
| CvEntry.language | Language | node | entity | — | CvEntry |
| CvDescription | Description | attribute | value | — | — |
| CvSkill | Skill | node | skill | — | — |
| CvDemonstratesEdge | Demonstrates | node | edge_node | — | — |

### Children of `CvProfileGraphPayload`

| via | type | group_by | effect |
|-----|------|----------|--------|
| entries | CvEntry | category | Creates one sub-subflow per category value (education, job_experience, etc.) |
| skills | CvSkill | — | Placed as nodes in the right column of the group |
| demonstrates | CvDemonstratesEdge | — | Placed as nodes; their edges connect entries to skills |

### `edge_types`

| id | from | to | label | color_token | cardinality |
|----|------|----|-------|-------------|-------------|
| extends | CvEntry.{variant} | CvEntry | variant of | structural | N:1 |
| demonstrates | CvEntry | CvSkill | demonstrates | semantic | N:M |
| demo_source | CvDemonstratesEdge | CvEntry | source | structural | N:1 |
| demo_target | CvDemonstratesEdge | CvSkill | target | semantic | N:1 |
| demo_keys | CvDemonstratesEdge | CvDescription | evidence | structural | N:M |

---

## Component Design

### `SchemaExplorer.tsx` (thin page)

Domain selector pills at top: **CV · Job · Match**. Passes selected schema through `schemaToGraph()`, renders with `KnowledgeGraph` in `readOnly` mode. Job and Match show a placeholder until their schemas are authored.

```tsx
export function SchemaExplorer() {
  const [domain, setDomain] = useState<'cv' | 'job' | 'match'>('cv');
  const schema = useSchema(domain);
  const { nodes, edges } = useMemo(() => schemaToGraph(schema), [schema]);
  return (
    <KnowledgeGraph initialNodes={nodes} initialEdges={edges} readOnly />
  );
}
```

### `schemaToGraph.ts`

```ts
import type { DocumentSchema } from '../../../schemas/types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

export function schemaToGraph(schema: DocumentSchema): {
  nodes: SimpleNode[];
  edges: SimpleEdge[];
}
```

Mapping rules:
- `render_as: "group"` → ReactFlow group node (parentId + extent: 'parent' for children)
  - `group_by` field → creates intermediate group nodes per distinct value
- `render_as: "node"` → regular `SimpleNode`; `abstract: true` nodes rendered with muted style
- `render_as: "attribute"` → **not rendered as a node**; stored in parent's `node.data.meta.attributes`
- Each `edge_type` → `SimpleEdge` with `data.relationType` and stroke color from `visual_encoding`
- `variant_of` types get an `extends` edge to their parent
- `color_token` resolved from `schema.visual_encoding.color_tokens[token]` — no global fallback
- Layout: dagre `rankdir: LR`

### `useSchema.ts`

Location: `features/schema-explorer/lib/useSchema.ts` (static import, no API call).

```ts
import cv    from '../../../schemas/cv.schema.json';
import job   from '../../../schemas/job.schema.json';
import match from '../../../schemas/match.schema.json';
import type { DocumentSchema } from '../../../schemas/types';

const SCHEMAS: Record<string, DocumentSchema> = {
  cv:    cv    as DocumentSchema,
  job:   job   as DocumentSchema,
  match: match as DocumentSchema,
};

export function useSchema(domain: 'cv' | 'job' | 'match'): DocumentSchema {
  return SCHEMAS[domain];
}
```

### `KnowledgeGraph.tsx` additions

- `readOnly?: boolean` prop — suppresses edit panel, save button, drag-to-connect
- `CATEGORY_COLORS` extended with `root`, `abstract`, `edge_node`, `value` tokens

---

## File Structure

```
apps/review-workbench/src/
├── schemas/
│   ├── types.ts             ← DocumentSchema, SchemaNodeType, SchemaEdgeType, …
│   ├── cv.schema.json       ← full CV domain (Phase 1)
│   ├── job.schema.json      ← stub { document, node_types:[], edge_types:[], visual_encoding:{…} }
│   └── match.schema.json    ← stub
├── features/schema-explorer/
│   └── lib/
│       ├── schemaToGraph.ts
│       └── useSchema.ts
└── pages/global/
    └── SchemaExplorer.tsx
```

Router (`App.tsx`): add `{ path: 'schema', element: <SchemaExplorer /> }`.
Nav (`AppShell.tsx`): add Schema icon.
`KnowledgeGraph.tsx`: add `readOnly` prop + extend `CATEGORY_COLORS`.

---

## Definition of Done

- [ ] `/schema` route renders without errors
- [ ] Domain selector (CV / Job / Match) switches the displayed graph
- [ ] `render_as: "group"` types render as subflow group nodes
- [ ] `group_by: "category"` produces sub-subflows (one per category value)
- [ ] `render_as: "node"` types render as standalone nodes
- [ ] `render_as: "attribute"` types are absent from the graph; their fields appear in the inspector of their parent node
- [ ] `variant_of` nodes render with an `extends` edge pointing to their abstract parent
- [ ] Edge labels and colors come from `edge_types[].color_token` resolved via `visual_encoding`
- [ ] Node colors come from `color_token` resolved via `visual_encoding`
- [ ] A colour legend is rendered, derived from `visual_encoding.color_tokens`
- [ ] Clicking a node shows its `attributes` in the inspector panel
- [ ] Layout is dagre LR with no overlapping nodes
- [ ] Job and Match domains show a placeholder
- [ ] `KnowledgeGraph` read-only mode: no edit panel, no save button, no drag-to-connect
