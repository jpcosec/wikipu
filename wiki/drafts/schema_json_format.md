---
identity:
  node_id: "doc:wiki/drafts/schema_json_format.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md", relation_type: "documents"}
---

### TypeScript contracts — `src/schemas/types.ts`

## Details

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

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md`.