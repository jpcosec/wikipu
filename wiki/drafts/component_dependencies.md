---
identity:
  node_id: "doc:wiki/drafts/component_dependencies.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

```

## Details

```
AppShell
└── LeftNav
    ├── Icon (nav items)
    └── Badge (active indicator)

JobWorkspaceShell
├── PipelineTimeline (TopBar)
├── LeftNav (mini)
└── <Outlet />

SplitPane
└── react-resizable-panels

IntelligentEditor
├── CodeMirror (@uiw/react-codemirror)
├── Tag (for highlights)
└── Badge (for line numbers)

GraphCanvas
├── @xyflow/react
├── dagre (layout)
├── Badge (score badges)
└── Icon (node icons)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.