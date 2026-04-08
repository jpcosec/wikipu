---
identity:
  node_id: "doc:wiki/drafts/orden_de_implementaci_n.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md", relation_type: "documents"}
---

> Fuente de verdad: `plan/index_checklist.md`

## Details

> Fuente de verdad: `plan/index_checklist.md`

```
Fase 0  → Foundation: cn.ts, main.tsx, AppShell, JobWorkspaceShell, Badge, PortfolioDashboard, mock toggle, types/
Fase 1  → B0 JobFlowInspector (PipelineTimeline, sin librerías externas)
Fase 2  → A2 DataExplorer (FileTree + IntelligentEditor modo fold)
Fase 3  → B1 ScrapeDiagnostics (metadata + texto + screenshot)
Fase 4  → B2 ExtractUnderstand (CodeMirror + RequirementList + SourceTextPane)
Fase 5  → B3 Match (ReactFlow + dagre + dnd-kit + EvidenceBankPanel)
Fase 6  → B4 GenerateDocuments PREP_MATCH (CodeMirror + DocumentTabs)
Fase 7  → B5 PackageDeployment (checklist + file download)
Fase 8  → B4b Default Document Gates ⚠️ BLOCKED — requiere backend
Fase 9  → A3 BaseCvEditor (ReactFlow modo CV)
Fase 10 → B3b ApplicationContext ⚠️ BLOCKED — requiere backend
```

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/migration_agent_prompt.md`.