---
identity:
  node_id: "doc:wiki/reference/protocols/human_contributor.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

This protocol summarizes the expectations for human contributors working in a Wikipu-managed repository. It is a quick reference to the durable rules that keep code, docs, and the graph aligned.

## Rule Schema

- Treat `wiki/standards/house_rules.md` as the primary normative source.
- Keep code, wiki nodes, and changelog entries aligned when behavior changes.
- Use the graph and reference docs to understand the system before introducing new structure.
- Record exemptions explicitly rather than hiding non-compliance.
- Keep documentation in its canonical category according to `wiki/standards/document_topology.md`.

## Fields

- `Primary normative source` means contributors should update standards first when a rule changes.
- `Aligned` means code, docs, and graph-facing metadata tell the same story.
- `Exemption` means a visible, justified departure from the default rules.

## Usage Examples

- When adding a new durable rule, write it under `wiki/standards/` instead of burying it in a how-to.
- When moving a doc, update its `node_id`, inbound links, and any related issue references in the same change.
