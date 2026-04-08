---
identity:
  node_id: "doc:wiki/drafts/direcci_n_del_flujo_de_datos.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md", relation_type: "documents"}
---

```

## Details

```
API (mock o real)
  └── React Query hook (features/*/api/)
        └── Page (lee params, llama hook)
              └── Feature component (recibe data via props)
                    └── Organism / Molecule / Atom (UI pura)
```

- Las capas de abajo **nunca** importan de las capas de arriba
- Los `atoms/` y `molecules/` no saben nada del backend
- Los `features/` no importan entre sí (máximo via `types/`)

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_architecture.md`.