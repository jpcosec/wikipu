---
identity:
  node_id: "doc:wiki/drafts/6_estructura_de_archivos_esperada.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

src/

## Details

src/
  features/
    [nombre-feature]/
      api/
        use[NombreHook].ts          ← useQuery / useMutation
      components/
        [Organismo].tsx             ← UI compleja de la vista
        [Molécula].tsx              ← subcomponentes
  pages/
    job/
      [NombrePage].tsx              ← TONTO: useParams + hook + render

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.