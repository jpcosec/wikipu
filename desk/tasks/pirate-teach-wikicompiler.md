---
status: open
priority: p1
depends_on: []
created: 2026-04-17
assigned_to: self
---

# Pirate Teach Loop: Learn Wikicompiler

## Objective

Loop pirate until it properly learns to use `wiki-compiler` CLI.

## Iteration Cycle

1. **Prompt pirate** to perform a wikicompiler task
2. **Observe failures** - document what pirate gets wrong
3. **Teach corrections** - explain the mistakes
4. **Repeat** until competent

## Initial Test Tasks

### Task 1: Basic Build
```
pirate -p "Run wiki-compiler build and explain the output"
```

### Task 2: Check Energy
```
pirate -p "Run wiki-compiler energy and tell me what needs fixing"
```

### Task 3: Audit Documentation
```
pirate -p "Run wiki-compiler audit --format json | jq '.summary' to see doc quality"
```

### Task 4: Create a New Wiki Node
```
pirate -p "Create a new wiki node for a simple concept. Follow the template."
```

### Task 5: Fix a Compliance Issue
```
pirate -p "Find and fix one compliance violation from the audit"
```

## Success Criteria

Pirate can:
- [ ] Run all wiki-compiler commands correctly
- [ ] Understand the 4-zone model (raw, wiki, desk, drawers)
- [ ] Create proper wiki nodes with frontmatter
- [ ] Navigate the topology to find relevant code/docs

## Related

- `wiki/concepts/pirate_curriculum.md`
- `wiki/system/pirate.md`
