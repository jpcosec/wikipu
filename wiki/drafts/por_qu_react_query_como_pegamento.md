---
identity:
  node_id: "doc:wiki/drafts/por_qu_react_query_como_pegamento.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md", relation_type: "documents"}
---

En lugar de `useEffect` + `useState(loading)` por cada llamada:

## Details

En lugar de `useEffect` + `useState(loading)` por cada llamada:

```ts
// Antes (feo)
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
useEffect(() => { fetch(...).then(setData).finally(() => setLoading(false)) }, [jobId]);

// Con React Query
const { data: jobTimeline, isLoading } = useQuery({
  queryKey: ['timeline', source, jobId],
  queryFn: () => getJobTimeline(source, jobId),
});
```

Out of the box: caché, reintentos automáticos si el backend falla, background-refetch,
invalidación de caché en mutations, y devtools para inspeccionar el estado.
El mock client ya tiene las mismas firmas — cambiar `VITE_MOCK=true/false` es transparente.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md`.