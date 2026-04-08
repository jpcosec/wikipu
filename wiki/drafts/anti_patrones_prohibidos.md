---
identity:
  node_id: "doc:wiki/drafts/anti_patrones_prohibidos.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md", relation_type: "documents"}
---

| Prohibido | Correcto |

## Details

| Prohibido | Correcto |
|-----------|----------|
| `style={{ color: '#00f2ff' }}` | `className="text-primary"` |
| `useEffect + fetch` para datos del servidor | `useQuery` de React Query |
| Lógica de negocio en `pages/` | Todo en `features/` |
| `className="bg-blue-500"` en un átomo sin `cn()` | `cn('bg-primary', className)` |
| Crear un archivo `.css` nuevo | Tailwind utilities o `@layer utilities` en `styles.css` |
| Datos literales hardcodeados en componentes (`const jobs = [...]`) | Todo dato viene del mock/API via `useQuery` — nunca arrays estáticos en el render |

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/component_templates.md`.