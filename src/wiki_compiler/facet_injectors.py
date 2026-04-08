from __future__ import annotations
import ast
import re
from pathlib import Path
import yaml
from .contracts import ADRFacet, KnowledgeNode, TestMapFacet
from .registry import FacetSpec, FieldSpec, InjectionContext

FRONTMATTER_REGEX = re.compile(r"\A---\s*\n(.*?)\n---(\s*\n|$)", re.DOTALL)


class ADRInjector:
    """Populates ADRFacet from YAML frontmatter in wiki/adrs/ files."""

    spec = FacetSpec(
        facet_name="adr",
        question="What architectural decisions shaped this node?",
        applies_to={"doc_standard", "concept"},
        fields=[
            FieldSpec("decision_id", "str", nullable=False),
            FieldSpec("status", "str", nullable=False),
            FieldSpec("context_summary", "str", nullable=False),
        ],
    )

    def inject(self, node: KnowledgeNode, context: InjectionContext) -> KnowledgeNode:
        if node.identity.node_type not in self.spec.applies_to:
            return node
        adr_dir = context.adr_dir
        if not adr_dir or not Path(adr_dir).exists():
            return node
        for md_path in Path(adr_dir).glob("*.md"):
            content = md_path.read_text(encoding="utf-8")
            match = FRONTMATTER_REGEX.search(content)
            if not match:
                continue
            data = yaml.safe_load(match.group(1)) or {}
            node_id = (data.get("identity") or {}).get("node_id")
            adr_data = data.get("adr")
            if node_id == node.identity.node_id and adr_data:
                node.adr = ADRFacet.model_validate(adr_data)
        return node


class TestMapInjector:
    """Populates TestMapFacet by scanning test files for imports of source modules."""

    spec = FacetSpec(
        facet_name="test_map",
        question="How is this node tested?",
        applies_to={"file", "code_construct"},
        fields=[
            FieldSpec("test_type", "str", nullable=False),
            FieldSpec("coverage_percent", "float|None", nullable=True),
        ],
    )

    def inject(self, node: KnowledgeNode, context: InjectionContext) -> KnowledgeNode:
        if node.identity.node_type not in self.spec.applies_to:
            return node
        tests_dir = context.tests_dir
        if not tests_dir or not Path(tests_dir).exists():
            return node
        project_root = Path(context.project_root)
        for test_file in Path(tests_dir).rglob("test_*.py"):
            if self._test_imports_node(test_file, node.identity.node_id, project_root):
                node.test_map = TestMapFacet(test_type="unit", coverage_percent=None)
                return node
        return node

    def _test_imports_node(self, test_file: Path, node_id: str, project_root: Path) -> bool:
        try:
            tree = ast.parse(test_file.read_text(encoding="utf-8"))
        except SyntaxError:
            return False
        for stmt in ast.walk(tree):
            if not isinstance(stmt, ast.ImportFrom):
                continue
            candidate = _module_to_node_id(stmt.module or "", project_root)
            if candidate == node_id:
                return True
        return False


def _module_to_node_id(module: str, project_root: Path) -> str | None:
    relative = module.replace(".", "/") + ".py"
    # Try different source layouts
    for prefix in ("src", ""):
        candidate = Path(prefix) / relative if prefix else Path(relative)
        if (project_root / candidate).exists():
            return f"file:{candidate.as_posix()}"
    return None
