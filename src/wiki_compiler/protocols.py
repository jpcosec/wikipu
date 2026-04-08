from __future__ import annotations
from typing import Protocol, runtime_checkable
import networkx as nx
from .contracts import AuditFinding, KnowledgeNode
from .registry import FacetSpec, InjectionContext


@runtime_checkable
class FacetInjector(Protocol):
    """A plugin that enriches graph nodes with one facet dimension."""
    spec: FacetSpec

    def inject(self, node: KnowledgeNode, context: InjectionContext) -> KnowledgeNode:
        """Return node enriched with this facet. Return unchanged if not applicable."""
        ...


@runtime_checkable
class AuditCheck(Protocol):
    """A plugin that answers: which nodes fail to answer the facet's question?"""
    check_name: str
    question: str       # e.g. "Which code nodes have no documentation?"
    related_facet: str  # facet_name this check validates

    def run(self, graph: nx.DiGraph) -> list[AuditFinding]:
        ...
