---
identity:
  node_id: "doc:wiki/drafts/ai_agent_restrictions_system_enforcement.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

**This repository is protected by Git Hooks and Branch Protection Rules.**

## Details

**This repository is protected by Git Hooks and Branch Protection Rules.**

| Rule | What Happens | How to Comply |
|------|--------------|---------------|
| `commit-msg` hook | Blocks commits without valid format or TestSprite evidence | Include `TestSprite: Passed` or `TestSprite: ID-123` in commit body |
| `pre-push` hook | Blocks push if tests fail | Ensure `pytest` and `npm run typecheck` pass |
| GitHub PR rules | Requires 1+ approval and passing CI | Get human review before merge |

### Commit Message Format (Required)

```
<type>(<domain>): <description> (<spec-id>)

- <component 1>
- <component 2>
- TestSprite: <Passed|ID-123>
```

**Valid examples:**
```
feat(ui): implement strategy form (spec-123)
  - StrategyForm component
  - DeltaEditor component
  TestSprite: Passed

fix(pipeline): correct span offset (hotfix-456)
  - Fixed multiline handling
  TestSprite: ID-789
```

### What Happens If You Violate Rules

| Violation | Result |
|-----------|--------|
| Missing `(spec-id)` | `commit-msg` hook blocks commit |
| Missing `TestSprite:` | `commit-msg` hook blocks commit |
| Failing tests + push | `pre-push` hook blocks push |
| Push without PR | GitHub blocks merge (requires approval) |

### Safe Workflow for AI Agents

1. Before any code change: Read the spec in `plan/`
2. After implementation: Run tests locally (or document that they pass)
3. When committing: Use exact format with `TestSprite:` line
4. When pushing: Ensure pre-push hook passes (or document test failure)

**Do NOT attempt to bypass these rules — they protect the codebase integrity.**

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.