# Facets as Questions

## Core Idea

The graph topology answers structural questions: what exists, what connects to what.
Facets answer dimensional questions about the meaning, health, and context of each node.

Each facet is a lens — one specific question you can ask uniformly across every node in the graph.

---

## Current Facets and Their Questions

| Facet | Question |
|---|---|
| `SemanticFacet` | What does this do? |
| `ASTFacet` | How is it structured? |
| `IOFacet` | What data does it consume or produce? |
| `ComplianceFacet` | How complete and rule-compliant is it? |
| `TestMapFacet` | How is it tested? |
| `ADRFacet` | What decisions shaped it? |

## Example Future Facets

| Facet | Question |
|---|---|
| `ModelUsageFacet` | What AI models does it use? |
| `PipelineStageFacet` | Where does it sit in the execution flow? |
| `ProductEvolutionFacet` | How fast is it changing and why? |

---

## The Auditor's Role

The auditor is the inverse of the facet question:

> For each question, which nodes can't answer it when they should be able to?

A `file:` node that can't answer "what does this do?" → missing docstring.
A `file:` node that can't answer "what data does it produce?" → untyped I/O.
A `code:` node that can't answer "how is it tested?" → no test coverage.

---

## When Is a Facet Worth Adding?

A facet is worth adding when:
1. You have a question you want to ask uniformly across the whole graph.
2. The answer isn't already captured by an existing facet.

If the question is one-off or node-specific, it's not a facet — it's a query.
If the question duplicates an existing facet's scope, it's a field on that facet, not a new one.

---

## Design Rule

**Every facet must declare its question explicitly.**
No facet should be added to contracts.py without a one-sentence question
that defines what it answers. This question is the facet's contract —
it governs what data belongs in it, how the injector populates it,
and what the auditor checks against it.
