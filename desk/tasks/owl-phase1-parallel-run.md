---
status: completed
priority: p2
depends_on: []
created: 2026-04-17
completed: 2026-04-17
assigned_to: self
---

# Phase 1: Owlready2 Parallel Run

## Objective

Add owlready2 as dependency and export current wiki graph to OWL format. Quadstore lives alongside Markdown files.

## Tasks

- [ ] Add `owlready2` to `pyproject.toml` dependencies
- [ ] Create `src/wiki_compiler/owl_backend/` module
  - [ ] `__init__.py` — base ontology IRI, world setup
  - [ ] `extractor.py` — `markdown_to_owl()` main function
  - [ ] `frontmatter.py` — YAML → RDF triples extraction
  - [ ] `wikilinks.py` — wiki-links → `:references` extraction
  - [ ] `annotations.py` — sections → annotation properties
  - [ ] `export.py` — RDF/XML export
- [ ] Create `src/wiki_compiler/shacl/` module
  - [ ] `shapes.py` — KnowledgeNode SHACL shapes
  - [ ] `validator.py` — SHACL validation wrapper
- [ ] Create `wikipu.owl` in repo root (gitignored, derived artifact)
- [ ] Add `--owl` flag to `wiki-compiler query` command

## Verification

```bash
# Dependency
python -c "from owlready2 import *; print('owlready2 import OK')"

# Module import
python -c "from wiki_compiler.owl_backend import markdown_to_owl; print('module OK')"

# Build with OWL export
wiki-compiler build
ls wikipu.owl  # Should exist

# Query with OWL
wiki-compiler query --owl "SELECT ?s ?p ?o WHERE { ?s a ?p } LIMIT 10"

# SHACL validation
python -c "from wiki_compiler.shacl import validate_node; print('shacl OK')"
```

## Related

- `wiki/adrs/003_owl_integration.md`
- `wiki/standards/house_rules.md`
