---
identity:
  node_id: "doc:wiki/concepts/pirate.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/Index.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Pirate

Pirate is a looted fork of [pi](https://github.com/badlogic/pi-mono) - a coding agent CLI tool. It lives at `src/looting/pirate/` and is used for autopoietic self-experimentation.

## Rebranding Notes

### What Changed

- **CLI command**: `pi` → `pirate`
- **Config directory**: `~/.pi/` → `~/.pirate/`
- **Directory location**: `src/looting/pi/` → `src/looting/pirate/`

### What Stayed the Same

- **npm package names**: Remained as `@mariozechner/pi-*` for npm registry compatibility
- **Package versions**: Maintain lockstep versioning with upstream

## npm Retrocompatibility

The npm packages are NOT renamed because:

1. **No publishing needed**: This is a local fork for self-use
2. **Workspace resolution**: Within the monorepo, pnpm/npm resolve `@mariozechner/pi-*` via local workspace symlinks
3. **External consumers**: If someone installed `@mariozechner/pi-coding-agent` from npm, they still get the original, not this fork

If you ever want to publish this as a separate package:
1. Rename all `@mariozechner/pi-*` → `@mariozechner/pirate-*` in package.json files
2. Update workspace globs in root package.json
3. Update all internal import statements
4. Publish new packages to npm under the pirate scope

## Running Pirate

```bash
cd src/looting/pirate

# Install dependencies
pnpm install

# Build
pnpm run build

# Run tests
./pirate-test.sh

# Interactive mode
./pirate-test.sh
```

## Configuration

Pirate reads its config from `~/.pirate/agent/`:
- `auth.json` - API keys
- `settings.json` - User preferences
- `models.json` - Model configurations
- `skills/` - Custom skills
- `extensions/` - Custom extensions
- `sessions/` - Conversation history

Environment variable override: `PIRCONFIG_DIR=~/.custom-dir pirate ...`

## Usage

After running the setup once, `pirate` is callable from anywhere:

```bash
# Interactive mode
pirate

# Non-interactive mode
pirate -p "your prompt"

# With args
pirate --help
pirate --version
pirate --model anthropic/claude-sonnet-4-5 "your prompt"
```

The `pirate` command is symlinked at `~/.local/bin/pirate` and points to the wrapper at `src/looting/pirate/pirate`.

## Definition

Pirate is a looted fork of `pi-coding-agent`, adapted to run as a local binary named `pirate`. It uses a small language model (gemma 4b) with a fast but limited context window. Pirate lives in `src/looting/pirate/` and serves as the system's smaller experimental self for autopoietic self-experimentation.

## Examples

- Running `pirate "your prompt"` for one-shot task execution
- Using `wiki-compiler query` to navigate topology before reading files
- Teaching Pirate to use CLI commands efficiently given limited context

## Related Concepts

- [[topology]] — Pirate is located in the `src/looting/` zone
- [[wiki/system/pirate.md]] — Pirate's system identity
- [[wiki/concepts/pirate_curriculum.md]] — Teaching curriculum for Pirate
