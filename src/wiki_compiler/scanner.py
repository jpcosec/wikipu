"""
Scans Python source code using AST to extract semantics, code structure, and I/O.
It identifies modules, classes, and functions, generating corresponding KnowledgeNode objects.
"""

from __future__ import annotations

import ast
import fnmatch
import inspect
import re
from dataclasses import dataclass
from pathlib import Path

from .contracts import (
    ASTFacet,
    ComplianceFacet,
    Edge,
    IOFacet,
    KnowledgeNode,
    SemanticFacet,
    SystemIdentity,
)


IO_LINE_RE = re.compile(
    r"^(?:input|inputs|output|outputs|i/o):\s*(?P<medium>memory|disk|network)\s*\|\s*(?P<path>[^|]+?)\s*(?:\|\s*(?P<schema>.+))?$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class IgnoreRule:
    """Represents a rule for ignoring files during scanning, based on a glob pattern."""

    pattern: str
    reason: str | None

    def matches(self, path: str) -> bool:
        """Determines if the given path matches the ignore pattern."""
        return fnmatch.fnmatch(path, self.pattern) or fnmatch.fnmatch(
            path, f"{self.pattern}/**"
        )


from .protocols import ScannerPlugin


def scan_codebase(
    project_root: Path,
    source_roots: list[Path] | None = None,
    wikiignore_path: Path | None = None,
    plugins: list[ScannerPlugin] | None = None,
) -> list[KnowledgeNode]:
    """Recursively scans source directories for knowledge nodes using available scanner plugins."""
    roots = source_roots or [project_root / "src"]
    ignore_rules = load_wikiignore_rules(
        wikiignore_path or project_root / ".wikiignore"
    )

    # Use default plugins if none provided
    if plugins is None:
        plugins = [PythonScanner(), TypeScriptScanner()]

    nodes: list[KnowledgeNode] = []

    # Map extensions to plugins
    extension_map: dict[str, ScannerPlugin] = {}
    for plugin in plugins:
        for ext in plugin.supported_extensions:
            extension_map[ext] = plugin

    for root in roots:
        if not root.exists():
            continue
        for file_path in sorted(p for p in root.rglob("*") if p.is_file()):
            # Rule: Hidden files/directories are implicitly excluded (Not-Self)
            if any(part.startswith(".") for part in file_path.parts):
                continue

            rel_path = file_path.relative_to(project_root).as_posix()
            reason = match_ignore_reason(rel_path, ignore_rules)
            if reason is not None:
                nodes.append(build_ignored_file_node(rel_path, reason))
                continue

            plugin = extension_map.get(file_path.suffix)
            if plugin:
                nodes.extend(plugin.scan(file_path, project_root))

    return nodes


class PythonScanner:
    """Scanner plugin for Python source code."""

    @property
    def supported_extensions(self) -> set[str]:
        return {".py"}

    def scan(self, path: Path, project_root: Path) -> list[KnowledgeNode]:
        return scan_python_file(project_root, path)


class TypeScriptScanner:
    """Scanner plugin for TypeScript source code."""

    @property
    def supported_extensions(self) -> set[str]:
        return {".ts", ".tsx"}

    def scan(self, path: Path, project_root: Path) -> list[KnowledgeNode]:
        # For now, return a basic file node. Full extraction to be added.
        rel_path = path.relative_to(project_root).as_posix()
        return [
            KnowledgeNode(
                identity=SystemIdentity(node_id=f"file:{rel_path}", node_type="file"),
                semantics=SemanticFacet(
                    intent=f"TypeScript source file `{rel_path}`.", raw_docstring=None
                ),
                compliance=ComplianceFacet(status="implemented", failing_standards=[]),
            )
        ]


def scan_python_sources(
    project_root: Path,
    source_roots: list[Path] | None = None,
    wikiignore_path: Path | None = None,
) -> list[KnowledgeNode]:
    """Legacy wrapper for backward compatibility."""
    return scan_codebase(project_root, source_roots, wikiignore_path, [PythonScanner()])


def load_wikiignore_rules(wikiignore_path: Path) -> list[IgnoreRule]:
    """Reads and parses the .wikiignore file into a list of IgnoreRule objects."""
    if not wikiignore_path.exists():
        return []
    rules: list[IgnoreRule] = []
    for raw_line in wikiignore_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        pattern, _, comment = line.partition(" #")
        rules.append(
            IgnoreRule(pattern=pattern.strip(), reason=comment.strip() or None)
        )
    return rules


def match_ignore_reason(path: str, rules: list[IgnoreRule]) -> str | None:
    """Returns the reason a path is ignored if it matches any of the provided rules."""
    reason: str | None = None
    for rule in rules:
        if rule.matches(path):
            reason = rule.reason or "Ignored by .wikiignore"
    return reason


def build_ignored_file_node(rel_path: str, reason: str) -> KnowledgeNode:
    """Creates a KnowledgeNode representing a file that has been explicitly ignored."""
    return KnowledgeNode(
        identity=SystemIdentity(node_id=f"file:{rel_path}", node_type="file"),
        semantics=SemanticFacet(
            intent=f"Ignored source file `{rel_path}`.", raw_docstring=None
        ),
        ast=ASTFacet(
            construct_type="script", signatures=[f"module {rel_path}"], dependencies=[]
        ),
        compliance=ComplianceFacet(
            status="exempt", exemption_reason=reason, failing_standards=[]
        ),
    )


def scan_python_file(project_root: Path, file_path: Path) -> list[KnowledgeNode]:
    """Analyzes a single Python file and returns nodes for the module and its constructs."""
    rel_path = file_path.relative_to(project_root).as_posix()
    source = inspect.cleandoc(file_path.read_text(encoding="utf-8")) + "\n"
    module_ast = ast.parse(source, filename=rel_path)
    module_docstring = ast.get_docstring(module_ast)
    import_lines = collect_import_lines(module_ast)
    module_node = KnowledgeNode(
        identity=SystemIdentity(node_id=f"file:{rel_path}", node_type="file"),
        edges=[],
        semantics=build_semantic_facet(
            module_docstring, fallback=f"Python module `{rel_path}`."
        ),
        ast=ASTFacet(
            construct_type="script",
            signatures=[f"module {rel_path}"],
            dependencies=import_lines,
        ),
        io_ports=parse_docstring_io(module_docstring) + infer_io_from_ast(module_ast),
        compliance=ComplianceFacet(status="implemented", failing_standards=[]),
    )
    nodes = [module_node]
    for statement in module_ast.body:
        if isinstance(statement, ast.FunctionDef | ast.AsyncFunctionDef):
            nodes.append(build_function_node(rel_path, statement))
            module_node.edges.append(
                Edge(
                    target_id=f"code:{rel_path}:{statement.name}",
                    relation_type="contains",
                )
            )
        elif isinstance(statement, ast.ClassDef):
            nodes.append(build_class_node(rel_path, statement))
            module_node.edges.append(
                Edge(
                    target_id=f"code:{rel_path}:{statement.name}",
                    relation_type="contains",
                )
            )
    return nodes


def build_function_node(
    rel_path: str, statement: ast.FunctionDef | ast.AsyncFunctionDef
) -> KnowledgeNode:
    """Constructs a KnowledgeNode for a Python function or async function."""
    docstring = ast.get_docstring(statement)
    compliance = detect_exemption(statement)
    return KnowledgeNode(
        identity=SystemIdentity(
            node_id=f"code:{rel_path}:{statement.name}", node_type="code_construct"
        ),
        semantics=build_semantic_facet(
            docstring, fallback=f"Function `{statement.name}` in `{rel_path}`."
        ),
        ast=ASTFacet(
            construct_type="function",
            signatures=[format_function_signature(statement)],
            dependencies=decorator_names(statement.decorator_list),
        ),
        io_ports=parse_docstring_io(docstring) + infer_io_from_ast(statement),
        compliance=compliance
        or ComplianceFacet(status="implemented", failing_standards=[]),
    )


def build_class_node(rel_path: str, statement: ast.ClassDef) -> KnowledgeNode:
    """Constructs a KnowledgeNode for a Python class, including its methods in the signature."""
    docstring = ast.get_docstring(statement)
    signatures = [f"class {statement.name}"]
    signatures.extend(
        format_function_signature(child)
        for child in statement.body
        if isinstance(child, ast.FunctionDef | ast.AsyncFunctionDef)
    )
    compliance = detect_exemption(statement)
    return KnowledgeNode(
        identity=SystemIdentity(
            node_id=f"code:{rel_path}:{statement.name}", node_type="code_construct"
        ),
        semantics=build_semantic_facet(
            docstring, fallback=f"Class `{statement.name}` in `{rel_path}`."
        ),
        ast=ASTFacet(
            construct_type="class",
            signatures=signatures,
            dependencies=[base_name(base) for base in statement.bases],
        ),
        io_ports=parse_docstring_io(docstring),
        compliance=compliance
        or ComplianceFacet(status="implemented", failing_standards=[]),
    )


def build_semantic_facet(docstring: str | None, fallback: str) -> SemanticFacet:
    """Creates a SemanticFacet by extracting the intent from a docstring or using a fallback."""
    intent = fallback
    if docstring:
        intent = next(
            (line.strip() for line in docstring.splitlines() if line.strip()), fallback
        )
    return SemanticFacet(intent=intent, raw_docstring=docstring)


def collect_import_lines(module_ast: ast.Module) -> list[str]:
    """Extracts all import and from-import statements from a module's AST."""
    imports: list[str] = []
    for statement in module_ast.body:
        if isinstance(statement, ast.Import):
            for alias in statement.names:
                imports.append(f"import {alias.name}")
        elif isinstance(statement, ast.ImportFrom):
            module_name = "." * statement.level + (statement.module or "")
            imported = ", ".join(alias.name for alias in statement.names)
            imports.append(f"from {module_name} import {imported}")
    return imports


def decorator_names(decorators: list[ast.expr]) -> list[str]:
    """Returns a list of names for all decorators applied to a construct."""
    return [base_name(decorator) for decorator in decorators]


def base_name(node: ast.expr) -> str:
    """Resolves the string name of an AST expression, such as a variable or attribute."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{base_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Call):
        return base_name(node.func)
    return ast.unparse(node)


def format_function_signature(statement: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """Generates a string representation of a function's signature from its AST node."""
    args = [arg.arg for arg in statement.args.posonlyargs + statement.args.args]
    defaults_start = len(args) - len(statement.args.defaults)
    rendered_args: list[str] = []
    for index, arg in enumerate(statement.args.posonlyargs + statement.args.args):
        rendered = arg.arg
        if arg.annotation is not None:
            rendered += f": {ast.unparse(arg.annotation)}"
        if index >= defaults_start and statement.args.defaults:
            default = statement.args.defaults[index - defaults_start]
            rendered += f" = {ast.unparse(default)}"
        rendered_args.append(rendered)
    if statement.args.vararg is not None:
        rendered_args.append(f"*{statement.args.vararg.arg}")
    for arg, default in zip(statement.args.kwonlyargs, statement.args.kw_defaults):
        rendered = arg.arg
        if arg.annotation is not None:
            rendered += f": {ast.unparse(arg.annotation)}"
        if default is not None:
            rendered += f" = {ast.unparse(default)}"
        rendered_args.append(rendered)
    if statement.args.kwarg is not None:
        rendered_args.append(f"**{statement.args.kwarg.arg}")
    prefix = "async def" if isinstance(statement, ast.AsyncFunctionDef) else "def"
    signature = f"{prefix} {statement.name}({', '.join(rendered_args)})"
    if statement.returns is not None:
        signature += f" -> {ast.unparse(statement.returns)}"
    return (
        signature.removeprefix("def ")
        if prefix == "def"
        else signature.removeprefix("async def ")
    )


def detect_exemption(
    statement: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef,
) -> ComplianceFacet | None:
    """Identifies if a construct is marked with @wiki_exempt and returns its compliance facet."""
    for decorator in statement.decorator_list:
        if base_name(decorator).endswith("wiki_exempt"):
            reason = extract_exemption_reason(decorator)
            return ComplianceFacet(
                status="exempt", exemption_reason=reason, failing_standards=[]
            )
    return None


def extract_exemption_reason(decorator: ast.expr) -> str:
    """Extracts the 'reason' argument from a @wiki_exempt decorator call."""
    if isinstance(decorator, ast.Call):
        for keyword in decorator.keywords:
            if (
                keyword.arg == "reason"
                and isinstance(keyword.value, ast.Constant)
                and isinstance(keyword.value.value, str)
            ):
                return keyword.value.value
        if (
            decorator.args
            and isinstance(decorator.args[0], ast.Constant)
            and isinstance(decorator.args[0].value, str)
        ):
            return decorator.args[0].value
    return "Declared via @wiki_exempt"


def parse_docstring_io(docstring: str | None) -> list[IOFacet]:
    """Parses I/O port declarations from a docstring using regular expressions."""
    if not docstring:
        return []
    ports: list[IOFacet] = []
    for raw_line in docstring.splitlines():
        match = IO_LINE_RE.match(raw_line.strip())
        if not match:
            continue
        ports.append(
            IOFacet(
                medium=match.group("medium").lower(),
                path_template=match.group("path").strip(),
                schema_ref=(match.group("schema") or "").strip() or None,
            )
        )
    return ports


def infer_io_from_ast(tree: ast.AST) -> list[IOFacet]:
    """Statically infers I/O ports by searching for common file I/O patterns in the AST."""
    ports: list[IOFacet] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        inferred = (
            infer_open_call(node) or infer_pathlib_call(node) or infer_json_call(node)
        )
        if inferred is not None:
            ports.append(inferred)
    return ports


def infer_open_call(node: ast.Call) -> IOFacet | None:
    """Infers an I/O port from a call to the built-in 'open' function."""
    if not isinstance(node.func, ast.Name) or node.func.id != "open" or not node.args:
        return None
    path = extract_string(node.args[0])
    if path is None:
        return None
    mode = extract_string(node.args[1]) if len(node.args) > 1 else "r"
    medium = "disk"
    direction: Literal["input", "output"] = "input"
    schema_ref = None
    if mode and any(flag in mode for flag in ("w", "a", "x")):
        direction = "output"
    if path:
        if path.endswith(".json"):
            schema_ref = "json"
        elif path.endswith(".csv"):
            schema_ref = "csv"
        elif path.endswith((".yaml", ".yml")):
            schema_ref = "yaml"
    return IOFacet(
        medium=medium, path_template=path, direction=direction, schema_ref=schema_ref
    )


def infer_pathlib_call(node: ast.Call) -> IOFacet | None:
    """Infers an I/O port from calls to Path methods like read_text or write_text."""
    if not isinstance(node.func, ast.Attribute):
        return None
    if node.func.attr not in {"read_text", "write_text", "read_bytes", "write_bytes"}:
        return None
    direction: Literal["input", "output"] = "input"
    if node.func.attr.startswith("write"):
        direction = "output"

    owner = node.func.value
    # Case 1: Path("foo.txt").read_text()
    schema_ref = None
    if isinstance(owner, ast.Call) and base_name(owner.func) == "Path" and owner.args:
        path = extract_string(owner.args[0])
        if path:
            if path.endswith(".json"):
                schema_ref = "json"
            elif path.endswith(".csv"):
                schema_ref = "csv"
            elif path.endswith((".yaml", ".yml")):
                schema_ref = "yaml"
            return IOFacet(
                medium="disk",
                path_template=path,
                direction=direction,
                schema_ref=schema_ref,
            )

    # Case 2: p = Path("foo.txt"); p.read_text()
    # We don't have full data flow, but we can at least return a generic disk IO
    # if the attribute is on something that looks like a path variable or if we just want to mark the file as doing IO.
    # For now, let's keep it simple as per instructions.
    return None


def infer_json_call(node: ast.Call) -> IOFacet | None:
    """Infers an I/O port from calls to json.load or json.dump."""
    name = base_name(node.func)
    if name == "json.load":
        return IOFacet(medium="disk", direction="input", schema_ref="json")
    if name == "json.dump":
        return IOFacet(medium="disk", direction="output", schema_ref="json")
    return None


def extract_string(node: ast.AST) -> str | None:
    """Extracts a literal string value from an AST node if possible."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None
