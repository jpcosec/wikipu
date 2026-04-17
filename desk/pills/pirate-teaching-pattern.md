---
pill_type: pattern
scope: domain
language: en
nature: context
bound_to: pirate-teach-wikicompiler
created: 2026-04-17
lifecycle: current
---

# Pirate Teaching Loop Pattern

## Iteration Cycle

```
1. Prompt pirate → perform a wikicompiler task
2. Observe failures → document mistakes
3. Teach corrections → explain why wrong
4. Repeat → until competent
```

## Test Task Progression

| Task | Command | What it tests |
|------|---------|---------------|
| 1 | `pirate -p "Run wiki-compiler build"` | Basic CLI usage |
| 2 | `pirate -p "Run wiki-compiler energy"` | Self-assessment |
| 3 | `pirate -p "wiki-compiler audit --format json \| jq '.summary'"` | Diagnostics |
| 4 | `pirate -p "Create wiki node following template"` | Creation |
| 5 | `pirate -p "Fix one audit violation"` | Problem-solving |

## Mastery Indicators

- [ ] All wiki-compiler commands work
- [ ] 4-zone model understood
- [ ] Proper frontmatter creation
- [ ] Topology navigation

## Reference

- `wiki/concepts/pirate_curriculum.md`
