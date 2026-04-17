"""SHACL validation wrapper."""

import json
from pathlib import Path
from typing import Optional

from owlready2 import World

from wiki_compiler.owl_backend.extractor import get_world
from wiki_compiler.shacl.shapes import get_knowledge_node_shape, get_edge_shape


def validate_node(node: object, shapes: Optional[list[dict]] = None) -> list[str]:
    """Validate a node against SHACL shapes. Returns list of violations."""
    violations = []

    if shapes is None:
        shapes = [get_knowledge_node_shape(), get_edge_shape()]

    node_dict = vars(node) if hasattr(node, "__dict__") else {}

    for shape in shapes:
        shape_type = shape.get("type", "PropertyShape")

        if shape_type == "NodeShape":
            target = shape.get("targetClass", "")
            for prop in shape.get("property", []):
                path = prop.get("path", "").split("/")[-1]
                min_count = prop.get("minCount", 0)
                actual = node_dict.get(path, None)

                if min_count > 0 and not actual:
                    violations.append(f"Missing required property: {path} on {target}")

                if "in" in prop and actual:
                    allowed = prop["in"]
                    if actual not in allowed:
                        violations.append(
                            f"Invalid value '{actual}' for {path}, expected one of {allowed}"
                        )

        elif shape_type == "PropertyShape":
            path = shape.get("path", "").split("/")[-1]
            if "in" in shape:
                actual = node_dict.get(path, "")
                if actual and actual not in shape["in"]:
                    violations.append(f"Invalid edge type: {actual}")

    return violations


def validate_ontology(world: Optional[World] = None) -> dict[str, list[str]]:
    """Validate entire ontology against SHACL shapes. Returns violations by node."""
    if world is None:
        world = get_world()

    results = {}
    shapes = [get_knowledge_node_shape(), get_edge_shape()]

    ontology = list(world.individuals()) if hasattr(world, "individuals") else []
    for individual in ontology:
        violations = validate_node(individual, shapes)
        if violations:
            results[
                str(individual) if hasattr(individual, "__str__") else "unknown"
            ] = violations

    return results
