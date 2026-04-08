---
identity:
  node_id: "doc:wiki/drafts/file_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

### Backend (`src/doc_router/`)

## Details

### Backend (`src/doc_router/`)

```
src/doc_router/
  __init__.py              # Package init, version
  cli.py                   # Click CLI entrypoint (init, scan, lint, graph, serve)
  config.py                # Load/validate doc-router.yml
  models.py                # TaggedEntity, RouteNode, RouteEdge, RouteGraph dataclasses
  scanner/
    __init__.py
    markdown.py            # Parse YAML frontmatter from .md files
    python.py              # Parse :doc-*: from Python docstrings
    typescript.py           # Parse @doc-* from JSDoc (stub for Phase 1)
    registry.py            # Scanner registry — maps file extensions to parsers
  graph.py                 # Graph builder — resolve references, detect broken links, compute stats
  linter.py                # Validate tags against vocabulary, check required fields
  server.py                # FastAPI app — serve graph JSON + static UI
```

### Frontend (`ui/`)

```
ui/
  package.json
  vite.config.ts
  tsconfig.json
  tsconfig.app.json
  index.html
  src/
    main.tsx               # React root
    App.tsx                 # Router (single route: graph explorer)
    styles.css             # Terran Command design system (copied from review-workbench)
    utils/cn.ts            # Class merge utility (copied)
    api/
      client.ts            # Fetch graph from FastAPI backend
    types/
      graph.types.ts       # RouteNode, RouteEdge, RouteGraph TypeScript types
    components/
      atoms/
        Badge.tsx           # Copied from review-workbench
        Button.tsx          # Copied from review-workbench
        Icon.tsx            # Copied from review-workbench
        Spinner.tsx         # Copied from review-workbench
        Tag.tsx             # Copied from review-workbench
      molecules/
        ControlPanel.tsx    # Adapted — show node tags, linked files
        SplitPane.tsx       # Copied from review-workbench
      layouts/
        AppShell.tsx        # Simplified — doc-router branding, no job nav
    features/
      graph-explorer/
        components/
          RouteGraphCanvas.tsx    # React Flow canvas for route graph
          DocNode.tsx             # Custom node for doc-type entities
          CodeNode.tsx            # Custom node for code-type entities
          RouteEdge.tsx           # Custom edge with type label
          NodeInspector.tsx       # Right panel — show node details on click
          FilterBar.tsx           # Domain/stage/nature filter controls
        hooks/
          useRouteGraph.ts        # TanStack Query hook — fetch + filter graph
        lib/
          layout.ts              # Dagre layout for route graph
          colors.ts              # Domain → hue mapping
```

### Tests

```
tests/
  conftest.py                    # Fixtures: sample doc-router.yml, sample tagged files
  test_config.py                 # Config loading/validation
  test_scanner_markdown.py       # Frontmatter parsing
  test_scanner_python.py         # Docstring tag parsing
  test_graph.py                  # Graph building, broken link detection
  test_linter.py                 # Vocabulary validation, required fields
  test_cli.py                    # CLI integration tests (click.testing.CliRunner)
  test_server.py                 # FastAPI endpoint tests
  fixtures/
    sample_project/
      doc-router.yml             # Sample config
      docs/
        design.md                # Tagged doc (frontmatter)
        architecture.md          # Tagged doc (depends_on)
      src/
        module.py                # Tagged Python file (docstrings)
        empty.py                 # No tags (orphan)
```

### Root

```
doc-router.yml                   # PhD 2.0 project config (first consumer)
pyproject.toml                   # Package config, CLI entrypoint
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.