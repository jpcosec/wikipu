---
identity:
  node_id: "doc:wiki/how_to/document.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

Writing a wiki node means creating or updating a Markdown file in `wiki/` that describes current truth. Every node must answer exactly one question, start with a mandatory abstract, use transclusion instead of copying content, and carry YAML frontmatter that makes the node machine-readable as a graph vertex.

# How to Document

Writing a wiki node means creating or updating a Markdown file in `wiki/` that describes current truth — not plans, not aspirations, not historical decisions. Every node must answer exactly one question, start with a mandatory abstract, use transclusion instead of copying content, and carry YAML frontmatter that makes the node machine-readable as a graph vertex. The rules are defined in Layer 6 (WK rules) of `wiki/standards/house_rules.md`.

## Prerequisites

- Read WK-1 through WK-6 in `wiki/standards/house_rules.md` (Layer 6).
- Read the artifact template for the node type you are writing — see `wiki/standards/artifacts/` for `how_to`, `concept`, `doc_standard`, `adr`, `reference`, and `faq` schemas.
- Know the node's `node_type` — this determines the required body sections (WK-4).
- Understand when NOT to create a new node: if a concept already exists, transclude it rather than duplicate it (WK-3).

## Steps

1. Confirm the node does not already exist by querying the graph or searching `wiki/`. If it exists, update the existing file rather than creating a new one.
2. Identify the single question or concept the node answers (WK-1). If more than one, split into multiple nodes.
3. Choose the correct `node_type` from the enum: `concept`, `doc_standard`, `how_to`, `adr`, `reference`, or `faq`.
4. Create the file under the appropriate `wiki/` subdirectory with a descriptive, lowercase, underscore-separated filename.
5. Write the YAML frontmatter with at minimum: `identity.node_id` (format: `"doc:wiki/<path>"`), `identity.node_type`, and `compliance.status`. Add `edges` for every relationship to another node.
6. Write the mandatory abstract — 1 to 3 sentences of plain prose immediately after the frontmatter, with no heading above it (WK-2). It must stand alone as a complete summary.
7. Write the body sections required by WK-4 for the chosen node type.
8. Replace any content copied from another node with a `![[node_name]]` transclusion (WK-3).
9. Set `compliance.status` accurately: `"implemented"` only if the described code or process exists and matches reality (WK-5).
10. Add the node to its domain's `Index.md` with a one-line description.
11. Run `wiki-compiler build` to verify the node is parsed without errors and appears in `knowledge_graph.json`.

## Verification

- [ ] The node's purpose can be stated in one sentence, and it cannot reasonably be split further.
- [ ] The abstract paragraph exists as the first plain-text content after the frontmatter, with no heading above it.
- [ ] No content is duplicated from another node — shared facts are transcluded.
- [ ] `compliance.status` matches the actual implementation state of the described subject.
- [ ] The node does not reference `desk/` or `backlog/` nodes.
- [ ] The node appears in its domain's `Index.md`.
- [ ] `wiki-compiler build` completes without errors referencing this node.
