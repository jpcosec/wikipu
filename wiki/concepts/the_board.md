---
identity:
  node_id: "doc:wiki/concepts/the_board.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/board_gate_pattern.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/board_gate_pattern.md"
  source_hash: "5ddbb160292bc8387a9d70b4d3060c3c843651e5af5ef68e156bab47a0701c06"
  compiled_at: "2026-04-14T16:50:28.657131"
  compiled_from: "wiki-compiler"
---

### Structure

## Details

### Structure

```
<domain>/Board.md
<domain>/items/<item-slug>.md
```

`Board.md` is the index and monitoring surface for one domain. It contains:
- Current state summary (one paragraph)
- Priority roadmap with phases
- Each phase lists items with a one-line description
- Dependency summary (what blocks what)
- Parallelization map

Each item lives in a separate file with: explanation, what to fix, how to do it, depends on.

### Resolution Protocol

When an item is resolved:
1. Verify existing tests are still valid.
2. Add new tests where needed.
3. Run tests.
4. Update changelog.md.
5. Delete the item file AND remove it from Board.md.
6. Commit.

Nothing is "archived" — resolved items live in git history and changelog only.

### Existing Instance

`desk/issues/` is the first Board. It tracks implementation work. The pattern should be replicated for:

| Board | Domain |
|---|---|
| `desk/issues/` | Implementation work (gaps, unimplemented features) |
| `desk/proposals/` | Topology and facet proposals awaiting approval |
| `desk/socratic/` | Open design questions awaiting resolution |
| `desk/autopoiesis/` | Self-repair cycles (cleansing, drift correction, rule patches) |

---

Generated from `raw/board_gate_pattern.md`.