---
identity:
  node_id: "doc:wiki/drafts/task_4_c1_b_create_cvtograph_adapter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

Create the adapter that converts `CvProfileGraphPayload` ↔ `SimpleNode[]`/`SimpleEdge[]`. The `meta` passthrough preserves structured `CvEntry` fields and descriptions across the round-trip.

## Details

Create the adapter that converts `CvProfileGraphPayload` ↔ `SimpleNode[]`/`SimpleEdge[]`. The `meta` passthrough preserves structured `CvEntry` fields and descriptions across the round-trip.

**Files:**
- Create: `apps/review-workbench/src/features/base-cv/lib/cvToGraph.ts`

Import paths to use:
- `type { SimpleNode, SimpleEdge }` from the KnowledgeGraph file need to be exported first (see Step 0 below)

- [ ] **Step 0: Export SimpleNode, SimpleEdge, SimpleNodeData, SimpleEdgeData from KnowledgeGraph.tsx**

Add `export` before these four type/interface declarations in KnowledgeGraph.tsx:
- `export interface SimpleNodeData`
- `export interface SimpleEdgeData`
- `export type SimpleNode`
- `export type SimpleEdge`

- [ ] **Step 1: Create the adapter file**

```ts
// apps/review-workbench/src/features/base-cv/lib/cvToGraph.ts
import type { CvProfileGraphPayload, CvEntry, CvSkill } from '../../../types/api.types';
import type { SimpleNode, SimpleEdge } from '../../../pages/global/KnowledgeGraph';

function entryId(id: string) { return `entry:${id}`; }
function skillId(id: string) { return `skill:${id}`; }
function sectionId(cat: string) { return `section:${cat}`; }

export function cvProfileToGraph(data: CvProfileGraphPayload): { nodes: SimpleNode[]; edges: SimpleEdge[] } {
  const nodes: SimpleNode[] = [];
  const edges: SimpleEdge[] = [];

  // Document root group
  const docId = 'doc:root';
  nodes.push({
    id: docId,
    type: 'group',
    position: { x: 0, y: 0 },
    style: { width: 440, height: 60 },  // height expanded dynamically by content
    data: { name: 'My CV', category: 'document', properties: {} },
  });

  // Group entries by category
  const byCategory = new Map<string, CvEntry[]>();
  for (const entry of data.entries) {
    const arr = byCategory.get(entry.category) ?? [];
    arr.push(entry);
    byCategory.set(entry.category, arr);
  }

  let sectionY = 0;
  let skillY = 0;
  const categoryList = Array.from(byCategory.keys());

  for (let ci = 0; ci < categoryList.length; ci++) {
    const cat = categoryList[ci]!;
    const catEntries = byCategory.get(cat)!;
    const secId = sectionId(cat);

    const sectionHeight = 60 + catEntries.length * 80;

    nodes.push({
      id: secId,
      type: 'group',
      parentId: docId,
      extent: 'parent',
      position: { x: 20, y: 60 + sectionY },
      style: { width: 400, height: sectionHeight },
      data: { name: cat, category: 'section', properties: {} },
    });

    sectionY += sectionHeight + 16;

    for (let ei = 0; ei < catEntries.length; ei++) {
      const entry = catEntries[ei]!;
      const eId = entryId(entry.id);
      const title = String(entry.fields['title'] ?? entry.id);
      const date = String(entry.fields['date'] ?? entry.fields['start_date'] ?? '');

      nodes.push({
        id: eId,
        type: 'simple',
        parentId: secId,
        extent: 'parent',
        position: { x: 20, y: 50 + ei * 80 },
        data: {
          name: title,
          category: 'entry',
          properties: { date },
          meta: {
            originalId: entry.id,
            fields: entry.fields,
            descriptions: entry.descriptions,
            essential: entry.essential,
          },
        },
      });
    }
  }

  // Update docId height to fit all sections
  const docNode = nodes.find(n => n.id === docId)!;
  (docNode.style as Record<string, unknown>)['height'] = 80 + sectionY;

  // Skill nodes (right column)
  for (let si = 0; si < data.skills.length; si++) {
    const skill = data.skills[si]!;
    const sId = skillId(skill.id);
    nodes.push({
      id: sId,
      type: 'simple',
      position: { x: 600, y: skillY },
      data: {
        name: skill.label,
        category: 'skill',
        properties: { level: skill.level ?? '', category: skill.category },
        meta: { originalId: skill.id, essential: skill.essential, skillMeta: skill.meta },
      },
    });
    skillY += 70;
  }

  // Demonstrates edges
  for (const d of data.demonstrates) {
    edges.push({
      id: `demonstrates:${d.id}`,
      source: entryId(d.source),
      target: skillId(d.target),
      type: 'subflow',
      data: { relationType: 'demonstrates', properties: {} },
    });
  }

  return { nodes, edges };
}

export function graphToCvProfile(
  nodes: SimpleNode[],
  edges: SimpleEdge[],
  original: CvProfileGraphPayload,
): CvProfileGraphPayload {
  const entries: CvEntry[] = nodes
    .filter(n => n.data.category === 'entry')
    .map(n => {
      const meta = n.data.meta as { originalId?: string; fields?: Record<string, unknown>; descriptions?: CvEntry['descriptions']; essential?: boolean } | undefined;
      return {
        id: meta?.originalId ?? n.id.replace('entry:', ''),
        category: n.parentId
          ? nodes.find(p => p.id === n.parentId)?.data.name ?? 'general'
          : 'general',
        essential: meta?.essential ?? false,
        fields: meta?.fields ?? { title: n.data.name },
        descriptions: meta?.descriptions ?? [],
      };
    });

  const skills: CvSkill[] = nodes
    .filter(n => n.data.category === 'skill')
    .map(n => {
      const meta = n.data.meta as { originalId?: string; essential?: boolean; skillMeta?: Record<string, unknown> } | undefined;
      return {
        id: meta?.originalId ?? n.id.replace('skill:', ''),
        label: n.data.name,
        category: n.data.properties['category'] ?? 'general',
        essential: meta?.essential ?? false,
        level: n.data.properties['level'] || null,
        meta: meta?.skillMeta ?? {},
      };
    });

  const demonstrates = edges
    .filter(e => e.data?.relationType === 'demonstrates')
    .map(e => ({
      id: e.id.replace('demonstrates:', ''),
      source: e.source.replace('entry:', ''),
      target: e.target.replace('skill:', ''),
      description_keys: [],
    }));

  return {
    ...original,
    entries,
    skills,
    demonstrates,
  };
}
```

- [ ] **Step 2: Verify TypeScript compiles**

```bash
cd apps/review-workbench && npm run build 2>&1 | grep -E "error|warning" | head -20
```
Expected: no type errors.

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/base-cv/lib/cvToGraph.ts apps/review-workbench/src/pages/global/KnowledgeGraph.tsx
git commit -m "feat(ui): add cvToGraph adapter with meta passthrough"
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.