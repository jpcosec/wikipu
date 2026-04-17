---
pill_type: tip
scope: global
language: en
nature: context
bound_to: self
created: 2026-04-17
lifecycle: current
---

# Quick Operational Tips

## CLI Shortcuts

| Task | Command |
|------|---------|
| Quick search | `wiki-compiler query --search "term"` |
| Task list | `wiki-compiler query --tasks` |
| Energy check | `wiki-compiler energy --format json \| jq '.score'` |
| Full context | `wiki-compiler context --nodes "X" "Y" --depth 2` |

## Git Hygiene

1. Commit BEFORE editing (clean tree rule)
2. One logical change per commit
3. Message format: `[domain] action: what`

## Task Workflow

```
desk/tasks/Board.md → Pick task → Atomize → Execute → Commit → Update Board
```

## Pill Lifecycle

```
Draft → Bound → Audited → Current → Redundant? → Delete
```

## Reference

- `wiki/reference/cli/query.md`
- `desk/pills/README.md`
