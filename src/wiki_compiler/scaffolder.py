import os
from pathlib import Path
import textwrap

def generate_scaffolding(module_path: Path, intent: str):
    """Crea la estructura inmutable de un nuevo módulo."""
    if module_path.exists():
        raise FileExistsError(f"El módulo {module_path} ya existe.")
        
    os.makedirs(module_path, exist_ok=True)
    module_name = module_path.name

    # 1. Generar contracts.py
    contracts_content = textwrap.dedent(f"""\
        from pydantic import BaseModel, Field
        
        class {module_name.capitalize()}Input(BaseModel):
            pass
            
        class {module_name.capitalize()}Output(BaseModel):
            pass
    """)
    (module_path / "contracts.py").write_text(contracts_content, encoding="utf-8")

    # 2. Generate __init__.py
    (module_path / "__init__.py").write_text(f"# Public surface of {module_name}\n", encoding="utf-8")

    # 3. Generate README.md (Wiki Node with YAML Frontmatter)
    readme_content = textwrap.dedent(f"""\
        ---
        identity:
          node_id: "dir:{module_path}"
          node_type: "directory"
        
        edges: []
        io_ports: []
        
        compliance:
          status: "scaffolding"
          failing_standards: []
        ---
        
        # 🧠 {module_name.capitalize()}
        
        **Intent:** {intent}
        
        ## 🏗️ Architecture & Features
        *TODO: Describe components or transclude shared concepts (![[concept]])*
        
        ## 📝 Data Contract
        Inputs and Outputs defined in `contracts.py`.
    """)
    (module_path / "README.md").write_text(readme_content, encoding="utf-8")
