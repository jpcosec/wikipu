"""
Wiki node document models using StructuredNLDoc.
These models enforce the required structure for each node type.
"""

from sldb import StructuredNLDoc
from pydantic import Field
from typing import Literal


class ConceptDoc(StructuredNLDoc):
    """Document model for concept nodes (What is X?)."""

    frontmatter: dict = Field(
        description="YAML frontmatter with identity, edges, and compliance"
    )
    title: str = Field(description="Title of the concept")
    abstract: str = Field(description="One-paragraph summary of the concept")
    definition: str = Field(description="Formal definition of the concept")
    examples: list[str] = Field(
        default_factory=list, description="Examples illustrating the concept"
    )
    related_concepts: list[str] = Field(
        default_factory=list, description="Related concept IDs"
    )

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

## Definition

⸢rev,markdown•definition⸥

## Examples

⸢rev,list•examples⸥

## Related Concepts

⸢rev,list•related_concepts⸥
"""


class HowToDoc(StructuredNLDoc):
    """Document model for how-to nodes (How do I do X?)."""

    frontmatter: dict = Field(description="YAML frontmatter")
    title: str = Field(description="Title")
    abstract: str = Field(description="One-paragraph summary")
    prerequisites: list[str] = Field(
        default_factory=list, description="Required prerequisites"
    )
    steps: list[str] = Field(
        default_factory=list, description="Step-by-step instructions"
    )
    verification: str = Field(description="How to verify success")

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

## Prerequisites

⸢rev,list•prerequisites⸥

## Steps

⸢rev,list•steps⸥

## Verification

⸢rev,markdown•verification⸥
"""


class DocStandardDoc(StructuredNLDoc):
    """Document model for doc_standard nodes (What is the rule for X?)."""

    frontmatter: dict = Field(description="YAML frontmatter")
    title: str = Field(description="Title")
    abstract: str = Field(description="One-paragraph summary of the rule")
    rule_schema: str = Field(description="Formal schema or structure of the rule")
    fields: list[dict] = Field(default_factory=list, description="Field definitions")
    usage_examples: list[str] = Field(
        default_factory=list, description="Examples of usage"
    )

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

## Rule Schema

⸢rev,markdown•rule_schema⸥

## Fields

⸢rev,list•fields⸥

## Usage Examples

⸢rev,list•usage_examples⸥
"""


class ReferenceDoc(StructuredNLDoc):
    """Document model for reference nodes (How does X work technically?)."""

    frontmatter: dict = Field(description="YAML frontmatter")
    title: str = Field(description="Title")
    abstract: str = Field(description="One-paragraph summary")
    signature_or_schema: str = Field(description="Function signature or data schema")
    fields: list[dict] = Field(
        default_factory=list, description="Parameter/field definitions"
    )
    usage_examples: list[str] = Field(
        default_factory=list, description="Usage examples"
    )

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

## Signature or Schema

⸢rev,markdown•signature_or_schema⸥

## Fields

⸢rev,list•fields⸥

## Usage Examples

⸢rev,list•usage_examples⸥
"""


class IndexDoc(StructuredNLDoc):
    """Document model for index nodes (What lives in this area?)."""

    frontmatter: dict = Field(description="YAML frontmatter")
    title: str = Field(description="Title")
    abstract: str = Field(description="One-paragraph summary")
    content: str = Field(default="", description="Additional content")

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

⸢rev,markdown•content⸥
"""


class ADRDoc(StructuredNLDoc):
    """Document model for ADR nodes (Architecture Decision Records)."""

    frontmatter: dict = Field(
        description="YAML frontmatter with identity, adr, edges, compliance"
    )
    title: str = Field(description="Title of the decision")
    abstract: str = Field(description="One-paragraph summary of the decision")
    context: str = Field(description="Problem context and background")
    decision: str = Field(description="The decision that was made")
    consequences: str = Field(description="Positive and negative consequences")

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

## Context

⸢rev,markdown•context⸥

## Decision

⸢rev,markdown•decision⸥

## Consequences

⸢rev,markdown•consequences⸥
"""


class SelfDocDoc(StructuredNLDoc):
    """Document model for self-documentation nodes."""

    frontmatter: dict = Field(description="YAML frontmatter")
    title: str = Field(description="Title")
    abstract: str = Field(description="One-paragraph summary")
    content: str = Field(default="", description="Additional content")

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•abstract⸥

⸢rev,markdown•content⸥
"""
