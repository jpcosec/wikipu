---
identity:
  node_id: "doc:wiki/drafts/2_contrato_de_datos_api_i_o.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md", relation_type: "documents"}
---

**Lectura:**

## Details

**Lectura:**
- `GET /api/v2/query/portfolio/summary` → `PortfolioSummary`
  ```ts
  {
    totals: { jobs, completed, pending_hitl, running, failed, archived },
    jobs: JobListItem[]  // { source, job_id, thread_id, current_node, status, updated_at }
  }
  ```
  Status values: `running` · `pending_hitl` · `completed` · `failed` · `archived`

**Escritura:** Ninguna. Vista de solo lectura.

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md`.