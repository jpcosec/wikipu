"""
Task document models using StructuredNLDoc for idempotent roundtrips.
"""

from sldb import StructuredNLDoc
from pydantic import Field
from typing import Literal


class TaskDoc(StructuredNLDoc):
    """A task document that can roundtrip between Markdown and structured data."""

    frontmatter: dict | None = Field(
        default=None, description="YAML frontmatter containing task metadata"
    )
    title: str = Field(description="Task title shown as H1 heading")
    description: str = Field(description="Task description in markdown")
    tasks: list[str] = Field(
        default_factory=list, description="List of subtask items (checkboxes)"
    )
    verification: str = Field(
        default="", description="Verification instructions in markdown"
    )

    __template__ = """---
⸢rev,dict•frontmatter⸥
---

# ⸢rev•title⸥

⸢rev,markdown•description⸥

## Tasks

- ⸢rev,list•tasks⸥

## Verification

⸢rev,markdown•verification⸥
"""
