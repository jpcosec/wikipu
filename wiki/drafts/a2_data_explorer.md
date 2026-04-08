---
identity:
  node_id: "doc:wiki/drafts/a2_data_explorer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md", relation_type: "documents"}
---

**Route:** `/explorer`

## Details

**Route:** `/explorer`
**Feature:** `features/explorer/`
**Libraries:** `react-resizable-panels` · `@uiw/react-codemirror` · `lucide-react`

### Layout

```
┌── col-left (30%) ─────┬── col-right (70%) ───────────────────┐
│ Path breadcrumb        │ [header: ruta actual + tipo]         │
│                        │                                      │
│ ► tu_berlin/           │  Si directorio: grid de archivos    │
│   ► 201397/           │  Si archivo JSON: CodeMirror         │
│     ► nodes/          │  Si imagen: img centrada              │
└────────────────────────┴──────────────────────────────────────┘
```

### Components
- `<ExplorerTree>` — Recursive collapsible tree, icons by type
- `<BreadcrumbNav>` — Clickable path segments
- `<FilePreview>` — Dispatcher: JSON / MD / image / binary
- `<JsonPreview>` — CodeMirror read-only with syntax highlighting

### API Contract

**Read:**
- `GET /api/v1/explorer/browse?path=<path>` → `ExplorerPayload`

```ts
{
  path: string,
  is_dir: boolean,
  entries?: ExplorerEntry[],
  content_type?: "text" | "image" | "binary",
  content?: string | null
}
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/views.md`.