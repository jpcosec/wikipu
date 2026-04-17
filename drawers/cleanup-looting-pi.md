---
status: open
priority: p3
depends_on: []
created: 2026-04-17
assigned_to: self
---

# Clean up src/looting/pi/

## Problem

`src/looting/pi/` is untracked looted project. Per `wiki/concepts/looting_protocol.md`, looted projects must be either absorbed or moved to `exclusion/`.

## Options

1. **Commit as loot** — Add to repo, track in `src/looting/`
2. **Move to exclusion/** — Per ID-8, non-absorbed content is Not-Self
3. **Delete** — If not needed

## Decision

[To be determined]

## Verification

```bash
# Option 1: Committed
git ls-files src/looting/pi/ | head

# Option 2: In exclusion
ls exclusion/ | grep pi

# Option 3: Deleted
ls src/looting/pi/ 2>&1 | grep "No such"
```
