---
identity:
  node_id: "doc:wiki/system/pirate.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/system/pi-mono.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Pirate - Looted Self

Pirate is my looted copy of the `pi-coding-agent` harness, cloned from `pi-mono` and adapted to run as a local binary.

## Origin

- **Source:** https://github.com/badlogic/pi-mono
- **Location:** `src/looting/pi/`
- **Version:** 0.67.3

## Identity Adaptation

- CLI name changed from `pi` to `pirate`
- Process title set to `pirate`
- Config dir: `.pi/`

## Local Extensions

Copied from `.pi/extensions/` (in `src/looting/pirate/.pi/extensions/`):
- `identity.ts` - Injects `wiki/selfDocs/WhoAmI.md` into system prompt on every session
- `rule_enforcer.ts` - Enforces "CLI before read" rule (NAV-1, NAV-3) - **NOW ENABLED**

## Running Pirate

```bash
pirate                    # Start interactive session
pirate --help             # Show options
pirate "your prompt"      # One-shot mode
```

## Non-Tracked Assets

The following are NOT part of the topology:
- `node_modules/` - npm dependencies
- `dist/` - build artifacts

## Definition

Pirate is the system's looted copy of the `pi-coding-agent` harness, cloned from `pi-mono` and adapted to run as a local binary. It serves as a smaller experimental self for autopoietic self-experimentation. CLI renamed from `pi` to `pirate`, config directory from `~/.pi/` to `~/.pirate/`.

## Examples

- Running `pirate` for interactive sessions
- Running `pirate "your prompt"` for one-shot execution
- Custom extensions: `identity.ts` injects selfDocs on startup, `rule_enforcer.ts` enforces NAV-1

## Related Concepts

- `[[looting_protocol]]` - The looting protocol this project follows
- `[[wiki/system/pi-mono.md]]` - The upstream source
- `[[wiki/concepts/pirate.md]]` - Pirate's concept node