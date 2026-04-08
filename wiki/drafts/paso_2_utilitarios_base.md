---
identity:
  node_id: "doc:wiki/drafts/paso_2_utilitarios_base.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md", relation_type: "documents"}
---

### `src/utils/cn.ts`

## Details

### `src/utils/cn.ts`

```ts
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

### `src/main.tsx` — Providers

```tsx
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import App from './App';
import './styles.css';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: { staleTime: 30_000, retry: 1 },
  },
});

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </StrictMode>,
);
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md`.