---
identity:
  node_id: "doc:wiki/drafts/las_3_reglas_de_oro.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md", relation_type: "documents"}
---

### Regla 1 — Las `pages/` son tontas, las `features/` son listas

## Details

### Regla 1 — Las `pages/` son tontas, las `features/` son listas

Un archivo en `pages/` tiene exactamente tres responsabilidades:

1. Leer parámetros de URL (`useParams`)
2. Llamar al hook de datos de la feature (`useExtractState(jobId)`)
3. Renderizar el layout inyectando los componentes de la feature

```tsx
// pages/job/ExtractPage.tsx — correcto
export function ExtractPage() {
  const { source, jobId } = useParams();
  const { data, isLoading } = useExtractState(source!, jobId!);
  return <JobWorkspaceShell><ExtractView data={data} loading={isLoading} /></JobWorkspaceShell>;
}
```

**Si tu Page tiene más de ~80 líneas, estás poniendo lógica donde no va.**

---

### Regla 2 — Feature-Sliced evita el acoplamiento

Agrupar por feature (no por tipo de archivo) significa que borrar o rediseñar una vista
no contamina el resto de la app. Toda la lógica de Match vive y muere en `features/job-pipeline/`.

```
# MAL — agrupa por tipo (el clásico que escala fatal)
hooks/useMatchState.ts
hooks/useExtractState.ts
components/MatchPanel.tsx
components/RequirementList.tsx

# BIEN — agrupa por feature
features/job-pipeline/api/useMatchState.ts
features/job-pipeline/api/useExtractState.ts
features/job-pipeline/components/MatchPanel.tsx
features/job-pipeline/components/RequirementList.tsx
```

---

### Regla 3 — `cn()` para todos los átomos

Los componentes base (`<Button>`, `<Badge>`, etc.) reciben `className` como prop para
permitir overrides contextuales. Sin `cn()`, Tailwind genera clases duplicadas que se
anulan de forma impredecible.

```ts
// utils/cn.ts
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

Uso en cualquier átomo:

```tsx
// components/atoms/Button.tsx
export function Button({ className, ...props }) {
  return (
    <button className={cn("bg-primary text-primary-on font-headline uppercase", className)} {...props} />
  );
}

// Llamada con override — bg-secondary gana limpio, sin colisión
<Button className="bg-secondary text-secondary-on" />
```

**Instalar antes de escribir el primer átomo:**
```bash
npm install clsx tailwind-merge
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md`.