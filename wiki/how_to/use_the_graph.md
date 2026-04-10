---
identity:
  node_id: "doc:wiki/how_to/use_the_graph.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

The knowledge graph is the authoritative routing system for the Wikipu ecosystem — not a secondary artifact of the Markdown files but the primary navigation surface for agents and the compliance enforcement mechanism for the system. Every node in `wiki/` compiles to a vertex in the graph, and traversal and facet queries replace sequential file reading for any structural question.

# How to Use the Graph

The knowledge graph is the authoritative routing system for the Wikipu ecosystem — it is not a secondary artifact of the Markdown files but the primary navigation surface for agents and the compliance enforcement mechanism for the system. Every node in `wiki/` compiles to a vertex in the graph, and every `edges:` declaration in frontmatter becomes a typed edge. Traversal and facet queries replace sequential file reading for any non-trivial structural question. The full node and edge type vocabulary is defined in `wiki/reference/knowledge_node_facets.md`.

## Prerequisites

- `knowledge_graph.json` must be current — run `wiki-compiler build` if it is stale.
- Familiarity with the node types (`directory`, `file`, `code_construct`, `doc_standard`, `concept`) and facet types (`SemanticFacet`, `ASTFacet`, `IOFacet`, `ComplianceFacet`, `TestMapFacet`, `ADRFacet`) from `wiki/reference/knowledge_node_facets.md`.
- Understanding of edge relation types: `contains`, `depends_on`, `reads_from`, `writes_to`, `documents`, `transcludes`.

## Steps

1. Start every structural query with `wiki-compiler query` rather than reading Markdown files directly (NAV-1, NAV-3 in `wiki/standards/house_rules.md`).
2. Retrieve a single node by ID: `wiki-compiler query --type get_node --node-id <node_id>`. Node ID format: `doc:wiki/<path>`, `file:src/<path>`, `code:<module>.<class>`.
3. Traverse upward to find what a node belongs to: `wiki-compiler query --type get_ancestors --node-id <node_id>`.
4. Traverse downward to find what depends on a node: `wiki-compiler query --type get_descendants --node-id <node_id>`.
5. Filter by facet to find nodes matching a compliance state or IO profile: `wiki-compiler query --type find_by_io --medium disk` or filter by `ComplianceFacet.status`.
6. Interpret edge semantics: a `depends_on` edge means the source node's code imports or requires the target. A `documents` edge means the source is a wiki/doc node describing the target code node. A `transcludes` edge enforces DRY — the source embeds the target's content verbatim.
7. For compliance review, inspect a node's `ComplianceFacet.failing_standards` to see which rules it violates.
8. To understand the system's topology as a whole, load `knowledge_graph.json` with NetworkX and apply standard graph algorithms (e.g., weakly connected components to find orphan nodes, in-degree centrality to find high-dependency hubs).

## Verification

- [ ] Queries are issued via `wiki-compiler query`, not by scanning directory listings or reading dozens of Markdown files.
- [ ] Node IDs used in queries match the `node_id` format in frontmatter (prefix + path).
- [ ] `knowledge_graph.json` reflects the current state of `wiki/` — `wiki-compiler build` was run after the last edit.
- [ ] Ancestor and descendant traversals return the expected dependency chains without orphan nodes.
- [ ] Nodes with `compliance.status: "implemented"` have no entries in `failing_standards`.
