---
identity:
  node_id: "doc:wiki/drafts/task_11_frontend_project_setup_design_system.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `ui/package.json`
- Create: `ui/vite.config.ts`
- Create: `ui/tsconfig.json`
- Create: `ui/tsconfig.app.json`
- Create: `ui/index.html`
- Create: `ui/src/main.tsx`
- Create: `ui/src/App.tsx`
- Create: `ui/src/styles.css` (copy from review-workbench)
- Create: `ui/src/utils/cn.ts` (copy from review-workbench)

- [ ] **Step 1: Create package.json**

```json
{
  "name": "doc-router-ui",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@dagrejs/dagre": "^1.1.5",
    "@tanstack/react-query": "^5.94.5",
    "@xyflow/react": "^12.10.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.577.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-resizable-panels": "^4.7.4",
    "tailwind-merge": "^3.5.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.0.17",
    "@types/react": "^18.3.23",
    "@types/react-dom": "^18.3.7",
    "@vitejs/plugin-react": "^4.4.1",
    "tailwindcss": "^4.0.17",
    "typescript": "^5.8.2",
    "vite": "^5.4.14"
  }
}
```

- [ ] **Step 2: Create vite.config.ts**

```typescript
// ui/vite.config.ts
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: "127.0.0.1",
    port: 5174,
    proxy: {
      "/api": "http://127.0.0.1:8030",
    },
  },
});
```

- [ ] **Step 3: Create tsconfig files**

```json
// ui/tsconfig.json
{ "files": [], "references": [{ "path": "./tsconfig.app.json" }] }
```

```json
// ui/tsconfig.app.json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "Bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["src"]
}
```

- [ ] **Step 4: Create index.html**

```html
<!-- ui/index.html -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Doc-Router</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

- [ ] **Step 5: Copy styles.css from review-workbench**

Source: `/home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench/src/styles.css`

Copy to `ui/src/styles.css`. No modifications needed — the Terran Command theme is project-agnostic.

- [ ] **Step 6: Copy cn.ts utility**

```typescript
// ui/src/utils/cn.ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

- [ ] **Step 7: Create main.tsx and App.tsx**

```typescript
// ui/src/main.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";

const queryClient = new QueryClient();

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </StrictMode>,
);
```

```typescript
// ui/src/App.tsx
export default function App() {
  return (
    <div className="min-h-screen bg-[var(--color-background)] text-[var(--color-on-surface)]">
      <div className="flex items-center justify-center h-screen">
        <h1 className="font-headline text-2xl tracking-widest uppercase text-[var(--color-primary)]">
          Doc-Router
        </h1>
      </div>
    </div>
  );
}
```

- [ ] **Step 8: Create .gitignore**

```
# ui/.gitignore
node_modules/
dist/
```

- [ ] **Step 9: Install and verify**

```bash
cd ui && npm install && npm run dev
```

Expected: Dev server on http://127.0.0.1:5174, showing "DOC-ROUTER" in cyan on dark background.

- [ ] **Step 10: Commit**

```bash
git add ui/
git commit -m "feat(doc-router): frontend scaffold with Terran Command design system"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.