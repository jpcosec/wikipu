import ast
from pathlib import Path
from typing import Protocol
from .contracts import KnowledgeNode, ASTFacet, IOFacet, ComplianceFacet

# --- Interfaz Base ---
class WikiPlugin(Protocol):
    def process(self, path: Path, current_node: KnowledgeNode) -> KnowledgeNode:
        """Modifica el nodo inyectando nuevas facetas o aristas."""
        ...

# --- Plugin 1: El Lector de AST (Los Cómos) ---
class PythonASTPlugin:
    def process(self, path: Path, current_node: KnowledgeNode) -> KnowledgeNode:
        if path.suffix != ".py":
            return current_node
            
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
            
        # Extraer firmas de clases como ejemplo muy básico
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        current_node.ast = ASTFacet(
            construct_type="script",
            signatures=classes,
            dependencies=[] # Aquí agregarías lógica para parsear ast.ImportFrom
        )
        return current_node

# --- Plugin 2: El Lector de I/O (Disco) ---
class StorageIOPlugin:
    def process(self, path: Path, current_node: KnowledgeNode) -> KnowledgeNode:
        # Solo buscamos I/O en archivos que sabemos que lo manejan
        if path.name != "storage.py":
            return current_node
            
        # Lógica dummy: si el archivo existe, asumimos que escribe a disco
        # En la vida real, usarías regex o AST para buscar 'Path("output/...")'
        current_node.io_ports.append(
            IOFacet(medium="disk", path_template="output/<dynamic>/")
        )
        return current_node

# --- Plugin 3: El Auditor de Cumplimiento ---
class CompliancePlugin:
    def process(self, path: Path, current_node: KnowledgeNode) -> KnowledgeNode:
        failing = []
        status = "implemented" # Default optimista
        
        # Regla: Si es código Python, debe tener AST (inyectado por el plugin anterior)
        # y si tiene AST, debe tener docstrings.
        if path.suffix == ".py":
            if not current_node.semantics or not current_node.semantics.raw_docstring:
                failing.append("basic.md#module-docstrings-missing")
                status = "scaffolding" # Si no tiene docstring, no cuenta como implementado
                
        current_node.compliance = ComplianceFacet(
            status=status,
            failing_standards=failing
        )
        return current_node