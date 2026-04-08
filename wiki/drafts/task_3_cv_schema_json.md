---
identity:
  node_id: "doc:wiki/drafts/task_3_cv_schema_json.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

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

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.