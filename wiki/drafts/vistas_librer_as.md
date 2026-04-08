---
identity:
  node_id: "doc:wiki/drafts/vistas_librer_as.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md", relation_type: "documents"}
---

| Spec | Vista | Layout | Componentes Core | Librerías |

## Details

| Spec | Vista | Layout | Componentes Core | Librerías |
|------|-------|--------|-----------------|-----------|
| A1 | Portfolio Dashboard | Grid 9/3 | `<PortfolioTable>` `<ProgressSegmented>` | `react-router-dom` · `@tanstack/react-query` |
| A2 | Data Explorer | `<SplitPane>` | `<IntelligentEditor>` `<FileTree>` | `react-resizable-panels` · `lucide-react` |
| A3 | Base CV Editor | Grid 70/30 | `<GraphCanvas>` `<NodeInspectorSidebar>` | `@xyflow/react` · `dagre` |
| B0 | Job Flow Inspector | Columna única | `<PipelineTimeline>` `<HitlCtaBanner>` | `@tanstack/react-query` (polling) |
| B1 | Scrape Diagnostics | Columna + Control | `<DiagnosticCard>` `<ImagePreview>` | Nativas React/Tailwind |
| B2 | Extract & Understand | `<SplitPane>` | `<IntelligentEditor>` `<RequirementList>` | `react-resizable-panels` · `@uiw/react-codemirror` |
| B3 | Match | `<SplitPane>` | `<GraphCanvas>` `<EvidenceBankSidebar>` | `@xyflow/react` · `@dnd-kit/core` |
| B4 | Generate Documents | `<SplitPane>` | `<IntelligentEditor>` `<DocumentTabs>` | `react-resizable-panels` · `@uiw/react-codemirror` (diff) |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md`.