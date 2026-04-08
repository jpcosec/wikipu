---
identity:
  node_id: "doc:wiki/drafts/architecture_features.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

The match skill runs as a LangGraph `StateGraph` with a single human breakpoint.

## Details

The match skill runs as a LangGraph `StateGraph` with a single human breakpoint.

- Graph definition and node wiring: `src/core/ai/match_skill/graph.py`
- State schema: `MatchSkillState` in `src/core/ai/match_skill/graph.py`
- Artifact persistence: `MatchArtifactStore` in `src/core/ai/match_skill/storage.py`
```

Never describe a function signature or field list in a README — that belongs in docstrings.

### CLI / UI section rules

Describe the *intent* of the interface. Do not copy argument tables — they drift. Instead, point to where the self-documentation lives in the code so an agent can read it directly without executing anything.

```markdown

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.