---
identity:
  node_id: "doc:wiki/drafts/1_tomo_atom.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md", relation_type: "documents"}
---

Elementos indivisibles: Button, Badge, Tag, Kbd, Spinner.

## Details

Elementos indivisibles: Button, Badge, Tag, Kbd, Spinner.

**Reglas:**
- Siempre `forwardRef` — librerías de D&D, tooltips y focus management lo necesitan
- Sin estado complejo, sin llamadas a API
- La prop `className` siempre va al final del `cn()` para que el padre pueda sobrescribir

```tsx
import { forwardRef } from 'react';
import { cn } from '@/utils/cn';

export interface ComponentNameProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  // className y children vienen incluidos en HTMLAttributes
}

export const ComponentName = forwardRef<HTMLDivElement, ComponentNameProps>(
  ({ className, variant = 'primary', size = 'md', children, ...props }, ref) => {

    const baseStyles = 'inline-flex items-center justify-center transition-colors';

    const variants = {
      primary:   'bg-primary/10 text-primary border border-primary/30',
      secondary: 'bg-secondary/10 text-secondary border border-secondary/30',
      ghost:     'bg-transparent text-on-muted hover:text-on-surface',
    };

    const sizes = {
      sm: 'px-2 py-0.5 text-[10px]',
      md: 'px-4 py-2 text-xs',
      lg: 'px-6 py-3 text-sm',
    };

    return (
      <div
        ref={ref}
        className={cn(baseStyles, variants[variant], sizes[size], className)}
        {...props}
      >
        {children}
      </div>
    );
  }
);

ComponentName.displayName = 'ComponentName';
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md`.