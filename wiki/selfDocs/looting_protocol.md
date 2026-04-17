---
identity:
  node_id: "doc:wiki/selfDocs/looting_protocol.md"
  node_type: "selfDoc"
edges:
  - {target_id: "doc:wiki/selfDocs/WhoAmI.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Looting Protocol

A protocol for integrating external codebases into autopoietic topology.

## Purpose

Looting external projects embeds their source code into the knowledge graph, enabling direct experimentation, modification, and self-hosted deployment. It transforms external dependencies into internal topology. Looted code becomes **part of our topology** - subject to our rules, formatting, and git workflow.

## Principles

1. **Merge, not isolate**: Looted code is *our* code now - integrated, adapted, eventually absorbed
2. **Compliance**: All looted code must conform to our formatting, styling, and linting rules
3. **Tracked**: Looted code lives in our git, commits with our commits, pushes with our pushes
4. **Adapt**: Modify looted code for our use case
5. **Extract**: Relocate useful patterns/components into our own codebase

## Protocol

### Phase 1: Initialize

1. Create `src/looting/<project-name>/`
2. Document the loot in `wiki/system/<project-name>.md`:
   - Source location (URL, package registry, etc.)
   - Purpose and relevance to autopoietic identity
   - Relationship to other topology elements

### Phase 2: Loot

1. Clone source code into `src/looting/<project-name>/`
2. Initialize as git submodule:
   ```bash
   cd src/looting/<project-name>/
   git init
   git add .
   git commit -m "Looted from <source>"
   ```
3. Add to `.gitmodules` for automatic sync:
   ```
   [submodule "src/looting/<project-name>"]
       path = src/looting/<project-name>
       url = .
   ```
4. Add `.git` to `.gitignore` (submodule tracks everything via our git)

### Phase 3: Comply

1. Apply our formatting and style:
   - Run our linters, formatters on looted code
   - Conform to our naming conventions
   - Add local development rules in `AGENTS.md`
2. Ensure imports work with our environment (use venv if needed for testing)

### Phase 4: Integrate

1. Run `wiki-compiler build` to incorporate into knowledge graph
2. Document looted architecture in wiki:
   - Key components and their roles
   - How it integrates with existing topology
   - Any modifications made during looting

### Phase 5: Verify

1. Execute the looted code successfully (run, build, deploy)
2. Test key functionality
3. If verification fails, iterate until functional

### Phase 6: Absorb (ongoing)

1. Identify reusable components
2. Relocate patterns to our own codebase
3. Deprecate looted code as components are absorbed

## Git Submodule Automation

Looted projects must auto-sync with our git. Configure `.gitmodules`:

```ini
[submodule "src/looting/pirate"]
    path = src/looting/pirate
    url = .
[submodule "src/looting/gemma-rag"]
    path = src/looting/gemma-rag
    url = .
```

The looted repos track their own history but are committed **through our main repo**:

```bash
# Auto-commit: add submodule changes when we commit main
git add src/looting/<name> && git commit -m "Update loot"

# Auto-push: push main repo, submodule pushes too
git push && git push --recurse-submodules=on-demand

# Auto-pull: pull main repo, submodules update too
git pull --recurse-submodules=on-demand
```

Add to `~/.gitconfig` for automatic behavior:

```ini
[submodule]
    recurse = on-demand
[pull]
    recurse = on-demand
[push]
    recurse = on-demand
```

## Checklist

- [ ] `src/looting/<name>/` created with source code
- [ ] `src/looting/<name>/.git` exists (local git for submodule tracking)
- [ ] `.gitmodules` updated with submodule entry
- [ ] `wiki/system/<name>.md` documents the loot
- [ ] Code complies with our formatting/style rules
- [ ] `wiki-compiler build` succeeds
- [ ] Looted code runs/compiles/deploys successfully
- [ ] Useful components identified for absorption

## Naming

Looted projects are named descriptively:
- `pirate` - looted fork of pi-coding-agent
- `gemma-rag` - looted RAG system
- `<original-name>` - if no renaming needed

## Example

See [[wiki/system/pirate]] for a complete looting example.
