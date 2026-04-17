"""SHACL shapes for KnowledgeNode validation."""

from typing import Any


NODE_SHAPE_TEMPLATE = {
    "nodeKind": "sh:BlankNodeOrIRI",
    "property": [
        {
            "path": "https://wikipu.ai/ontology/node_id",
            "minCount": 1,
            "maxCount": 1,
            "datatype": "http://www.w3.org/2001/XMLSchema#string",
        },
        {
            "path": "https://wikipu.ai/ontology/node_type",
            "minCount": 1,
            "maxCount": 1,
            "in": [
                "index",
                "concept",
                "standard",
                "reference",
                "how_to",
                "adrs",
                "selfDoc",
                "workflow",
                "faq",
            ],
        },
        {
            "path": "https://wikipu.ai/ontology/compliance_status",
            "in": ["implemented", "partial", "pending", "violated"],
        },
    ],
}


def get_knowledge_node_shape() -> dict[str, Any]:
    """Return SHACL shape for KnowledgeNode."""
    return {
        "$schema": "http://www.w3.org/ns/shacl#",
        "type": "NodeShape",
        "targetClass": "https://wikipu.ai/ontology/KnowledgeNode",
        **NODE_SHAPE_TEMPLATE,
    }


def get_edge_shape() -> dict[str, Any]:
    """Return SHACL shape for edges."""
    return {
        "$schema": "http://www.w3.org/ns/shacl#",
        "type": "PropertyShape",
        "path": "https://wikipu.ai/ontology/relation_type",
        "in": [
            "contains",
            "implements",
            "references",
            "supersedes",
            "derives_from",
            "conflicts_with",
            "validates",
        ],
    }
