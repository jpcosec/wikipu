# Wiki Construction Principles

## Core Idea

The same discipline that makes code clean applies to documentation.
A wiki node is a unit of knowledge. It should have one responsibility,
a clear interface, and compose with other nodes rather than growing monolithic.

---

## Principle 1: Single Responsibility

Each wiki node answers exactly one question or defines exactly one concept.
If you cannot state the node's purpose in one sentence, it needs to be split.

The test: can you transclude this node into two different parent documents
and have it make sense in both contexts? If yes, it is atomic.
If it only makes sense in one context, it is probably not atomic — it is
a section of a larger document masquerading as a node.

---

## Principle 2: Mandatory Abstract

Every node opens with a 1-3 sentence abstract. This is the node's interface —
what gets indexed, what the context command uses to rank relevance, what
an LLM reads before deciding whether to go deeper.

The abstract must be:
- Self-contained (readable without the rest of the node)
- Declarative (states what the node IS, not what it CONTAINS)
- Machine-extractable (first paragraph after the YAML frontmatter, before any heading)

The abstract is a first-class field. Its absence is an audit violation.

---

## Principle 3: Composition via CLI, Not Prose

Long documents are assembles of atomic nodes via transclusion.
A composite node has no prose of its own — only transclusions and navigation.

You do not write a long document. You call:

    wiki-compiler compose --nodes "concept_a concept_b how_to_x" \
                          --title "Complete Guide to X" \
                          --output wiki/guides/x.md

This produces a node whose body is:
    ![[concept_a]]
    ![[concept_b]]
    ![[how_to_x]]

Composite nodes are index nodes. They exist for navigation, not for content.
Content lives in the atomic nodes.

This mirrors clean code: a function that only calls other functions,
with no logic of its own, is a composition layer. It is valid and useful.
It is not a smell. Growing it with inline prose IS a smell.

---

## Principle 4: Node Templates

Different types of knowledge have different required sections.
A template defines what a node of that type must contain to be complete.
Missing required sections are audit violations.

### `concept`
Question: What is X?
Required: abstract, definition, examples, related_concepts

### `how_to`
Question: How do I do X?
Required: abstract, prerequisites, steps, outcome

### `standard`
Question: What is the rule for X?
Required: abstract, rule, rationale, violation_examples

### `reference`
Question: How does X work technically?
Required: abstract, signature_or_schema, fields, usage_examples

### `index`
Question: What lives in this area?
Required: abstract, node list (via transclusion only — no inline content)

The node_type field in the YAML frontmatter selects the template.
The compiler checks that required sections are present.

---

## Principle 5: The Digestion Pipeline

Free text is the input. Structured nodes are the output.
The raw text is never deleted — it is the ore. The wiki nodes are the refined metal.

Pipeline:

    raw/                    immutable free text (source material)
      ↓ wiki-compiler ingest
    wiki/drafts/            proposed atomic nodes with template stubs
      ↓ human or LLM review
    wiki/                   approved, structured, indexed nodes

The ingest step does not just create stubs. It:
1. Reads the raw text
2. Identifies concepts, processes, standards, and references within it
3. Proposes a split into atomic nodes, each with the appropriate template
4. Outputs draft nodes for review — one file per proposed concept

The review step decides: approve as-is, merge two proposals, split one further,
or reject and rephrase. Only approved nodes enter wiki/.

The raw source is archived, not deleted. The link between
a wiki node and its raw origin is an edge: raw_source → wiki_node (documents).

---

## Principle 6: Free Text Has a Place But Not a Permanent Home

Free text (chat logs, brainstorm dumps, meeting notes) is valid input.
It lives in raw/ while it is undigested.
It is not a wiki node. It does not get indexed. It does not get queried.

The system "digests" it by running ingest, which proposes the
structured decomposition. Until digested, the content is available
as raw source but invisible to the graph.

This creates a clear lifecycle:
    undigested (raw/)  →  proposed (wiki/drafts/)  →  structured (wiki/)

---

## How This Relates to the Graph

The abstract becomes SemanticFacet.intent for doc nodes.
The template type maps to node_type in SystemIdentity.
The required sections map to audit checks: "does this concept node have a definition?"
The composition via transclusion maps to `transcludes` edges in the graph.

The graph is the compiled result of applying these principles.
The principles are what make the graph useful rather than just large.
