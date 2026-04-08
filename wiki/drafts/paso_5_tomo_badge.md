---
identity:
  node_id: "doc:wiki/drafts/paso_5_tomo_badge.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md", relation_type: "documents"}
---

Necesario para `PortfolioTable`. Primer átomo del sistema.

## Details

Necesario para `PortfolioTable`. Primer átomo del sistema.

```tsx
// src/components/atoms/Badge.tsx
import { cn } from '../../utils/cn';

const VARIANTS = {
  primary:   'bg-primary/15 text-primary border border-primary/30',
  secondary: 'bg-secondary/15 text-secondary border border-secondary/30',
  success:   'bg-primary/10 text-primary-dim border border-primary/20',
  danger:    'bg-error-container/20 text-error border border-error/30',
  muted:     'bg-surface-high text-on-muted border border-outline/20',
};

interface Props {
  variant?: keyof typeof VARIANTS;
  className?: string;
  children: React.ReactNode;
}

export function Badge({ variant = 'muted', className, children }: Props) {
  return (
    <span className={cn('inline-flex items-center px-2 py-0.5 text-[10px] font-mono uppercase tracking-widest', VARIANTS[variant], className)}>
      {children}
    </span>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md`.