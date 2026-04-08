---
identity:
  node_id: "doc:wiki/drafts/4_estilos_terran_command.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md", relation_type: "documents"}
---

- Fondo: `bg-surface`

## Details

- Fondo: `bg-surface`
- Tabla header sticky: `bg-surface-container/95 backdrop-blur-sm`
- Filas hover: `hover:bg-primary/5`
- Sidebar deadlines: `alert-glow`
- Panel main: `tactical-glow`
- Nombre app: `font-headline font-black uppercase tracking-tighter text-primary`
- Headers sección: `font-mono text-[11px] uppercase tracking-[0.2em] text-outline`
- Celdas: `font-mono text-[11px]`

**Interacciones:**
- Click en fila → `navigate(/jobs/:source/:jobId)`
- `Ctrl+K` → abre search bar (futura implementación)
- FAB hover → `brightness-110`, active → `scale-[0.98]`

**Estado Vacío:** panel `terminal` icon + `NO_ACTIVE_MISSIONS`
**Estado Error:** banner amber mono si falla `getPortfolioSummary`

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/A1_portfolio_dashboard.md`.