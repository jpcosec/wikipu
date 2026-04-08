---
identity:
  node_id: "doc:wiki/drafts/3_frontend_implementation_gap_analysis.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md", relation_type: "documents"}
---

### 3.1 Views Implemented vs Spec

## Details

### 3.1 Views Implemented vs Spec

| View | Route | Status | Missing |
|---|---|---|---|
| Portfolio Dashboard | `/` | ✅ Implemented | — |
| Data Explorer | `/explorer` | ✅ Implemented | Explorer file write (`PUT /commands/explorer/file`) wired up |
| Base CV Editor | `/cv` | ✅ Implemented | Save (`PUT /commands/profile/cv-profile-graph`) wired to mock only |
| Knowledge Graph | `/graph` | ✅ Implemented | — |
| Job Flow Inspector | `/jobs/:s/:j` | ✅ Implemented | Pipeline run/resume buttons call mock only |
| Scrape Diagnostics | `/jobs/:s/:j/scrape` | ✅ Implemented | Scrape trigger (`POST /commands/jobs/scrape`) mock only |
| Translate Diagnostics | `/jobs/:s/:j/translate` | ✅ Implemented | — |
| Extract & Understand | `/jobs/:s/:j/extract` | ✅ Implemented | Gate decide wired to mock only |
| Match | `/jobs/:s/:j/match` | ✅ Implemented | Gate decide wired to mock only |
| Application Context | `/jobs/:s/:j/context` | ❌ **Not implemented** | Entire view missing (spec: B3b) |
| Generate Documents | `/jobs/:s/:j/sculpt` | ✅ Implemented | Gate decide mock only; diff view not implemented |
| Package & Deployment | `/jobs/:s/:j/deployment` | ✅ Implemented | Archive command mock only |

### 3.2 API Hook Coverage

| Hook file | Endpoint called | Works with real API? |
|---|---|---|
| `usePortfolioSummary` | `query/portfolio/summary` | ❌ URL mismatch (v1 vs v2) |
| `useJobTimeline` | `query/jobs/.../timeline` | ❌ URL mismatch |
| `useViewExtract` | `query/jobs/.../views/extract` | ❌ view2 vs views/extract |
| `useViewMatch` | `query/jobs/.../views/match` | ❌ view1 vs views/match |
| `useGateDecide` | `commands/jobs/.../gates/.../decide` | ❌ not implemented in backend |
| `useEditorState` | `query/jobs/.../editor/.../state` | ❌ URL mismatch |
| `useCvProfileGraph` | `query/profile/cv-profile-graph` | ❌ portfolio vs profile |
| `useExplorerBrowse` | `query/explorer/browse` | ❌ URL mismatch |
| `useArtifacts` | `query/jobs/.../artifacts/{node}` | ❌ stage outputs vs artifacts |

All hooks work correctly with mock data. None work with the real `dev` backend until Phase M-1 is complete.

### 3.3 Missing UI Features (from spec docs)

From `docs/ui/ui_view_spec.md` (dev) and `docs/runtime/ui/views.md` (methodology):

#### Extract view gaps
- No difficulty rating per requirement
- No requirement category chip (technical / soft_skill / language)
- No confidence score display

#### Match view gaps
- No per-edge confidence bar
- No coverage summary header (X/Y requirements matched)
- No evidence bank sidebar linkage (panel exists but not wired to selection)

#### Generate Documents view gaps
- No diff view (proposed vs approved)
- No per-section sculpting controls
- No version history

#### Pipeline execution
- No real pipeline run/resume button wiring (all mock)
- No real-time status polling via `/system/orchestration/threads/`
- No error trace display via LangSmith

#### Application Context view (B3b)
- Entire view not implemented — spec exists at `plan/01_ui/specs/B3b_application_context.md`

---

Generated from `raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md`.