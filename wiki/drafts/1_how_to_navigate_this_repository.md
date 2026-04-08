---
identity:
  node_id: "doc:wiki/drafts/1_how_to_navigate_this_repository.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

### Entry points

## Details

### Entry points

```
README.md                  ← repository overview and orientation
docs/standards/docs/       ← documentation conventions (this file and siblings)
src/<module>/README.md     ← per-module orientation
future_docs/               ← deferred work and known problems
plan_docs/                 ← active execution plans (ephemeral)
changelog.md               ← record of significant changes
```

`docs/` is a navigation layer, not a content store. It holds cross-cutting guides and links out to module-level READMEs. It does not duplicate what the code or module READMEs already say.

### Reading order for a new contributor

1. `README.md` — understand the system shape and purpose.
2. `docs/standards/docs/` — understand documentation conventions before touching anything.
3. `src/<module>/README.md` — orient on the specific area you're working in.
4. The source files linked from that README — the code is the authoritative source.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.