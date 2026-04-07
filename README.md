# 🧠 wikipu (NetworkX Edition)

A Knowledge Graph compiler designed for LLM-driven development. It implements the **Hausordnung (House Rules)** laws to ensure architectural integrity and builds a deterministic **NetworkX-based** graph for agent reasoning.

## 🚀 Installation

### 1. From Git (Production/Usage)
Install directly from your repository to make the `wiki-compiler` command globally available:

```bash
pip install git+https://github.com/YOUR_USERNAME/llm-wiki-compiler.git
```

### 2. Local Development (Editable)
If you are modifying the compiler itself, install it in editable mode from the project root:

```bash
git clone https://github.com/YOUR_USERNAME/llm-wiki-compiler.git
cd llm-wiki-compiler
pip install -e .
```

---

## 🛠️ Usage

### Initialize a New Module
Automatically generate the mandatory `contracts.py`, `__init__.py`, and `README.md` (Wiki Node) for a new component:

```bash
wiki-compiler scaffold --module "src/core/auth" --intent "Manages user authentication and JWTs"
```

### Compile the Knowledge Graph
Resolve transclusions, bake standard Markdown for GitHub, and export the NetworkX JSON graph:

```bash
wiki-compiler build --source "src/wiki/nodes" --dest "docs/compiled" --graph "knowledge_graph.json"
```

---

## 🏛️ Key Features

- **House Rules Enforcement:** Ensures every module follows the strict Law of Structural Integrity.
- **Atomic Transclusion:** Use `![[concept_name]]` to embed shared knowledge without duplication.
- **Agent-Ready Graph:** Exports a `knowledge_graph.json` that any LLM can load via NetworkX for advanced topological reasoning (impact analysis, dependency mapping, etc.).
- **Decoupled Architecture:** Language-agnostic (English-native) and independent of any specific AI provider.

---

## 📁 Project Structure

- `raw/`: The Sanctuary. Immutable seed documents and fundamental requirements.
- `src/wiki/`: Source nodes with YAML frontmatter and transclusion syntax.
- `docs/compiled/`: Standard Markdown output optimized for GitHub/Web reading.
- `knowledge_graph.json`: The machine-readable brain of your repository.
