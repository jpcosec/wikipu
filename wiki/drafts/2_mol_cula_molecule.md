---
identity:
  node_id: "doc:wiki/drafts/2_mol_cula_molecule.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md", relation_type: "documents"}
---

Agrupación simple de átomos. SplitPane, DiagnosticCard, ControlPanel.

## Details

Agrupación simple de átomos. SplitPane, DiagnosticCard, ControlPanel.

**Reglas:**
- Componente "tonto" — recibe datos por props, no hace `useQuery`
- Puede tener micro-estado visual local (hover, open/closed)
- Siempre exporta la interface de props (la necesitarán los tests)

```tsx
import { cn } from '@/utils/cn';
import { Badge } from '@/components/atoms/Badge';
import { Button } from '@/components/atoms/Button';

export interface MoleculeNameProps extends React.HTMLAttributes<HTMLDivElement> {
  title: string;
  status: 'verified' | 'pending' | 'error';
  onAction?: () => void;
}

export function MoleculeName({ title, status, onAction, className, ...props }: MoleculeNameProps) {
  return (
    <div
      className={cn('flex flex-col gap-3 p-4 bg-surface-high panel-border', className)}
      {...props}
    >
      <div className="flex justify-between items-center">
        <h3 className="font-headline text-sm font-bold text-on-surface">{title}</h3>
        <Badge variant={status === 'error' ? 'danger' : status === 'verified' ? 'success' : 'muted'}>
          {status}
        </Badge>
      </div>
      <div className="flex justify-end">
        <Button variant="ghost" size="sm" onClick={onAction}>
          Revisar
        </Button>
      </div>
    </div>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md`.