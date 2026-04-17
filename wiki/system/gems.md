---
identity:
  node_id: "doc:wiki/system/gems.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/selfDocs/looting_protocol.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Gems - Local LLM CLI Tool

Gems is a shell CLI tool for interacting with local Large Language Models via [Ollama](https://ollama.com/). It provides rich prompt templates with language detection, JSON schema processing, and flexible output handling.

## Origin

- **Source:** https://github.com/jpcosec/gems.sh
- **Forked from:** CJHwong/gems.sh
- **License:** MIT
- **Location:** `src/looting/gems/`

## Files

- `gems.sh` - Original macOS version (Zsh, requires osascript, pbcopy)
- `gems-linux.sh` - Linux/FreeBSD adaptation (Bash, xclip/wl-copy, notify-send)

## Dependencies

### Required
- `ollama` - LLM runtime
- `curl` - API communication
- `jq` - JSON processing

### Optional (macOS)
- `osascript` - GUI template selection
- `pbcopy` - clipboard functionality

### Optional (Linux/FreeBSD)
- `wl-copy` or `xclip` or `xsel` - clipboard functionality
- `notify-send` - desktop notifications
- `fzf` or `rofi` - interactive template selection
- `yq` - YAML template parsing
- `glow` - markdown rendering

## Available Templates

| Template | Purpose |
|----------|---------|
| `TextReviser` | Grammar and clarity improvements |
| `Summarize` | Create concise summaries |
| `CodeReview` | Best practices and security review |
| `CodeExplain` | Simple code explanations |
| `CodeOptimize` | Performance improvements |
| `ComplexAnalysis` | Sentiment and topic analysis |
| `Brainstorm` | Creative idea generation |
| `EmailProfessional` | Professional email format |
| `BulletPoints` | Organize text into bullets |

## Running Gems

### Linux/FreeBSD
```bash
cd src/looting/gems
./gems-linux.sh -t CodeReview "function foo() { return x + y; }"
```

### macOS
```bash
cd src/looting/gems
./gems.sh -t CodeReview "function foo() { return x + y; }"
```

## Integration with Wikipu

Gems can enhance wikipu workflows:

- **Quick code review**: `./gems-linux.sh -t CodeReview "$(cat file.c)"`
- **Text improvement**: `./gems-linux.sh -t TextReviser "draft text"`
- **Offline fallback**: When cloud APIs unavailable

## Definition

Gems is a shell CLI tool for interacting with local LLMs via Ollama. It provides rich prompt templates with language detection, JSON schema processing, and flexible output handling. Available templates include CodeReview, Summarize, TextReviser, and others. Located at `src/looting/gems/`.

## Examples

- `./gems-linux.sh -t CodeReview "your code"` for code review
- `./gems-linux.sh -t TextReviser "draft text"` for grammar improvement
- Offline fallback when cloud APIs are unavailable

## Related Concepts

- [[looting_protocol]] - The protocol used for this loot
- [[wiki/system/pirate.md]] - Looted coding agent
