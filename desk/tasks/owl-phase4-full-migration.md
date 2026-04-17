---
status: open
priority: p2
depends_on: [owl-phase3-reasoning]
created: 2026-04-17
assigned_to: self
---

# Phase 4: Full OWL Migration

## Objective

Markdown files become human-readable OWL export. Owlready2 is the single source of truth. Pydantic models become read-only views.

## Tasks

- [ ] Remove YAML frontmatter edges from wiki/ nodes
  - [ ] Keep frontmatter for identity (node_id, node_type)
  - [ ] Move edges to OWL quadstore
- [ ] Update markdown_to_owl to NOT extract edges (quadstore is source)
- [ ] Add owl_to_markdown() for human-readable export
  - [ ] Generate frontmatter from quadstore
  - [ ] Generate body from annotations
- [ ] Update wiki-compiler build to export, not import
- [ ] Make Pydantic models read-only views
  - [ ] Validate from OWL, not write to OWL
- [ ] Update documentation to reflect OWL-first workflow

## Verification

```bash
wiki-compiler build  # Exports quadstore → markdown
cat wiki/concepts/energy.md  # Should have minimal frontmatter, content from OWL
owlready2 quadstore is single source of truth
```

## Related

- `wiki/adrs/003_owl_integration.md` (Phase 4 section)
- `desk/tasks/owl-phase3-reasoning.md`
