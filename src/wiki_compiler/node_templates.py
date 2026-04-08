"""
Definitions and validation for wiki node templates.
Enforces required sections and abstract extraction for different node types.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pydantic import BaseModel


@dataclass
class NodeTemplate:
    node_type: str
    question: str
    required_sections: list[str]


class TemplateRegistry:
    """Registry for node templates."""

    def __init__(self) -> None:
        self._templates: dict[str, NodeTemplate] = {}

    def register(self, template: NodeTemplate) -> None:
        self._templates[template.node_type] = template

    def get(self, node_type: str) -> NodeTemplate:
        if node_type not in self._templates:
            # Fallback or generic template?
            return NodeTemplate(node_type, "What is this?", ["abstract"])
        return self._templates[node_type]

    @property
    def node_types(self) -> list[str]:
        return list(self._templates)


def build_default_template_registry() -> TemplateRegistry:
    registry = TemplateRegistry()
    registry.register(NodeTemplate(
        "concept",
        "What is X?",
        ["abstract", "definition", "examples", "related_concepts"]
    ))
    registry.register(NodeTemplate(
        "how_to",
        "How do I do X?",
        ["abstract", "prerequisites", "steps", "outcome"]
    ))
    registry.register(NodeTemplate(
        "standard",
        "What is the rule for X?",
        ["abstract", "rule", "rationale", "violation_examples"]
    ))
    registry.register(NodeTemplate(
        "reference",
        "How does X work technically?",
        ["abstract", "signature_or_schema", "fields", "usage_examples"]
    ))
    registry.register(NodeTemplate(
        "index",
        "What lives in this area?",
        ["abstract"]  # Content must be transclusion-only, checked by composer
    ))
    return registry


def extract_abstract(content: str) -> str | None:
    """
    Extracts the first paragraph after the YAML frontmatter.
    Must be before any markdown heading.
    """
    content = content.strip()
    # Remove frontmatter
    body = re.sub(r"\A---\s*\n.*?\n---(\s*\n|$)", "", content, flags=re.DOTALL).strip()
    if not body:
        return None
    
    # Get the first block before any heading
    lines = body.splitlines()
    if not lines:
        return None
        
    if lines[0].startswith("#"):
        return None  # No abstract before first heading
        
    # Find first paragraph (until double newline or heading)
    first_paragraph_lines = []
    for line in lines:
        if not line.strip():
            if first_paragraph_lines:
                break
            continue
        if line.startswith("#"):
            break
        first_paragraph_lines.append(line.strip())
        
    if not first_paragraph_lines:
        return None
        
    return " ".join(first_paragraph_lines)


def validate_template_sections(node_type: str, content: str, registry: TemplateRegistry) -> list[str]:
    """Returns a list of missing required sections for the given node type."""
    template = registry.get(node_type)
    missing = []
    
    # Extract headings
    headings = {
        line.lstrip("#").strip().lower().replace(" ", "_")
        for line in content.splitlines()
        if line.strip().startswith("##")
    }
    
    # Special case: abstract is usually not a heading, it's the first paragraph.
    has_abstract = extract_abstract(content) is not None
    
    for section in template.required_sections:
        if section == "abstract":
            if not has_abstract:
                missing.append("abstract")
        elif section not in headings:
            missing.append(section)
            
    return missing
