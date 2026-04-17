---
status: open
priority: p1
depends_on: []
created: 2026-04-17
assigned_to: self
---

# Fix Energy CLI Performance

## Problem

`wiki-compiler energy` is extremely slow (times out) and reports 12,736 compliance violations.

## Root Cause Analysis

1. **Wikiignore bug**: `src/looting/pirate/` is being scanned despite `.wikiignore` entries (6315 irrelevant nodes)
2. **12,736 violations**: Likely the `compliance_violations` check is scanning all these pirate node_modules files

## Diagnosis

```bash
# Count pirate-related nodes in graph
cat knowledge_graph.json | python3 -c "import json,sys; d=json.load(sys.stdin); nodes=[n['id'] for n in d.get('nodes',[]) if 'pirate' in n['id'].lower() or 'pi-mono' in n['id'].lower()]; print(len(nodes))"
# Output: 6315 (should be 0)
```

## Fix Required

1. Fix wikiignore glob matching (see `desk/tasks/fix-wikiignore-glob-matching.md`)
2. Rebuild the knowledge graph: `wiki-compiler build`
3. Re-run energy to verify performance

## Expected Outcome

- Energy should complete in < 5 seconds
- Compliance violations should drop from 12,736 to a reasonable number (< 100)

## Verification

```bash
time wiki-compiler energy 2>&1
# Should complete in < 5 seconds
```
