---
identity:
  node_id: "doc:wiki/human_instructions.md"
  node_type: "doc_standard"
edges: []
---

# 🧑‍💻 Human Instructions for `wikipu`

This document provides essential guidelines for human developers working within a `wikipu`-managed repository. Adherence to these instructions ensures consistency, maintains architectural integrity, and facilitates seamless collaboration with AI agents.

## 📜 The `00_house_rules` - Your Guiding Principles

The `[[00_house_rules]]` (`wiki/standards/00_house_rules.md`) is your primary reference. These are not suggestions but the immutable laws of the ecosystem. Familiarize yourself with them to understand the "why" behind `wikipu`'s structure and processes. Key aspects to remember:

*   **Code is Truth, Documentation is Why**: Ensure your code accurately reflects the system's current state, and your documentation explains the design decisions and intent.
*   **Structured Development**: Always use `wiki-compiler scaffold` for new modules to ensure compliance from the start.
*   **DRY Documentation**: Utilize `![[transclusion]]` for shared concepts to avoid duplication and maintain a single source of truth for knowledge.
*   **CI/CD Integration**: Understand that `wiki-compiler` runs on every PR, enforcing compliance and updating the [[Knowledge Graph]].

## 📚 Understanding the Domain: `domain_glossary.yaml`

Refer to `[[wiki/domain_glossary.yaml]]` (`wiki/domain_glossary.yaml`) to understand the canonical terms and their synonyms used throughout the project. This helps prevent polysemy and ensures that both humans and AI agents share a common understanding of key concepts.

*   When discussing concepts, use the terms defined in the glossary.
*   If you introduce a new core concept, propose adding it to the `domain_glossary.yaml`.

## 🛡️ Declaring Exemptions: The `@wiki_exempt` Decorator

In rare cases, a piece of code might not fully comply with the `[[00_house_rules]]` due to external constraints (e.g., legacy libraries, specific third-party integrations). For these situations, use the `@wiki_exempt` decorator (`![[wiki_exempt]]`).

```python
from wikipu.decorators import wiki_exempt

@wiki_exempt(reason="Integrating with a legacy API that uses untyped dictionaries for responses.")
def process_legacy_data(raw_data: dict) -> dict:
    # ... legacy processing logic
    pass
```

*   Always provide a clear `reason` for the exemption.
*   Understand that declaring an exemption acknowledges technical debt, making it visible in the [[Knowledge Graph]]'s `ComplianceFacet`.

## ✍️ Contributing to the Wiki

Your module's `README.md` is its `KnowledgeNode`. Keep it updated with:

*   A clear `intent`.
*   Correct `edges` reflecting dependencies and I/O.
*   Relevant `Facets` information in the YAML frontmatter.
*   Human-readable explanations in the Markdown body.

Remember, the goal is to create a self-documenting, auditable, and intelligent codebase that can be understood and evolved efficiently by everyone, human or AI.
