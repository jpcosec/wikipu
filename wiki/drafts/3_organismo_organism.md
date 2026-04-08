---
identity:
  node_id: "doc:wiki/drafts/3_organismo_organism.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md", relation_type: "documents"}
---

Secciones complejas: IntelligentEditor, GraphCanvas, RequirementList, EvidenceBankSidebar.

## Details

Secciones complejas: IntelligentEditor, GraphCanvas, RequirementList, EvidenceBankSidebar.

**Reglas:**
- Pueden vivir en `src/features/.../components/`
- Pueden tener `useState` para estado UI local (tabs, acordeones, hover)
- Reciben datos complejos como props — no hacen `useQuery` directamente
- Delegan mutaciones al hook padre vía callbacks
- Early returns para `isLoading` y `isEmpty`

```tsx
import { useState } from 'react';
import { cn } from '@/utils/cn';
import { MoleculeName } from '@/components/molecules/MoleculeName';

export interface OrganismNameProps {
  items: Array<{ id: string; title: string; status: 'verified' | 'pending' | 'error' }>;
  isLoading?: boolean;
  onItemUpdate: (id: string, data: unknown) => void;
  className?: string;
}

export function OrganismName({ items, isLoading, onItemUpdate, className }: OrganismNameProps) {
  const [expandedId, setExpandedId] = useState<string | null>(null);

  if (isLoading) {
    return (
      <div className={cn('p-8 flex justify-center text-on-muted font-mono text-sm', className)}>
        Loading...
      </div>
    );
  }

  if (!items.length) {
    return (
      <div className={cn('p-8 text-center border border-dashed border-outline/30 text-on-muted font-mono text-sm', className)}>
        No items.
      </div>
    );
  }

  return (
    <section className={cn('flex flex-col gap-2 w-full', className)}>
      {items.map((item) => (
        <MoleculeName
          key={item.id}
          title={item.title}
          status={item.status}
          onAction={() => {
            setExpandedId(item.id === expandedId ? null : item.id);
            onItemUpdate(item.id, { viewed: true });
          }}
          className={item.id === expandedId ? 'border-primary tactical-glow' : ''}
        />
      ))}
    </section>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md`.