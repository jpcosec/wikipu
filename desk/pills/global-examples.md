---
pill_type: example
scope: global
language: en
nature: context
bound_to: self
created: 2026-04-17
lifecycle: current
---

# Global Code Examples

## Wiki Node Template

```markdown
---
identity:
  node_id: "doc:wiki/{path}.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/X.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Title

## Definition

## Examples

## Related Concepts

- [[wiki/X]]
```

## OWL Extraction

```python
from wiki_compiler.owl_backend import markdown_to_owl, get_world

world = get_world()
markdown_to_owl(Path("wiki/concepts/energy.md"), world)
```

## SPARQL Query

```bash
wiki-compiler query --owl "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"
```

## Audit with Auto-Task

```bash
wiki-compiler audit --auto-task
ls desk/tasks/audit-fix-*.md
```
