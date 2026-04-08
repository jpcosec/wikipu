# Schema Explorer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make KnowledgeGraph accept a `readOnly` prop and add new color tokens, then build a SchemaExplorer page that feeds `cv.schema.json` through a `schemaToGraph` adapter and renders it read-only.

**Architecture:** Schema JSONs (one per domain) define node types, render hints, edge types, and visual encoding. A pure `schemaToGraph` function converts them to `SimpleNode[]` + `SimpleEdge[]`. `SchemaExplorer` selects a domain, converts, and passes to `KnowledgeGraph readOnly`. No new component primitives — KnowledgeGraph is the runtime.

**Tech Stack:** React 18 · TypeScript · @xyflow/react · Vitest (added) · Tailwind Terran tokens

---

## Spec

`plan/01_ui/specs/D1_schema_explorer.md`

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `apps/review-workbench/src/schemas/types.ts` | `DocumentSchema`, `SchemaNodeType`, `SchemaEdgeType`, `SchemaAttribute`, `SchemaChild`, `VisualEncoding` TypeScript contracts |
| Create | `apps/review-workbench/src/schemas/cv.schema.json` | Full CV domain schema |
| Create | `apps/review-workbench/src/schemas/job.schema.json` | Stub (empty types/edges) |
| Create | `apps/review-workbench/src/schemas/match.schema.json` | Stub |
| Create | `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts` | Pure fn: `DocumentSchema → { nodes: SimpleNode[], edges: SimpleEdge[] }` |
| Create | `apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts` | Static domain selector |
| Create | `apps/review-workbench/src/pages/global/SchemaExplorer.tsx` | Thin page: pill selector + KnowledgeGraph readOnly |
| Modify | `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx:136-158` | Add `root`, `abstract`, `edge_node`, `value` to `CATEGORY_COLORS` |
| Modify | `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx:768-773` | Add `readOnly?: boolean` to `KnowledgeGraphProps` |
| Modify | `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx:775` | Thread `readOnly` through `NodeEditorInner` |
| Modify | `apps/review-workbench/src/App.tsx` | Add `/schema` route |
| Modify | `apps/review-workbench/src/components/layouts/AppShell.tsx` | Add Schema nav item |
| Create | `apps/review-workbench/vite.config.ts` (modify) | Add Vitest config block |
| Create | `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts` | Unit tests for schemaToGraph |

---

## Task 1: Add Vitest (minimal)

**Files:**
- Modify: `apps/review-workbench/package.json`
- Modify: `apps/review-workbench/vite.config.ts`

- [ ] **Step 1: Install Vitest**

```bash
cd apps/review-workbench
npm install --save-dev vitest
```

- [ ] **Step 2: Add test script to package.json**

In `package.json` scripts, add:
```json
"test": "vitest run",
"test:watch": "vitest"
```

- [ ] **Step 3: Add Vitest config to vite.config.ts**

Read current `vite.config.ts` first, then add `test` block:
```ts
/// <reference types="vitest" />
// existing config +
test: {
  environment: 'node',
  include: ['src/**/*.test.ts'],
}
```

- [ ] **Step 4: Verify Vitest works**

```bash
cd apps/review-workbench
echo 'import { test, expect } from "vitest"; test("smoke", () => expect(1+1).toBe(2));' > src/smoke.test.ts
npm test
# Expected: 1 passed
rm src/smoke.test.ts
```

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/package.json apps/review-workbench/vite.config.ts apps/review-workbench/package-lock.json
git commit -m "chore(workbench): add vitest for unit testing"
```

---

## Task 2: TypeScript schema contracts

**Files:**
- Create: `apps/review-workbench/src/schemas/types.ts`

- [ ] **Step 1: Create `types.ts`**

```ts
// apps/review-workbench/src/schemas/types.ts

export type RenderAs = 'group' | 'node' | 'attribute';
export type RelationType = 'contains' | 'extends' | 'semantic_edge' | 'references';

export interface SchemaAttribute {
  name: string;
  type: string;
  required: boolean;
  values?: string[];
  note?: string;
}

export interface SchemaChild {
  type: string;
  via: string;
  group_by?: string;
}

export interface SchemaNodeType {
  id: string;
  label: string;
  render_as: RenderAs;
  color_token: string;
  abstract?: boolean;
  variant_of?: string;
  attributes: SchemaAttribute[];
  children?: SchemaChild[];
}

