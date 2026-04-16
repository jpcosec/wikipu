---
issue_id: pirate-issue-001
status: open
created: 2026-04-16
task_ref: pirate-teaching
severity: critical
---

# Pirate Task 1 Failure - Tool Calling Broken

## Symptom

Pirate (gemma4:e4b via Ollama) does not execute bash tool calls. It generates plausible but fake output instead of calling tools.

## Expected Behavior

Pirate should use the `bash` tool to run commands like:
```bash
wiki-compiler query --type get_descendants --node-id 'doc:wiki/Index.md'
```

## Actual Behavior

Model responds with generated text describing what "knowledge graph systems" look like, without calling any tools.

## Root Cause

**Gemma4:e4b via Ollama's OpenAI compatibility layer does not properly support function/tool calling.**

Evidence:
- Model responds to simple prompts (e.g., "What is 2+2?")
- Model generates plausible but fake tool output (lists files that happen to exist)
- Model NEVER actually calls the bash tool
- Ollama uses `openai-completions` API which has limited function calling support

## Options

1. **Find a Gemma version with tool calling support** - Some Gemma variants support function calling
2. **Use a different model for Pirate** - One that properly supports tools (Claude, GPT, etc.)
3. **Configure Ollama differently** - Check if there's a way to enable tool calling
4. **Accept limitation** - Use Pirate for text-only tasks, not tool execution

## Testing Commands

```bash
# Test if model can use tools
pirate --provider ollama --model gemma4:e4b -p "Use bash to run: echo hello"

# Check Ollama API capabilities
curl http://localhost:11434/api/tags
```

## Related

- Task 1 in `wiki/concepts/pirate_curriculum.md`
- `wiki/system/pirate.md`
- Ollama gemma4 models: gemma4:latest, gemma4:26b, gemma4:e4b
