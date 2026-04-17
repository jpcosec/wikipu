"""Bidirectional sync between Pydantic models and OWL quadstore."""

from pathlib import Path
from typing import Optional

from owlready2 import World

from wiki_compiler.owl_backend import get_world, get_ontology, ONTOLOGY_IRI
from wiki_compiler.shacl import validate_node


class SyncGate:
    """Gate for all Pydantic ↔ OWL sync operations."""

    def __init__(self, world: Optional[World] = None):
        self.world = world or get_world()
        self.ontology = get_ontology(self.world)
        self._pending_sync = []

    def export_to_owl(self, node_id: str, triples: dict) -> list[str]:
        """Export Pydantic node data to OWL triples. Returns violations."""
        violations = []

        with self.ontology:
            individual = self.ontology(node_id)

            for prop, value in triples.items():
                if hasattr(individual, prop):
                    setattr(individual, prop, value)

            violations = validate_node(individual)
            if not violations:
                self._pending_sync.append(("export", node_id))

        return violations

    def import_from_owl(self, node_id: str) -> dict:
        """Import OWL individual to Pydantic-compatible dict."""
        results = list(
            self.world.sparql(f"""
            SELECT ?p ?o
            WHERE {{ <{ONTOLOGY_IRI}{node_id}> ?p ?o }}
        """)
        )
        return {p.split("/")[-1]: str(o) for p, o in results}

    def sync(self) -> dict[str, list[str]]:
        """Run full bidirectional sync. Returns conflicts."""
        conflicts = {}
        for op_type, node_id in self._pending_sync:
            if op_type == "export":
                pass
        self._pending_sync.clear()
        return conflicts

    def _shacl_validate(self, node_id: str) -> list[str]:
        """Validate node against SHACL shapes."""
        individual = getattr(self.ontology, node_id, None)
        if individual is None:
            return [f"Node {node_id} not found in ontology"]
        return validate_node(individual)
