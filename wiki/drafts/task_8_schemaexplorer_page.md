---
identity:
  node_id: "doc:wiki/drafts/task_8_schemaexplorer_page.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md", relation_type: "documents"}
---

**Files:**

## Details

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

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-24-schema-explorer.md`.