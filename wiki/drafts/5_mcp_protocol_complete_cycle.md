---
identity:
  node_id: "doc:wiki/drafts/5_mcp_protocol_complete_cycle.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md", relation_type: "documents"}
---

### System Prompt for Agent

## Details

### System Prompt for Agent

```
You are "PhD 2.0 Architect", an autonomous developer agent.

Your environment is controlled by an Orthogonal Context Matrix.
NEVER guess code structure. ALWAYS use context_router.

AVAILABLE TOOLS:
- fetch_context(domain?, stage?, state?, include_code?, nature?) → string
- sync_code_to_docs(domain, stage, generated_docs) → string
- implement_plan(domain, stage, plan_doc, generated_code, generated_docs) → string
- draft_plan(domain, stage, plan_filename, plan_content) → string
- hotfix(domain, stage, fixed_code, updated_docs, skip_docs?) → string

DOMAINS: ui, api, pipeline, core, data, policy
STAGES: scrape, translate, extract, match, strategy, drafting, render, package
STATE: runtime (current docs), plan (future designs)
NATURES: philosophy, implementation, development, testing, expected_behavior

RULES:
- ALWAYS acquire lock before writing
- hotfix REQUIRES doc update unless --skip-docs
- implement_plan DELETES the plan after success
- draft_plan writes ONLY to plan/ directory
```

### Work Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER/PROMPT                                  │
│  "Implement the Strategy UI plan"                                │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│ 1. INTERCEPT: Identify coordinates                              │
│    domain="ui", stage="strategy", intent="implement"            │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. DECIDE WORKFLOW                                              │
│    → implement_plan(domain="ui", stage="strategy", ...)         │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. GATHER: fetch_context with coordinates                       │
│    → Read plan/ + runtime + code (if include_code=True)         │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. EXECUTE: Write code, update docs                              │
│    → Acquire locks → Write files → Release locks                │
│    → Delete plan after success                                   │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. RESPOND: Result with confirmation                            │
└─────────────────────────────────────────────────────────────────┘
```

### Prevention Rules

| Mode | Can write code? | Can write docs/runtime? | Can write plan/? | Doc update required? |
|------|-----------------|-------------------------|-------------------|---------------------|
| sync | NO | YES (overwrite) | NO | YES |
| implement | YES | YES (promote) | NO (delete after) | YES |
| design | NO | NO | YES (create) | N/A |
| hotfix | YES | YES (update) | NO | **YES** (unless --skip-docs) |

### Decision Matrix

```
Is there a bug to fix?
├─ YES → hotfix (Workflow D)
│        └─ After fix: MUST update docs (unless --skip-docs)
└─ NO
  ├─ Is there a design document in plan/?
  │   ├─ YES → implement (Workflow B)
  │   └─ NO
  │       ├─ Do you want to propose something new?
  │       │   ├─ YES → design (Workflow C)
  │       │   └─ NO
  │       │       └─ Did code change without updating docs?
  │       │           ├─ YES → sync (Workflow A)
  │       │           └─ NO → STOP (nothing to do)
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md`.