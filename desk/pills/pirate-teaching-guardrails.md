---
pill_type: guardrail
scope: global
language: en
nature: context
bound_to: self
created: 2026-04-17
lifecycle: current
---

# Pirate Teaching Guardrails

## The 80/10 Rules Apply

- No wiki file exceeds 80 lines
- No function exceeds 10 executable lines

## CLI-First Rule

Pirate MUST use wiki-compiler CLI before any file read:
```
wiki-compiler query --type get_node --node-id "doc:wiki/X.md"
wiki-compiler context --nodes "doc:wiki/X.md" --depth 2
```

## Success Criteria

Pirate demonstrates mastery when:
- 90% of info retrieval uses CLI queries
- File reads are preceded by graph confirmation
- Status/energy checked before major operations
- Curriculum tasks 1-8 completed

## Anti-Patterns

- Guessing file paths instead of querying
- Reading before querying (NAV-1 violation)
- Dumping entire files instead of targeted extraction
- Ignoring status/energy output

## Reference

- `wiki/concepts/pirate_curriculum.md`
- `wiki/system/pirate.md`
