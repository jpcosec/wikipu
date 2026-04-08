---
identity:
  node_id: "doc:wiki/drafts/3_backend_api.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

### Plans Domain

## Details

### Plans Domain

```
GET  /api/plans                         → [{group, latest_type, latest_version, status, domain}]
GET  /api/plans/{group}                 → {group, chain: [{type, version, status, id}]}
GET  /api/plans/{group}/{type}_{ver}    → {metadata: {...}, content: "markdown body"}
PUT  /api/plans/{group}/{type}_{ver}    → save review (writes review_{group}_N.md to disk)
```

### File Tree Domain

```
GET  /api/files?path=/                  → [{name, path, is_dir, extension, child_count}]
GET  /api/files/content?path=xxx        → {path, content, language}
GET  /api/files/touched?group=xxx&ver=0 → [{path, symbol?, lines?}] (annotated touch list)
```

### Existing Endpoints (enhanced)

```
GET  /api/graph?group=xxx               → RouteGraph filtered to nodes whose paths appear in the plan's touches list
```

The `group` filter loads the active plan for that group, extracts its `touches` paths, and filters the graph to only nodes matching those paths. This is a cross-domain query (plans + graph) handled in the server layer.

All other existing endpoints (`/api/stats`, `/api/nodes/{id}`, `/api/rescan`) remain unchanged.

### PUT Request Body Schema

```json
{
  "content": "# Edited plan markdown...",
  "file_tags": [
    {"file": "src/foo.py", "lines": [10, 20], "comment": "needs fix"}
  ],
  "graph_changes": [
    {"action": "add_touch", "target": "src/bar.py", "comment": "reason"}
  ],
  "touches": [
    {"path": "src/foo.py"},
    {"path": "src/bar.py", "symbol": "MyClass"}
  ]
}
```

The server merges these into the review file's YAML frontmatter + markdown body.

### Error Handling

| Endpoint | Error | HTTP Status |
|----------|-------|-------------|
| `GET /api/plans/{group}` | Group not found | 404 |
| `GET /api/plans/{group}/{type}_{ver}` | File not found | 404 |
| `PUT /api/plans/{group}/{type}_{ver}` | `type` not "review" (cannot overwrite plans) | 403 |
| `PUT /api/plans/{group}/{type}_{ver}` | Parent plan does not exist | 409 |
| `GET /api/files?path=` | Path outside project root | 403 |
| `GET /api/files/content?path=` | File not found | 404 |
| `GET /api/files/content?path=` | File exceeds 1MB size limit | 413 |

### Security

All file tree endpoints are sandboxed to `project_root`. Path traversal attempts (e.g. `../../etc/passwd`) return 403. Paths are resolved and checked against `project_root` before any filesystem access.

### Backend Modules

| Module | Responsibility |
|--------|---------------|
| `src/doc_router/plans.py` | Plan discovery, iteration chain logic, read/write plan files, parse/update frontmatter, status transitions |
| `src/doc_router/filetree.py` | Directory listing, file content reading, language detection, touch annotation |
| `src/doc_router/server.py` | New route handlers for plans and files endpoints (additions to existing server) |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.