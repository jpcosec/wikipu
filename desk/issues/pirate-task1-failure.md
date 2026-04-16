---
issue_id: pirate-issue-001
status: resolved
created: 2026-04-16
task_ref: pirate-teaching
severity: critical
resolved: 2026-04-16
---

# Pirate Task 1 Failure - RESOLVED

## Symptom

Pirate (gemma4:e4b via Ollama) did not execute bash tool calls.

## Root Cause

**Two issues in `packages/ai/src/providers/openai-completions.ts`:**

1. **Ollama streaming format mismatch**: Ollama sends `message.tool_calls` directly, not `choices[0].delta.tool_calls`
2. **Missing thinking field**: Ollama uses `thinking` field for extended thinking, not in reasoningFields list

## Fix Applied

Added `parseChunk()` function to detect Ollama format and handle both:
- `message.tool_calls` (Ollama format)
- `choice.delta.tool_calls` (Standard OpenAI format)

Also added `"thinking"` to `reasoningFields` array to properly handle Ollama's extended thinking output.

## Files Changed

- `src/looting/pirate/packages/ai/src/providers/openai-completions.ts`

## Verification

```bash
pirate --provider ollama --model gemma4:e4b --no-session -p "Use the bash tool to run: echo test"
# Output: The command `echo test` was executed successfully.
```

## Related

- Task 1 in `wiki/concepts/pirate_curriculum.md`
- `wiki/system/pirate.md`
- Commit: `962b8794` in pirate repo
