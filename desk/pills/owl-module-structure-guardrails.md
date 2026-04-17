---
pill_type: guardrail
scope: component
language: en
nature: implementation
bound_to: owl-phase1-parallel-run
created: 2026-04-17
lifecycle: current
---

# OWL Module Structure Guardrails

## Module Atomization (per STANDARDS.md)

- **80-line rule** — No file exceeds 80 lines
- **10-line function** — No function exceeds 10 executable lines
- **Single responsibility** — One class/component per file

## OWL Backend Structure

```
src/wiki_compiler/owl_backend/
├── __init__.py          # Ontology IRI, world setup, exports
├── extractor.py         # markdown_to_owl() orchestrator
├── frontmatter.py      # YAML → RDF triples
├── wikilinks.py        # wiki-links → :references
├── annotations.py      # sections → annotation properties
└── export.py           # RDF/XML export

src/wiki_compiler/shacl/
├── __init__.py         # exports
├── shapes.py           # KnowledgeNode SHACL shapes
└── validator.py        # SHACL validation wrapper
```

## Naming Conventions

- Classes: `PascalCase`
- Functions: `snake_case`
- OWL properties: `camelCase` with `:prefix`
- Files: `snake_case.py`

## Prohibited

- No direct quadstore manipulation outside owl_backend module
- No OWL reasoning in validation (SHACL only for Phase 1)
- No bypassing SyncGate for direct OWL writes

## Reference

- `wiki/standards/house_rules.md` (ID-3, MA-2)
- `workflow/STANDARDS.md`
