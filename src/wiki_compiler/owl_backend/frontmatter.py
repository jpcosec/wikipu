"""Extract YAML frontmatter to RDF triples."""

from typing import Any


def extract_frontmatter_triples(
    node_class, frontmatter: dict[str, Any], ontology
) -> None:
    """Convert frontmatter fields to annotation properties."""
    if not frontmatter:
        return

    identity = frontmatter.get("identity", {})
    if identity:
        node_id = identity.get("node_id", "")
        if node_id and hasattr(node_class, "node_id"):
            node_class.node_id = node_id

        node_type = identity.get("node_type", "")
        if node_type and hasattr(node_class, "node_type"):
            node_class.node_type = node_type

    compliance = frontmatter.get("compliance", {})
    if compliance:
        status = compliance.get("status", "")
        if status and hasattr(node_class, "compliance_status"):
            node_class.compliance_status = status

        failing = compliance.get("failing_standards", [])
        if hasattr(node_class, "failing_standards"):
            node_class.failing_standards = failing

    for key, value in frontmatter.items():
        if key in ("identity", "compliance"):
            continue
        if hasattr(node_class, key):
            setattr(node_class, key, str(value))
