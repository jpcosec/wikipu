---
status: open
priority: p2
depends_on: []
created: 2026-04-17
assigned_to: self
---

# Phase 1: Owlready2 Parallel Run

## Objective

Add owlready2 as dependency and export current wiki graph to OWL format. Quadstore lives alongside Markdown files.

## Tasks

- [ ] Add `owlready2` to `pyproject.toml` dependencies
- [ ] Create `src/wiki_compiler/owl_backend.py` module
- [ ] Define base ontology IRI: `http://wikipu.org/ontology/`
- [ ] Implement `markdown_to_owl()` content extraction
  - [ ] Extract YAML frontmatter as RDF triples
  - [ ] Extract wiki-links as `:references` properties
  - [ ] Extract sections as annotations
- [ ] Export existing `wiki/` to RDF/XML
- [ ] Create `wikipu.owl` in repo root (gitignored, derived artifact)
- [ ] Add `--owl` flag to `wiki-compiler query` command
- [ ] Define SHACL shapes for `KnowledgeNode` schema

## Verification

```bash
python -c "from owlready2 import *; print('owlready2 import OK')"
wiki-compiler build --owl
ls wikipu.owl  # Should exist
wiki-compiler query --owl "SELECT ?s ?p ?o WHERE { ?s a ?p } LIMIT 10"
```

## Related

- `wiki/adrs/003_owl_integration.md`
- `wiki/standards/house_rules.md`
