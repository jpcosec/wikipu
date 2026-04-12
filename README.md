# 🧠 Wikipu: An LLM-Driven Wiki Ecosystem

Welcome to **Wikipu**. This is not just a CLI tool; it is a self-contained **Seed Repository** and **Development Operating System** designed for human-AI collaboration.

Wikipu allows you to "compile" knowledge from code, documentation, and raw brainstorming into a unified, machine-readable **Knowledge Graph**.

## 🚀 The 6-Step Workflow

Wikipu is designed to be the starting point for any new or existing project.

1.  **Download as Seed**: Clone this repository as the foundation for your project.
2.  **Install**: `pip install -e .` to get the `wiki-compiler` command.
3.  **Plug in your Code**: Move your existing code into `src/` or start building new modules using `wiki-compiler scaffold`.
4.  **Define the Raw Source**: Dump your "seminal" thoughts, chat logs, and messy notes into `raw/`.
5.  **Follow the Rules**: Adhere to `desk/STANDARDS.md` and `wiki/standards/house_rules.md` for code and documentation.
6.  **Compile & Run**: Run `wiki-compiler build` to generate the knowledge graph. Run `wiki-compiler run` to start the autopoiesis cycle.

## 🛠️ Quick Start

### 1. Install
```bash
pip install -e .
```

**If `wiki-compiler` command is not found after install:**
- Restart your terminal (or open a new shell)
- Verify Python path: `which python` and `echo $PATH`
- Try: `python -m wiki_compiler build` as fallback
- Or run directly: `python -c "from wiki_compiler.main import main; main()" -- build`

### 2. Build the Graph
```bash
wiki-compiler build
```

### 3. Start the Autopoiesis Cycle (Optional)
```bash
wiki-compiler run
```
This runs the self-maintaining loop - detects perturbations, creates cycles, pauses at Gates for human approval.

## 📂 The 4-Zone Model

To keep the ecosystem tidy, we follow a strict temporal and conceptual organization:

- **`raw/` (Origin)**: The immutable seed source. Read-only for LLMs, contains the "ore" refined into the wiki.
- **`wiki/` (Truth)**: The living documentation, standards, and concepts. Single source of truth for humans and machines.
- **`desk/` (Active)**: Active work surface. Ephemeral — items deleted when resolved. Contains issues, tasks, and gates.
- **`drawers/` (Deferred)**: Deferred work surface. Ideas waiting for prioritization. Stale after 6 months.

## 📖 Deep Dive

For detailed instructions on architecture, rules, and advanced usage, explore the `wiki/` directory:

*   [Wiki Front Page](wiki/Index.md)
*   [How it Works](wiki/concepts/how_wikipu_works.md)
*   [How to Use the CLI](wiki/how_to_use.md)
*   [How to Add a Component](wiki/how_to_add_component.md)
*   [House Rules](wiki/standards/house_rules.md)
*   [Librarian Agent Protocol](agents/librarian/intro.md)

---
*Wikipu ensures that code is the truth, documentation is the why, and the wiki is the index.*
