# 🧠 Wikipu: An LLM-Driven Wiki Ecosystem

Welcome to **Wikipu**. This is not just a CLI tool; it is a self-contained **Seed Repository** and **Development Operating System** designed for human-AI collaboration.

Wikipu allows you to "compile" knowledge from code, documentation, and raw brainstorming into a unified, machine-readable **Knowledge Graph**.

## 🚀 The 6-Step Workflow

Wikipu is designed to be the starting point for any new or existing project.

1.  **Download as Seed**: Clone this repository as the foundation for your project.
2.  **Plug in your Code**: Move your existing code into `src/` or start building new modules using `wiki-compiler scaffold`.
3.  **Define the Raw Source**: Dump your "seminal" thoughts, chat logs, and messy notes into `raw/`.
4.  **Generate Navigation**: Use `wiki-compiler ingest` to turn raw notes into draft wiki nodes.
5.  **Follow the Rules**: Adhere to the `wiki/standards/00_house_rules.md` to ensure your code and documentation are perfectly aligned (Pydantic contracts, clear docstrings, and orthogonal design).
6.  **Compile & Explore**: Run `wiki-compiler build` to generate the `knowledge_graph.json`. Now, both you and your LLM can use the `wiki/` and the graph to explore, design, and implement features with perfect context.

## 🛠️ Quick Start

### 1. Initialize
If you are plugging Wikipu into an existing repo, set up the structure:
```bash
wiki-compiler init
```

### 2. Build the Graph
Generate your knowledge graph and check compliance:
```bash
wiki-compiler build
```

### 3. Ingest Raw Ideas
Transform your `raw/` files into wiki drafts:
```bash
wiki-compiler ingest
```

## 📂 The 4-Place Design

To keep the ecosystem tidy, we follow a strict temporal and conceptual organization:

- **`wiki/` (Past/Truth)**: The living documentation, standards, and concepts. This is the single source of truth for humans and machines.
- **`plan_docs/` (Present/Doing)**: Ephemeral plans and active issue tracking. Once implemented, these are deleted.
- **`future_docs/` (Future/Waiting)**: A backlog for ideas and architectural shifts not yet in progress.
- **`raw/` (Source/Origin)**: The immutable seed source. Read-only for LLMs, it contains the "ore" refined into the wiki.

## 📖 Deep Dive

For detailed instructions on architecture, rules, and advanced usage, explore the `wiki/` directory:

*   [How it Works](wiki/how_it_works.md)
*   [How to Use the CLI](wiki/how_to_use.md)
*   [How to Add a Component](wiki/how_to_add_component.md)
*   [House Rules](wiki/standards/00_house_rules.md)
*   [Librarian Agent Protocol](agents/librarian/intro.md)

---
*Wikipu ensures that code is the truth, documentation is the why, and the wiki is the index.*
