---
identity:
  node_id: "doc:wiki/standards/document_topology.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

Document topology defines where durable knowledge belongs in the Wikipu wiki. It separates hand-authored standards, concepts, and workflows from derived reference material so agents can decide where to read, write, or relocate documentation without guessing.

## Rule Schema

### Category allocation

| Category | Path | Purpose | Authorship |
|---|---|---|---|
| Front page | `wiki/Index.md` | Root entrypoint for the whole wiki | hand-authored |
| Concept | `wiki/concepts/` | Explanatory truth, architecture, definitions | hand-authored |
| How-to | `wiki/how_to/` | Operational workflows and procedures | hand-authored |
| Standard | `wiki/standards/` | Normative rules, schemas, lifecycle requirements | hand-authored |
| Reference | `wiki/reference/` | Commands, APIs, facets, FAQs, and protocol lookups | derived or hand-maintained reference |
| ADR | `wiki/adrs/` | Durable architectural decisions | hand-authored |

### Allocation rules

1. Root `wiki/` is intentionally small. It holds only the front page and other global entry artifacts explicitly justified as cross-cutting.
2. Each subject has one canonical home. Other nodes may link to it, but should not restate its normative content.
3. If a document explains what something means, place it in `wiki/concepts/`.
4. If a document explains how to perform a task, place it in `wiki/how_to/`.
5. If a document defines what must be true, a schema, or a lifecycle, place it in `wiki/standards/`.
6. If a document describes commands, code structures, facets, FAQs, or audience protocols used for lookup, place it in `wiki/reference/`.
7. If a reference page is generated from or kept in sync with code, treat it as derived reference material and keep it under `wiki/reference/`.
8. When a path or naming convention changes, create the new canonical node first, update inbound references, then delete or supersede the legacy node.

### Migration rule

When relocating a document:

1. Decide its canonical category using the rules above.
2. Update `identity.node_id` to match the new path.
3. Update links, transclusion targets, and issue references that point at the old path.
4. Remove duplicated prose if the move also resolves overlap.
5. Rebuild the graph and audit the wiki.

## Fields

- `Purpose` answers the primary question the document is meant to solve.
- `Authorship` distinguishes hand-authored truth from derived or code-synced reference.
- "Canonical home" means the one location agents should update first when the subject changes.
- A root-level document must justify why it is not better placed under `concepts`, `how_to`, `standards`, `reference`, or `adrs`.

## Usage Examples

- Move issue lifecycle rules into `wiki/standards/` because they are normative.
- Keep `wiki/how_to/plan.md` in `wiki/how_to/` because it is an operator workflow.
- Keep command and facet lookup pages under `wiki/reference/`, even when they are curated by hand.
