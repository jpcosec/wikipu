"""
Creates immutable scaffolding for new modules.
Initializes code structure, contracts, and tests based on House Rules.
"""
import os
from pathlib import Path
import textwrap


def generate_scaffolding(module_path: Path, intent: str):
    """Creates the immutable structure of a new module."""
    if module_path.exists():
        raise FileExistsError(f"Module {module_path} already exists.")

    os.makedirs(module_path, exist_ok=True)
    module_name = module_path.name

    # 1. Generate contracts.py
    contracts_content = textwrap.dedent(f"""
        from pydantic import BaseModel, Field
        
        class {module_name.capitalize()}Input(BaseModel):
            pass
            
        class {module_name.capitalize()}Output(BaseModel):
            pass
    """)
    (module_path / "contracts.py").write_text(contracts_content, encoding="utf-8")

    # 2. Generate __init__.py
    (module_path / "__init__.py").write_text(
        f"# Public surface of {module_name}\n", encoding="utf-8"
    )

    # 3. Generate README.md (Wiki Node with YAML Frontmatter)
    readme_content = textwrap.dedent(f"""
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


def init_repository():
    """Creates the base directory structure required by the House Rules."""
    directories = [
        "raw",
        "wiki/adrs",
        "wiki/concepts",
        "wiki/standards",
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create a .gitkeep to ensure Git tracks empty folders
        (Path(directory) / ".gitkeep").touch()

    print("[✅] Wikipu ecosystem initialized. Base folders created.")
