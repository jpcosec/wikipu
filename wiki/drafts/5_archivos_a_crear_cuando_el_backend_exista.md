---
identity:
  node_id: "doc:wiki/drafts/5_archivos_a_crear_cuando_el_backend_exista.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/B3b_application_context.md", relation_type: "documents"}
---

```

## Details

```
src/features/job-pipeline/
  api/
    useApplicationContext.ts      useQuery(['context', source, jobId])
    useContextDecision.ts         useMutation
  components/
    ContextBrief.tsx              panel narrative
    MatchReferencePanel.tsx       scores del match
    ContextDecisionBar.tsx        botones de decisión
src/pages/job/
  ApplicationContext.tsx          TONTO: useParams + hooks + render
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/B3b_application_context.md`.