---
identity:
  node_id: "doc:wiki/drafts/vistas_y_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md", relation_type: "documents"}
---

| Spec | Vista | Layout Base | Main | Secundarios |

## Details

| Spec | Vista | Layout Base | Main | Secundarios |
|------|-------|-------------|------|-------------|
| A1 | Portfolio Dashboard | Grid 9/3 | `<PortfolioTable>` `<ProgressSegmented>` | `<DeadlineSensors>` `<SystemStats>` |
| A2 | Data Explorer | `<SplitPane>` 30/70 | `<IntelligentEditor mode="fold">` | `<FileTree>` |
| A3 | Base CV Editor | Grid 70/30 | `<GraphCanvas>` (nodos CV/Skills) | `<NodeInspectorSidebar>` |
| B0 | Job Flow Inspector | Columna única | `<PipelineTimeline>` `<HitlCtaBanner>` | — |
| B1 | Scrape Diagnostics | Columna + Control | `<DiagnosticCard>` `<ImagePreview>` | `<ScrapeControlPanel>` |
| B2 | Extract & Understand | `<SplitPane>` 50/50 | `<IntelligentEditor mode="tag-hover">` `<RequirementList>` | `<ExtractControlPanel>` |
| B3 | Match | `<SplitPane>` 3 col | `<GraphCanvas>` (edges evaluados) | `<EvidenceBankSidebar>` `<MatchControlPanel>` |
| B4 | Generate Documents | `<SplitPane>` 50/50 | `<IntelligentEditor mode="diff">` `<DocumentTabs>` | `<PackageControlPanel>` |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md`.