export interface SchemaEdgeType {
  id: string;
  label: string;
  from: string;
  to: string;
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
    root_type: string;
  };
  node_types: SchemaNodeType[];
  edge_types: SchemaEdgeType[];
  visual_encoding: VisualEncoding;
}
```

- [ ] **Step 2: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npx tsc --noEmit
# Expected: no errors
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/schemas/types.ts
git commit -m "feat(schema): add DocumentSchema TypeScript contracts"
```

---

## Task 3: CV schema JSON

**Files:**
- Create: `apps/review-workbench/src/schemas/cv.schema.json`

- [ ] **Step 1: Write the failing test first**

Create `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts` with just a schema shape test:

```ts
import { describe, test, expect } from 'vitest';
import cvSchema from '../../../schemas/cv.schema.json';
import type { DocumentSchema } from '../../../schemas/types';

const schema = cvSchema as DocumentSchema;

describe('cv.schema.json shape', () => {
  test('has required top-level keys', () => {
    expect(schema.document).toBeDefined();
    expect(schema.node_types).toBeInstanceOf(Array);
    expect(schema.edge_types).toBeInstanceOf(Array);
    expect(schema.visual_encoding).toBeDefined();
  });

  test('root_type exists in node_types', () => {
    const rootId = schema.document.root_type;
    const root = schema.node_types.find(t => t.id === rootId);
    expect(root).toBeDefined();
    expect(root?.render_as).toBe('group');
  });

  test('all variant_of references point to existing types', () => {
    const typeIds = new Set(schema.node_types.map(t => t.id));
    for (const t of schema.node_types) {
      if (t.variant_of) {
        expect(typeIds.has(t.variant_of), `${t.id}.variant_of="${t.variant_of}" not found`).toBe(true);
      }
    }
  });

  test('all edge from/to point to existing types', () => {
    const typeIds = new Set(schema.node_types.map(t => t.id));
    for (const e of schema.edge_types) {
      expect(typeIds.has(e.from), `edge ${e.id}.from="${e.from}" not found`).toBe(true);
      expect(typeIds.has(e.to), `edge ${e.id}.to="${e.to}" not found`).toBe(true);
    }
  });

  test('all color_tokens referenced in node_types exist in visual_encoding', () => {
    const tokens = new Set(Object.keys(schema.visual_encoding.color_tokens));
    for (const t of schema.node_types) {
      expect(tokens.has(t.color_token), `node ${t.id}.color_token="${t.color_token}" not in visual_encoding`).toBe(true);
    }
  });
});
```

- [ ] **Step 2: Run — expect FAIL (cv.schema.json missing)**

```bash
cd apps/review-workbench && npm test
# Expected: FAIL — cannot find module
```

- [ ] **Step 3: Create `cv.schema.json`**

