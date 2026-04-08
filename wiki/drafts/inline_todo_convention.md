---
identity:
  node_id: "doc:wiki/drafts/inline_todo_convention.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/future_docs_guide.md", relation_type: "documents"}
---

When deferring work from inside the code, leave a `# TODO` comment at the exact location. Format:

## Details

When deferring work from inside the code, leave a `# TODO` comment at the exact location. Format:

```python
# TODO(future): <short description> — see future_docs/<filename>.md
```

The `(future)` tag distinguishes deferred items from short-term TODOs. The file link makes it navigable.

**Example:**
```python
# TODO(future): thin MatchSkillState — move payload fields to disk refs — see future_docs/match_skill_hardening_roadmap.md
```

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/future_docs_guide.md`.