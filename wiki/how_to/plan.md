---
identity:
  node_id: "doc:wiki/how_to/plan.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

Planning in Wikipu means converting a perceived gap or requirement into a discrete, independently completable issue file before any code or wiki node is touched. A plan is ephemeral by design — it lives in `desk/issues/`, is deleted when resolved, and leaves a permanent trace only through the changelog and any resulting ADRs.

# How to Plan

Planning in Wikipu means converting a perceived gap or requirement into a discrete, independently completable issue file before any code or wiki node is touched. Good plans are atomic, checkable, and traceable to a specific perturbation in the system. The normative rules for issue format and lifecycle live in `wiki/standards/issues_lifecycle.md`; this guide is the operator workflow for applying them.

## Prerequisites

- Access to `wiki/standards/issues_lifecycle.md` — the canonical reference for issue format and lifecycle.
- Familiarity with the zones: `raw/`, `wiki/`, `desk/`, `drawers/`, `src/`.
- Understanding of OP-4 (Issue Resolution Protocol) in `wiki/standards/house_rules.md`.

## Steps

1. Identify the perturbation — a broken contract, a missing node, an unimplemented rule, or a new requirement from an external source.
2. Create a file under `desk/issues/` using the format defined in `wiki/standards/issues_lifecycle.md`.
   - Filename format: `<number>-<slug>.md`
3. Run the Board update stages from `wiki/standards/issues_lifecycle.md`: legacy audit, atomization check, contradiction check, dependency graph.
4. Update `desk/issues/Board.md` with the issue and its dependencies.
5. If the issue has more than 3–4 independently failing steps, split into child issues with explicit `Depends on:` links.
6. If the issue conflicts with or duplicates another, resolve the overlap before adding to the Board.
7. Commit the new issue file and updated Board with a message naming the perturbation.

## Verification

- [ ] The issue file exists in `desk/issues/`.
- [ ] The issue file contains all required sections with no placeholders.
- [ ] The issue is listed in `desk/issues/Board.md` with correct dependency links.
- [ ] No other issue file proposes a conflicting fix to the same file or component.
- [ ] The issue is atomic: it can be handed to a single subagent in one session.
