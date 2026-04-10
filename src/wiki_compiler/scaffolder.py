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
    """Simple initialization of the base directory structure."""
    bootstrap_repository(Path("."), "New Project")


def bootstrap_repository(project_root: Path, project_name: str):
    """Creates the full directory structure and seed files for a new Wikipu project."""
    directories = [
        "raw",
        "wiki/adrs",
        "wiki/concepts",
        "wiki/how_to",
        "wiki/reference",
        "wiki/standards/artifacts",
        "wiki/standards/languages",
        "manifests",
        "desk/proposals",
        "desk/autopoiesis/cycles",
        "desk/autopoiesis/sessions",
        "desk/autopoiesis/trails",
        "plan_docs/issues/gaps",
        "plan_docs/issues/unimplemented",
        "future_docs",
        "src",
        "tests",
    ]
    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / ".gitkeep").touch()

    # Seed Index.md files
    wiki_index = project_root / "wiki/Index.md"
    if not wiki_index.exists():
        wiki_index.write_text(textwrap.dedent(f"""
            ---
            identity:
              node_id: "doc:wiki/Index.md"
              node_type: "index"
            compliance:
              status: "implemented"
              failing_standards: []
            ---
            
            # {project_name} Knowledge Base
            
            This is the central entry point for the {project_name} wiki.
        """).strip() + "\n", encoding="utf-8")

    # Seed Gates.md
    gates_path = project_root / "desk/Gates.md"
    if not gates_path.exists():
        gates_path.write_text("| gate_id | proposal | opened | description | status |\n|---|---|---|---|---|\n", encoding="utf-8")

    print(f"[✅] Wikipu ecosystem bootstrapped for '{project_name}'.")


def upgrade_repository(project_root: Path):
    """Upgrades an existing Wikipu repository to the latest structure and markers."""
    # Ensure manifests and desk exist (new in 1.1.0)
    directories = [
        "manifests",
        "desk/proposals",
        "desk/autopoiesis/cycles",
    ]
    for directory in directories:
        dir_path = project_root / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            (dir_path / ".gitkeep").touch()
            print(f"[INFO] Created missing directory: {directory}")

    # Seed Gates.md if missing
    gates_path = project_root / "desk/Gates.md"
    if not gates_path.exists():
        gates_path.write_text("| gate_id | proposal | opened | description | status |\n|---|---|---|---|---|\n", encoding="utf-8")
        print("[INFO] Created missing desk/Gates.md")

    print("[✅] Wikipu ecosystem upgraded to latest version.")
