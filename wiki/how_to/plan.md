---
identity:
  node_id: "doc:wiki/how_to/plan.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

Planning in Wikipu means converting a perceived gap or requirement into a discrete, independently completable issue file before any code or wiki node is touched. A plan is ephemeral by design — it lives in `plan_docs/`, is deleted when resolved, and leaves a permanent trace only through the changelog and any resulting ADRs.

# How to Plan

Planning in Wikipu means converting a perceived gap or requirement into a discrete, independently completable issue file before any code or wiki node is touched. Good plans are atomic, checkable, and traceable to a specific perturbation in the system. The normative rules for issue format, indexing, contradiction checks, and lifecycle live in `wiki/standards/issues_lifecycle.md`; this guide is the operator workflow for applying them.

## Prerequisites

- Access to `wiki/standards/issues_lifecycle.md` — the canonical reference for issue format and lifecycle.
- Familiarity with the five zones: `raw/`, `wiki/`, `desk/`, `backlog/`, `src/`.
- Understanding of OP-4 (Issue Resolution Protocol) and OP-5 (Atomization) in `wiki/standards/house_rules.md`.

## Steps

1. Identify the perturbation — a broken contract, a missing node, an unimplemented rule, or a new requirement from an external source.
2. Classify it: is it a **gap** (something exists but is wrong) or an **unimplemented** item (something designed but not built)?
3. Create a file under `plan_docs/issues/gaps/` or `plan_docs/issues/unimplemented/` using the format defined in `wiki/standards/issues_lifecycle.md`.
4. Run the indexing stages from `wiki/standards/issues_lifecycle.md`: legacy audit, atomization check, contradiction check, dependency graph, and `Index.md` update.
5. If the issue has more than 3–4 independently failing steps, split it into child issues with explicit `Depends on:` links.
6. If the issue conflicts with or duplicates another, resolve the overlap before adding it to the Index.
7. Add the issue to `plan_docs/issues/Index.md` with its dependency links and parallelization status.
8. Commit the new issue file and updated Index with a message naming the perturbation.

## Verification

- [ ] The issue file exists under the correct subdirectory (`gaps/` or `unimplemented/`).
- [ ] The issue file contains all five required sections with no placeholders.
- [ ] The issue is listed in `plan_docs/issues/Index.md` with correct dependency links.
- [ ] No other issue file proposes a conflicting fix to the same file or component.
- [ ] The issue is atomic: it can be handed to a single subagent in a single session.
