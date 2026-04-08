from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, Field


class FieldCondition(BaseModel):
    field: str
    op: Literal["eq", "ne", "is_null", "is_not_null", "contains", "gt", "lt"]
    value: Any = None


class FacetFilter(BaseModel):
    """Filter nodes by conditions on a specific facet's fields."""
    facet: str  # facet_name from the registry
    conditions: list[FieldCondition]


class GraphScope(BaseModel):
    """Restrict the query to a subgraph region."""
    descendant_of: str | None = None
    ancestor_of: str | None = None
    node_id_prefix: str | None = None  # e.g. "doc:future_docs/"


class StructuredQuery(BaseModel):
    """
    A typed query over the knowledge graph.

    Single-facet:  one FacetFilter  → answers one-dimensional questions.
    Compound:      multiple filters → intersection, answers multi-dimensional questions.
    Scoped:        with GraphScope  → restricts to a region of the graph.
    """
    filters: list[FacetFilter] = Field(default_factory=list)
    scope: GraphScope | None = None
