from __future__ import annotations
from pathlib import Path
import networkx as nx
import pytest
from wiki_compiler.contracts import KnowledgeNode, SemanticFacet, SystemIdentity
from wiki_compiler.graph_utils import add_knowledge_node
from wiki_compiler.node_templates import (
    NodeTemplate,
    TemplateRegistry,
    build_default_template_registry,
    extract_abstract,
    validate_template_sections,
)
from wiki_compiler.builder import parse_markdown_node


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


# --- Template registry ---

def test_template_registry_stores_and_retrieves_template() -> None:
    registry = TemplateRegistry()
    template = NodeTemplate(
        node_type="concept",
        question="What is X?",
        required_sections=["abstract", "definition", "examples"],
    )
    registry.register(template)
    assert registry.get("concept").required_sections == ["abstract", "definition", "examples"]


def test_default_registry_has_standard_templates() -> None:
    registry = build_default_template_registry()
    assert set(registry.node_types) >= {"concept", "how_to", "standard", "reference", "index"}


# --- Abstract extraction ---

def test_extract_abstract_returns_first_paragraph_after_frontmatter() -> None:
    content = """
---
identity:
  node_id: "doc:wiki/foo.md"
  node_type: "concept"
edges: []
---

This is the abstract. It is two sentences long.

## Definition

Some definition here.
"""
    abstract = extract_abstract(content)
    assert abstract == "This is the abstract. It is two sentences long."


def test_extract_abstract_returns_none_when_missing() -> None:
    content = """
---
identity:
  node_id: "doc:wiki/foo.md"
  node_type: "concept"
edges: []
---

## Definition

Jumps straight to a heading with no abstract paragraph.
"""
    assert extract_abstract(content) is None


# --- Section validation ---

def test_validate_template_sections_passes_when_all_present() -> None:
    registry = build_default_template_registry()
    content = """
---
identity:
  node_id: "doc:wiki/foo.md"
  node_type: "concept"
edges: []
---

This node explains what X is.

## Definition

X is a thing.

## Examples

Here is an example.

## Related Concepts

See also Y.
"""
    missing = validate_template_sections("concept", content, registry)
    assert missing == []


def test_validate_template_sections_reports_missing_sections() -> None:
    registry = build_default_template_registry()
    content = """
---
identity:
  node_id: "doc:wiki/foo.md"
  node_type: "concept"
edges: []
---

This node explains what X is.
"""
    missing = validate_template_sections("concept", content, registry)
    assert "definition" in missing
    assert "examples" in missing


# --- Integration with parse_markdown_node ---

def test_parse_markdown_node_populates_failing_standards(tmp_path: Path) -> None:
    p = write(tmp_path / "test.md", """
---
identity:
  node_id: "doc:test.md"
  node_type: "concept"
edges: []
---

Missing all required sections.
""")
    node, _ = parse_markdown_node(p)
    assert node is not None
    assert "definition" in node.compliance.failing_standards
    assert "examples" in node.compliance.failing_standards
