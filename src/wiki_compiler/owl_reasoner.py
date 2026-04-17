"""OWL reasoner integration for inference."""

from __future__ import annotations
from typing import Optional

from owlready2 import World


class OwlReasoner:
    """Wrapper for OWL reasoning with HermiT/Pellet."""

    def __init__(self, world: Optional[World] = None):
        self.world = world
        self.inference_ontology = None

    def sync_reasoner(self) -> dict[str, list[str]]:
        """Run HermiT reasoner and store inferred relationships."""
        if self.world is None:
            from wiki_compiler.owl_backend import get_world

            self.world = get_world()

        inferred = {}

        try:
            from wiki_compiler.owl_backend import get_ontology

            ontology = get_ontology(self.world)

            with ontology:
                try:
                    from owlready2 import sync_reasoner

                    sync_reasoner()
                    inferred["reasoning"] = ["HermiT reasoner completed"]
                except Exception as e:
                    inferred["reasoning"] = [f"Reasoner error: {e}"]

        except ImportError:
            inferred["reasoning"] = ["owlready2 not available"]

        return inferred

    def consistency_check(self) -> dict[str, list[str]]:
        """Check for contradictory knowledge via HermiT."""
        if self.world is None:
            return {"consistency": ["No world available"]}

        inconsistent = list(self.world.inconsistent_classes())
        if inconsistent:
            return {
                "consistency": ["INCONSISTENT"],
                "inconsistent_classes": [str(c) for c in inconsistent],
            }
        return {"consistency": ["CONSISTENT"]}

    def get_inferred_relationships(self) -> list[dict]:
        """Get all inferred class memberships."""
        if self.world is None:
            return []

        inferred = []
        for cls in self.world.classes():
            subclasses = list(cls.subclasses())
            for sub in subclasses:
                if sub != cls:
                    inferred.append(
                        {"superclass": str(cls), "subclass": str(sub), "inferred": True}
                    )
        return inferred
