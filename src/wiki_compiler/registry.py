"""
Central registry for Knowledge Graph facets and injection plugins.
Maps facet names to their questions, schemas, and applicable node types.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FieldSpec:
    """Defines the metadata for a single field within a facet."""
    name: str
    type: str        # e.g. "str", "float|None", "list[str]"
    nullable: bool


@dataclass
class FacetSpec:
    """Describes a facet dimension, including its intent and associated fields."""
    facet_name: str
    question: str    # The one question this facet answers
    applies_to: set[str]  # node_type values this facet is relevant for
    fields: list[FieldSpec]


@dataclass
class InjectionContext:
    """Provides environmental context for facet injection plugins."""
    project_root: Path
    adr_dir: Path | None = None
    tests_dir: Path | None = None


class FacetRegistry:
    """Central registry mapping facet names to their specs and plugins."""

    def __init__(self) -> None:
        """Initializes an empty FacetRegistry."""
        self._specs: dict[str, FacetSpec] = {}

    def register_spec(self, spec: FacetSpec) -> None:
        """Adds a FacetSpec to the registry."""
        self._specs[spec.facet_name] = spec

    def get_spec(self, facet_name: str) -> FacetSpec:
        """Retrieves a FacetSpec from the registry by its name."""
        if facet_name not in self._specs:
            raise KeyError(f"No facet registered under '{facet_name}'")
        return self._specs[facet_name]

    @property
    def facet_names(self) -> list[str]:
        """Returns a list of all registered facet names."""
        return list(self._specs)


def build_default_registry() -> FacetRegistry:
    """Returns a registry pre-populated with the built-in facet specs."""
    registry = FacetRegistry()
    registry.register_spec(FacetSpec(
        facet_name="semantics",
        question="What does this node do?",
        applies_to={"file", "code_construct", "concept", "doc_standard"},
        fields=[
            FieldSpec("intent", "str", nullable=False),
            FieldSpec("raw_docstring", "str|None", nullable=True),
        ],
    ))
    registry.register_spec(FacetSpec(
        facet_name="ast",
        question="How is this node structured?",
        applies_to={"file", "code_construct"},
        fields=[
            FieldSpec("construct_type", "str", nullable=False),
            FieldSpec("signatures", "list[str]", nullable=False),
            FieldSpec("dependencies", "list[str]", nullable=False),
        ],
    ))
    registry.register_spec(FacetSpec(
        facet_name="io",
        question="What data does this node consume or produce?",
        applies_to={"file", "code_construct"},
        fields=[
            FieldSpec("medium", "str", nullable=False),
            FieldSpec("schema_ref", "str|None", nullable=True),
            FieldSpec("path_template", "str|None", nullable=True),
        ],
    ))
    registry.register_spec(FacetSpec(
        facet_name="compliance",
        question="How complete and rule-compliant is this node?",
        applies_to={"file", "code_construct", "directory"},
        fields=[
            FieldSpec("status", "str", nullable=False),
            FieldSpec("failing_standards", "list[str]", nullable=False),
            FieldSpec("exemption_reason", "str|None", nullable=True),
        ],
    ))
    registry.register_spec(FacetSpec(
        facet_name="test_map",
        question="How is this node tested?",
        applies_to={"file", "code_construct"},
        fields=[
            FieldSpec("test_type", "str", nullable=False),
            FieldSpec("coverage_percent", "float|None", nullable=True),
        ],
    ))
    registry.register_spec(FacetSpec(
        facet_name="adr",
        question="What architectural decisions shaped this node?",
        applies_to={"doc_standard", "concept"},
        fields=[
            FieldSpec("decision_id", "str", nullable=False),
            FieldSpec("status", "str", nullable=False),
            FieldSpec("context_summary", "str", nullable=False),
        ],
    ))
    return registry
