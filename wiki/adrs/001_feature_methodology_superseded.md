---
identity:
  node_id: "doc:wiki/adrs/001_feature_methodology_superseded.md"
  node_type: "adr"
adr:
  decision_id: "001"
  status: "accepted"
  context_summary: "Legacy methodology documents copied from another project created ambiguity, so they were retired and replaced by repo-specific standards and protocols."
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Legacy methodology material copied from another project was retired so Wikipu could have one canonical standards surface. This ADR records that the repository should keep only repo-specific durable guidance rather than preserving unrelated prior-framework instructions as shadow authority.

# ADR 001: Legacy old_standards material is retired

## Context

`raw/old_standards/` contained methodology and standards documents copied from an earlier project. They referenced unrelated modules, domain terms, and runtime patterns that do not exist in `wikipu`. Leaving them under `raw/` made their status ambiguous: they looked authoritative, but they were neither integrated into the active documentation set nor explicitly retired.

## Decision

The legacy `raw/old_standards/` tree is retired and removed from the repository.

Verdict by document group:

- `feature_creation_methodology.md`: superseded by the current house rules, ADR workflow, and issue-plan process.
- `code/*.md`: superseded because they describe a different codebase and runtime shape.
- `wiki/*.md`: superseded because they prescribe documentation structure for unrelated modules and obsolete paths such as `wiki/standards/wiki/`.

Relevant surviving ideas are now represented by the current canonical docs instead of preserved as legacy reference:

- `wiki/standards/house_rules.md`
- `wiki/domain_glossary.yaml`
- `agents/librarian/intro.md`
- `plan_docs/issues/Index.md`

## Consequences

- `raw/` again contains only source material with active meaning for this repository.
- Contributors have one canonical standards surface instead of a shadow archive.
- If a retired concept proves useful later, it should be reintroduced as a new ADR or durable document written for `wikipu`, not restored from the deleted legacy set.
