---
identity:
  node_id: "doc:wiki/drafts/5_archivos_a_crear.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md", relation_type: "documents"}
---

```

## Details

```
src/features/portfolio/
  api/
    usePortfolioSummary.ts        useQuery(['portfolio','summary'])
  components/
    PortfolioTable.tsx            tabla principal con Badge de status
    DeadlineSidebar.tsx           lista de deadlines
    RecentArtifacts.tsx           3 cards estáticos (mock data)
    SystemStatus.tsx              dot decorativo
src/pages/global/
  PortfolioDashboard.tsx          TONTO: useParams no necesario, solo hook + layout
src/components/atoms/
  Badge.tsx                       REQUERIDO por PortfolioTable (ya en phase_0)
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md`.