```json
{
  "document": {
    "id": "cv_profile_graph",
    "label": "CV Profile Graph",
    "version": "1.0",
    "description": "Structured CV with entries grouped by category, connected to skills via demonstrates edges.",
    "root_type": "CvProfileGraphPayload"
  },
  "node_types": [
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
        { "type": "CvEntry",            "via": "entries",      "group_by": "category" },
        { "type": "CvSkill",            "via": "skills" },
        { "type": "CvDemonstratesEdge", "via": "demonstrates" }
      ]
    },
    {
      "id": "CvEntry",
      "label": "CV Entry",
      "render_as": "node",
      "color_token": "abstract",
      "abstract": true,
      "attributes": [
        { "name": "id",        "type": "string",  "required": true },
        { "name": "essential", "type": "boolean", "required": true }
      ]
    },
    {
      "id": "CvEntry.personal_data",
      "label": "Personal Data",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "full_name",      "type": "string", "required": true  },
        { "name": "preferred_name", "type": "string", "required": false },
        { "name": "birth_date",     "type": "date",   "required": false },
        { "name": "nationality",    "type": "string", "required": false }
      ]
    },
    {
      "id": "CvEntry.contact",
      "label": "Contact",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "email",     "type": "string",   "required": true  },
        { "name": "phone",     "type": "string",   "required": false },
        { "name": "addresses", "type": "object[]", "required": false },
        { "name": "links",     "type": "object",   "required": false }
      ]
    },
    {
      "id": "CvEntry.legal_status",
      "label": "Legal Status",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "visa_type",               "type": "string",  "required": true },
        { "name": "visa_status",             "type": "string",  "required": true },
        { "name": "work_permission_germany", "type": "boolean", "required": true }
      ]
    },
    {
      "id": "CvEntry.education",
      "label": "Education",
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
    },
    {
      "id": "CvEntry.job_experience",
      "label": "Job Experience",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "role",         "type": "string", "required": true  },
        { "name": "organization", "type": "string", "required": true  },
        { "name": "location",     "type": "string", "required": false },
        { "name": "start_date",   "type": "date",   "required": true  },
        { "name": "end_date",     "type": "date",   "required": false }
      ]
    },
    {
      "id": "CvEntry.project",
      "label": "Project",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "name",  "type": "string",   "required": true  },
        { "name": "role",  "type": "string",   "required": false },
        { "name": "stack", "type": "string[]", "required": false }
      ]
    },
    {
      "id": "CvEntry.publication",
      "label": "Publication",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "year",  "type": "number", "required": true  },
        { "name": "title", "type": "string", "required": true  },
        { "name": "venue", "type": "string", "required": false },
        { "name": "url",   "type": "string", "required": false }
      ]
    },
    {
      "id": "CvEntry.language",
      "label": "Language",
      "render_as": "node",
      "color_token": "entity",
      "variant_of": "CvEntry",
      "attributes": [
        { "name": "name",  "type": "string", "required": true  },
        { "name": "level", "type": "string", "required": true  },
        { "name": "note",  "type": "string", "required": false }
      ]
    },
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
    },
    {
      "id": "CvSkill",
      "label": "Skill",
      "render_as": "node",
      "color_token": "skill",
      "attributes": [
        { "name": "id",        "type": "string",  "required": true  },
        { "name": "label",     "type": "string",  "required": true  },
        { "name": "category",  "type": "string",  "required": true  },
        { "name": "essential", "type": "boolean", "required": true  },
        { "name": "level",     "type": "string",  "required": false }
      ]
    },
    {
      "id": "CvDemonstratesEdge",
      "label": "Demonstrates",
      "render_as": "node",
      "color_token": "edge_node",
      "attributes": [
        { "name": "id",               "type": "string",   "required": true,
          "note": "CvEntry.id" },
        { "name": "source",           "type": "string",   "required": true,
          "note": "CvEntry.id" },
        { "name": "target",           "type": "string",   "required": true,
          "note": "CvSkill.id" },
        { "name": "description_keys", "type": "string[]", "required": true,
          "note": "CvDescription.key values that are the evidence" }
      ]
    }
  ],
  "edge_types": [
    {
      "id": "extends",
      "label": "variant of",
      "from": "CvEntry.personal_data",
      "to": "CvEntry",
      "color_token": "structural",
      "cardinality": "N:1",
      "note": "Applies to all CvEntry.* variants. Edge direction: child → parent."
    },
    {
      "id": "demonstrates",
      "label": "demonstrates",
      "from": "CvEntry",
      "to": "CvSkill",
      "color_token": "semantic",
      "cardinality": "N:M",
      "note": "Mediated by CvDemonstratesEdge. source=CvEntry.id, target=CvSkill.id."
    },
    {
      "id": "demo_source",
      "label": "source → entry",
      "from": "CvDemonstratesEdge",
      "to": "CvEntry",
      "color_token": "structural",
      "cardinality": "N:1"
    },
    {
      "id": "demo_target",
      "label": "target → skill",
      "from": "CvDemonstratesEdge",
      "to": "CvSkill",
      "color_token": "semantic",
      "cardinality": "N:1"
    }
  ],
  "visual_encoding": {
    "color_tokens": {
      "root":     { "border": "rgba(255,255,255,0.5)",  "bg": "rgba(255,255,255,0.04)" },
      "abstract": { "border": "rgba(116,117,120,0.4)",  "bg": "rgba(116,117,120,0.05)" },
      "entity":   { "border": "rgba(0,242,255,0.5)",    "bg": "rgba(0,242,255,0.07)"   },
      "skill":    { "border": "rgba(255,170,0,0.5)",    "bg": "rgba(255,170,0,0.07)"   },
      "edge_node":{ "border": "rgba(255,180,171,0.5)",  "bg": "rgba(255,180,171,0.07)" },
      "value":    { "border": "rgba(116,117,120,0.3)",  "bg": "rgba(116,117,120,0.03)" }
    },
    "edge_color_tokens": {
      "structural": { "stroke": "rgba(116,117,120,0.5)" },
      "semantic":   { "stroke": "rgba(255,170,0,0.6)"   },
      "contains":   { "stroke": "rgba(0,242,255,0.3)"   }
    }
  }
}
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd apps/review-workbench && npm test
# Expected: 5 passed
```

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/src/schemas/cv.schema.json apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts
git commit -m "feat(schema): add cv.schema.json + shape validation tests"
```

---

## Task 4: Job and Match schema stubs

**Files:**
- Create: `apps/review-workbench/src/schemas/job.schema.json`
- Create: `apps/review-workbench/src/schemas/match.schema.json`

- [ ] **Step 1: Create `job.schema.json`**

```json
{
  "document": {
    "id": "job_posting",
    "label": "Job Posting",
    "version": "0.1",
    "description": "Structured job posting with requirements extracted by extract_understand node.",
    "root_type": "__stub__"
  },
  "node_types": [],
  "edge_types": [],
  "visual_encoding": {
    "color_tokens": {},
    "edge_color_tokens": {}
  }
}
```

- [ ] **Step 2: Create `match.schema.json`**

```json
{
  "document": {
    "id": "match_result",
    "label": "Match Result",
    "version": "0.1",
    "description": "Match envelope linking CV evidence to job requirements via skill nodes.",
    "root_type": "__stub__"
  },
  "node_types": [],
  "edge_types": [],
  "visual_encoding": {
    "color_tokens": {},
    "edge_color_tokens": {}
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/schemas/job.schema.json apps/review-workbench/src/schemas/match.schema.json
git commit -m "feat(schema): add job and match schema stubs"
```

---

## Task 5: `schemaToGraph` — pure converter

**Files:**
- Create: `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts`
- Modify: `apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts`

The converter maps each `render_as: "node"` and `render_as: "group"` type to a `SimpleNode`, and each `edge_type` to a `SimpleEdge`. Types with `render_as: "attribute"` are skipped (they show in the inspector only). Color comes from `visual_encoding.color_tokens[color_token]`.

- [ ] **Step 1: Add converter tests to the existing test file**

Append to `schemaToGraph.test.ts`:

```ts
import { schemaToGraph } from './schemaToGraph';

describe('schemaToGraph', () => {
  const { nodes, edges } = schemaToGraph(schema);

  test('produces one node per non-attribute type', () => {
    const nonAttr = schema.node_types.filter(t => t.render_as !== 'attribute');
    expect(nodes).toHaveLength(nonAttr.length);
  });

  test('attribute types are not in nodes', () => {
    const attrIds = schema.node_types.filter(t => t.render_as === 'attribute').map(t => t.id);
    for (const id of attrIds) {
      expect(nodes.find(n => n.id === id)).toBeUndefined();
    }
  });

  test('each node has a name and category from schema', () => {
    for (const node of nodes) {
      expect(typeof node.data.name).toBe('string');
      expect(typeof node.data.category).toBe('string');
    }
  });

  test('edges are produced for each edge_type', () => {
    expect(edges.length).toBeGreaterThanOrEqual(schema.edge_types.length);
  });

  test('variant_of types get an extends edge to their parent', () => {
    const variantTypes = schema.node_types.filter(t => t.variant_of);
    for (const vt of variantTypes) {
      const extendsEdge = edges.find(
        e => e.source === vt.id && e.target === vt.variant_of
      );
      expect(extendsEdge, `no extends edge for ${vt.id}`).toBeDefined();
    }
  });

  test('color from visual_encoding is stored in node meta', () => {
    const rootNode = nodes.find(n => n.id === schema.document.root_type);
    expect(rootNode?.data.meta).toBeDefined();
  });
});
```

- [ ] **Step 2: Run — expect FAIL (schemaToGraph not found)**

```bash
cd apps/review-workbench && npm test
# Expected: FAIL — cannot find module schemaToGraph
```

- [ ] **Step 3: Implement `schemaToGraph.ts`**

```ts
// apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts
import type { DocumentSchema, SchemaNodeType } from '../../../schemas/types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

function renderToken(type: SchemaNodeType): string {
  // Map schema category to KnowledgeGraph CATEGORY_COLORS key
  const map: Record<string, string> = {
    root:     'root',
    abstract: 'abstract',
    entity:   'entry',
    skill:    'skill',
    edge_node: 'edge_node',
    value:    'value',
  };
  return map[type.color_token] ?? type.color_token;
}

export function schemaToGraph(schema: DocumentSchema): {
  nodes: SimpleNode[];
  edges: SimpleEdge[];
} {
  const nodes: SimpleNode[] = [];
  const edges: SimpleEdge[] = [];

  // Nodes: all non-attribute types
  for (const type of schema.node_types) {
    if (type.render_as === 'attribute') continue;

    const colorToken = schema.visual_encoding.color_tokens[type.color_token];

    nodes.push({
      id: type.id,
      type: type.render_as === 'group' ? 'group' : 'simple',
      position: { x: 0, y: 0 }, // dagre will reposition
      data: {
        name: type.label,
        category: renderToken(type),
        properties: {
          render_as: type.render_as,
          ...(type.abstract ? { abstract: 'true' } : {}),
          ...(type.variant_of ? { variant_of: type.variant_of } : {}),
        },
        meta: {
          schemaType: type,
          colorToken,
        },
      },
    });

    // extends edge for variants
    if (type.variant_of) {
      edges.push({
        id: `extends:${type.id}`,
        source: type.id,
        target: type.variant_of,
        data: {
          relationType: 'extends',
          properties: { label: 'variant of' },
        },
      });
    }
  }

  // Edges from edge_types (skip duplicates already added as extends)
  for (const et of schema.edge_types) {
    // Skip if already covered by variant_of auto-edges
    if (et.id === 'extends') continue;
    const edgeColor = schema.visual_encoding.edge_color_tokens[et.color_token];
    edges.push({
      id: `edge:${et.id}`,
      source: et.from,
      target: et.to,
      data: {
        relationType: et.id,
        properties: {
          label: et.label,
          ...(et.cardinality ? { cardinality: et.cardinality } : {}),
        },
        meta: { edgeColor },
      },
    });
  }

  return { nodes, edges };
}
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd apps/review-workbench && npm test
# Expected: all passed
```

> **Note — edge color application is deferred:** `SimpleEdgeData extends Record<string, unknown>` so `meta: { edgeColor }` on edges does not cause a TypeScript error, but edge color is not yet applied to rendered edges (no edge style renderer reads `data.meta.edgeColor`). This is intentional — edge color rendering is a follow-up task once the schema graph is working.

> **Note — CATEGORY_COLORS dependency:** The `renderToken` function maps `root`, `abstract`, `edge_node`, `value` to CATEGORY_COLORS keys that are added in Task 7. Tests pass because they don't exercise CATEGORY_COLORS, but the browser render will show fallback grey for those tokens until Task 7 is done. Complete Task 7 before doing the end-to-end check in Task 9.

- [ ] **Step 5: Commit**

```bash
git add apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.ts apps/review-workbench/src/features/schema-explorer/lib/schemaToGraph.test.ts
git commit -m "feat(schema-explorer): add schemaToGraph converter with tests"
```

---

## Task 6: `useSchema` static hook

**Files:**
- Create: `apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts`

- [ ] **Step 1: Create `useSchema.ts`**

```ts
// apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts
import cvSchema    from '../../../schemas/cv.schema.json';
import jobSchema   from '../../../schemas/job.schema.json';
import matchSchema from '../../../schemas/match.schema.json';
import type { DocumentSchema } from '../../../schemas/types';

export type SchemaDomain = 'cv' | 'job' | 'match';

const SCHEMAS: Record<SchemaDomain, DocumentSchema> = {
  cv:    cvSchema    as unknown as DocumentSchema,
  job:   jobSchema   as unknown as DocumentSchema,
  match: matchSchema as unknown as DocumentSchema,
};

export function useSchema(domain: SchemaDomain): DocumentSchema {
  return SCHEMAS[domain];
}
```

- [ ] **Step 2: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npx tsc --noEmit
# Expected: no errors
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/schema-explorer/lib/useSchema.ts
git commit -m "feat(schema-explorer): add useSchema static domain loader"
```

---

## Task 7: `readOnly` prop + new CATEGORY_COLORS

**Files:**
- Modify: `apps/review-workbench/src/pages/global/KnowledgeGraph.tsx`

- [ ] **Step 1: Add new tokens to `CATEGORY_COLORS` (line ~136)**

Add after the existing entries:
```ts
// Schema explorer tokens
root:      { border: 'rgba(255,255,255,0.5)',  bg: 'rgba(255,255,255,0.04)' },
abstract:  { border: 'rgba(116,117,120,0.4)',  bg: 'rgba(116,117,120,0.05)' },
edge_node: { border: 'rgba(255,180,171,0.5)',  bg: 'rgba(255,180,171,0.07)' },
value:     { border: 'rgba(116,117,120,0.3)',  bg: 'rgba(116,117,120,0.03)' },
```

- [ ] **Step 2: Add `readOnly` to `KnowledgeGraphProps` (line ~768)**

```ts
export interface KnowledgeGraphProps {
  initialNodes?: SimpleNode[];
  initialEdges?: SimpleEdge[];
  onSave?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
  onChange?: (nodes: SimpleNode[], edges: SimpleEdge[]) => void;
  readOnly?: boolean;
}
```

- [ ] **Step 3: Thread `readOnly` through `NodeEditorInner`**

In `function NodeEditorInner({ initialNodes, initialEdges, onSave, onChange }: KnowledgeGraphProps)` (line ~775), add `readOnly = false` to destructuring:

```ts
function NodeEditorInner({ initialNodes, initialEdges, onSave, onChange, readOnly = false }: KnowledgeGraphProps)
```

- [ ] **Step 4: Suppress edit controls when `readOnly`**

All changes are in the JSX returned by `NodeEditorInner`. Apply each gate:

**4a — Save / Discard / Undo toolbar (around line 2133)**
```tsx
{/* gate the entire save/discard/undo row */}
{!readOnly && (
  <>
    <button ... onClick={onSaveWorkspace}>Save workspace</button>
    <button ... onClick={onDiscardWorkspace}>Discard</button>
    <button ... onClick={onUndo}>Undo</button>
    <button ... onClick={onRedo}>Redo</button>
  </>
)}
```

**4b — ReactFlow connection handlers (around line 2422)**
```tsx
onConnect={readOnly ? undefined : onConnect}
onConnectStart={readOnly ? undefined : onConnectStart}
onConnectEnd={readOnly ? undefined : onConnectEnd}
nodesDraggable={!readOnly}
nodesConnectable={!readOnly}
```

**4c — Vacant-node connect buttons (around line 2396)**
```tsx
{!readOnly && vacantCandidateNodes.map((node) => ( ... ))}
```

**4d — Edit node/edge panels (the `editorState === 'edit_node'` and `editorState === 'edit_relation'` blocks)**
```tsx
{!readOnly && editorState === 'edit_node' && ( ... )}
{!readOnly && editorState === 'edit_relation' && ( ... )}
```

- [ ] **Step 5: Verify TypeScript compiles and dev server runs**

```bash
cd apps/review-workbench && npx tsc --noEmit
npm run dev
# Open browser, check /cv still works normally
```

- [ ] **Step 6: Commit**

```bash
git add apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "feat(knowledge-graph): add readOnly prop + schema color tokens"
```

---

## Task 8: `SchemaExplorer` page

**Files:**
- Create: `apps/review-workbench/src/pages/global/SchemaExplorer.tsx`

- [ ] **Step 1: Create `SchemaExplorer.tsx`**

```tsx
// apps/review-workbench/src/pages/global/SchemaExplorer.tsx
import { useMemo, useState } from 'react';
import { cn } from '../../utils/cn';
import { KnowledgeGraph } from './KnowledgeGraph';
import { schemaToGraph } from '../../features/schema-explorer/lib/schemaToGraph';
import { useSchema, type SchemaDomain } from '../../features/schema-explorer/lib/useSchema';

const DOMAINS: { id: SchemaDomain; label: string }[] = [
  { id: 'cv',    label: 'CV' },
  { id: 'job',   label: 'Job' },
  { id: 'match', label: 'Match' },
];

export function SchemaExplorer() {
  const [domain, setDomain] = useState<SchemaDomain>('cv');
  const schema = useSchema(domain);
  const isStub = schema.node_types.length === 0;
  const { nodes, edges } = useMemo(() => schemaToGraph(schema), [schema]);

  return (
    <div className="flex flex-col min-h-screen bg-background">
      <header className="flex items-center gap-3 px-6 py-3 border-b border-outline/10 bg-surface">
        <span className="text-on-muted font-mono text-[10px] uppercase tracking-widest mr-2">Schema</span>
        {DOMAINS.map(d => (
          <button
            key={d.id}
            onClick={() => setDomain(d.id)}
            className={cn(
              'px-3 py-1 font-mono text-[11px] uppercase tracking-widest border transition-colors',
              domain === d.id
                ? 'border-primary text-primary bg-primary/10'
                : 'border-outline/20 text-on-muted hover:border-primary/50 hover:text-on-surface bg-transparent',
            )}
          >
            {d.label}
          </button>
        ))}
        <span className="ml-auto text-on-muted font-mono text-[10px]">
          {schema.document.label} · v{schema.document.version}
        </span>
      </header>

      {isStub ? (
        <div className="flex-1 flex items-center justify-center text-on-muted font-mono text-sm">
          Schema not yet defined for <span className="text-primary mx-1 uppercase">{domain}</span>
        </div>
      ) : (
        <div className="flex-1">
          <KnowledgeGraph initialNodes={nodes} initialEdges={edges} readOnly />
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Add colour legend below the header**

After the domain pill selector row, add a legend derived directly from `visual_encoding.color_tokens`:

```tsx
{/* Colour legend — inside the header, after the domain pills */}
<div className="flex items-center gap-3 ml-auto">
  {Object.entries(schema.visual_encoding.color_tokens).map(([token, colors]) => (
    <span key={token} className="flex items-center gap-1">
      <span
        className="inline-block w-2.5 h-2.5 rounded-sm border"
        style={{ borderColor: colors.border, backgroundColor: colors.bg }}
      />
      <span className="font-mono text-[9px] text-on-muted uppercase tracking-widest">
        {token}
      </span>
    </span>
  ))}
</div>
```

Move the `schema.document.label` version string outside the legend flex group so it doesn't crowd the legend.

- [ ] **Step 3: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npx tsc --noEmit
# Expected: no errors
```

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/pages/global/SchemaExplorer.tsx
git commit -m "feat(schema-explorer): add SchemaExplorer page with colour legend"
```

---

## Task 9: Wire routes and nav

**Files:**
- Modify: `apps/review-workbench/src/App.tsx`
- Modify: `apps/review-workbench/src/components/layouts/AppShell.tsx`

- [ ] **Step 1: Add route to `App.tsx`**

Add import:
```ts
import { SchemaExplorer } from './pages/global/SchemaExplorer';
```

Add to the `children` array inside the root route:
```ts
{ path: 'schema', element: <SchemaExplorer /> },
```

- [ ] **Step 2: Add nav item to `AppShell.tsx`**

Add import:
```ts
import { LayoutDashboard, FolderOpen, Network, GitGraph, Layers } from 'lucide-react';
```

Add to `NAV_ITEMS`:
```ts
{ to: '/schema', icon: Layers, label: 'Schema', end: false },
```

- [ ] **Step 3: Open dev server and verify end-to-end**

```bash
cd apps/review-workbench && npm run dev
```

Check:
- `/schema` loads without errors
- CV pill shows the graph with nodes
- Job/Match pills show the stub placeholder
- Node click opens inspector with field list
- No edit panel, no save button visible
- `/cv` still works (not broken by readOnly change)

- [ ] **Step 4: Commit**

```bash
git add apps/review-workbench/src/App.tsx apps/review-workbench/src/components/layouts/AppShell.tsx
git commit -m "feat(schema-explorer): wire /schema route and nav"
```

> **End-to-end checklist (do this after committing):**
> - `/schema` loads — CV graph shows nodes with category colors (not all grey)
> - Job/Match show placeholder text
> - Colour legend visible in header
> - Clicking a node shows its `attributes` in the inspector panel (field name + type + required)
> - No save button, no discard, no undo visible
> - Drag-to-connect disabled (cannot draw edges)
> - `/cv` editor still works normally (not regressed by readOnly change)
