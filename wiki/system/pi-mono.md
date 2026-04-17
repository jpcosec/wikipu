---
identity:
  node_id: "doc:wiki/system/pi-mono.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/system/pirate.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

# pi-mono

The monorepo that powers both `pi` (global install) and `pirate` (local loot).

## Packages

| Package | Description |
|---------|-------------|
| `@mariozechner/pi-ai` | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| `@mariozechner/pi-agent-core` | Agent runtime with tool calling and state management |
| `@mariozechner/pi-coding-agent` | Interactive coding agent CLI |
| `@mariozechner/pi-tui` | Terminal UI library |
| `@mariozechner/pi-web-ui` | Web UI components |

## Source

- **Repo:** https://github.com/badlogic/pi-mono
- **Loot Location:** `src/looting/pi/`

## Development

```bash
cd src/looting/pi
npm install          # Install dependencies
npm run build        # Build all packages
```

## Definition

pi-mono is the upstream monorepo containing the `@mariozechner/pi-*` npm packages that power both `pi` (global install) and `pirate` (local loot). It provides unified multi-provider LLM API, agent runtime, coding agent CLI, and terminal/web UI components. Source at https://github.com/badlogic/pi-mono.

## Examples

- npm packages powering Pirate: `@mariozechner/pi-coding-agent`, `@mariozechner/pi-ai`
- Building all packages with `npm run build`
- Reference implementation for npm monorepo structure

## Related Concepts

- `[[wiki/system/pirate.md]]` - The looted version of pi-coding-agent