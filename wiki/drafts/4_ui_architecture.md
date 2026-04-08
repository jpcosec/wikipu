---
identity:
  node_id: "doc:wiki/drafts/4_ui_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

Single local web app served by `doc-router serve`. Reuses PhD graph editor (React Flow) and workbench components (CodeMirror, Tailwind atoms).

## Details

Single local web app served by `doc-router serve`. Reuses PhD graph editor (React Flow) and workbench components (CodeMirror, Tailwind atoms).

### 4.1 Graph Explorer (Phase 1)

- Interactive graph of all tagged entities
- Filter by domain, stage, nature
- Click node → tags, content preview, linked nodes
- Color-coded by domain, shape-coded by nature
- Edge types visually distinct (implements, depends_on, contract)

### 4.2 Drift Dashboard (Phase 2)

- Health overview: green/yellow/red per domain and stage
- List of drift issues with severity
- Click issue → navigate to file in editor
- Historical trend stored in `.doc-router/history/`

### 4.3 Document & Code Editor (Phase 3)

- Split pane: rendered preview + source editor
- Markdown editor with frontmatter-aware editing
- Syntax-highlighted code view with tag regions highlighted
- Template insertion commands
- Save writes back to filesystem

### 4.4 Task Generator & Correction View (Phase 4-5)

- Select task type (implement, test, fix, review)
- Describe task, provide domain/stage coordinates
- See resolved context graph (which nodes selected, why)
- Edit/correct packet before exporting
- Correction history: track changes to generated packets, feed back into template refinement

#### Correction History Model

Corrections are stored in `.doc-router/corrections/`:

```json
{
  "id": "corr-2026-03-22-001",
  "timestamp": "2026-03-22T14:30:00Z",
  "packet_id": "implement-pipeline-match-001",
  "domain": "pipeline",
  "stage": "match",
  "type": "implement",
  "changes": [
    {
      "field": "context",
      "action": "added",
      "value": "src/nodes/match/contract.py",
      "reason": "Compiler missed the contract file"
    },
    {
      "field": "constraints",
      "action": "removed",
      "value": "src/core/graph/state.py",
      "reason": "This file does need modification for the new field"
    }
  ]
}
```

Over time, corrections reveal patterns: "the compiler always misses contract files for pipeline tasks" → adjust the edge-following rules or templates.

### 4.5 Tech Stack

| Component | Technology | Notes |
|-----------|------------|-------|
| Frontend | React + Tailwind | Reuse PhD workbench atoms/molecules |
| Graph | React Flow | Reuse PhD graph editor |
| Editor | CodeMirror | Already in PhD workbench |
| Backend | FastAPI | Serves API + static UI + MCP |
| Data | Filesystem | Scanned graph cached as `.doc-router/cache.json` |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.