---
status: open
priority: p2
depends_on: [owl-phase1-parallel-run]
created: 2026-04-17
assigned_to: self
---

# Phase 2: Quadstore as Primary Backend

## Objective

Parse Markdown files into quadstore on load. YAML frontmatter edges become OWL triples. Implement `SyncGate` for bidirectional sync.

## Tasks

- [ ] Implement `SyncGate` class in `src/wiki_compiler/sync_gate.py`
  - [ ] `export_to_owl(node)` - Pydantic → OWL
  - [ ] `import_from_owl(uri)` - OWL → Pydantic
  - [ ] `_shacl_validate()` - validate before commit
  - [ ] `sync()` - full bidirectional sync with conflict detection
- [ ] Parse wiki-links as `:references` properties during build
- [ ] Extract tables as enumerated classes where applicable
- [ ] Replace `.search()` with SPARQL queries behind the scenes
- [ ] Deprecate direct graph access, use quadstore API
- [ ] Add conflict detection to audit command

## Verification

```bash
wiki-compiler build  # Should populate quadstore
wiki-compiler query "SELECT ?x WHERE { ?x :references :autopoiesis }"  # Should return energy.md
wiki-compiler audit --sync-check  # Should report conflicts
```

## Related

- `wiki/adrs/003_owl_integration.md` (Gatekeeping section)
- `desk/tasks/owl-phase1-parallel-run.md`
