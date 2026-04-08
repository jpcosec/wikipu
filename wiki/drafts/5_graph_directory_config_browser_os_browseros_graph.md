---
identity:
  node_id: "doc:wiki/drafts/5_graph_directory_config_browser_os_browseros_graph.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

BrowserOS stores OpenBrowser agent scripts here as TypeScript files. Each subdirectory is a script ID.

## Details

BrowserOS stores OpenBrowser agent scripts here as TypeScript files. Each subdirectory is a script ID.

```
graph/
  code_l3aod1jcXf6w/
    graph.ts    ← the agent TypeScript script
```

### What `graph.ts` looks like

The TypeScript script uses the OpenBrowser SDK `Agent` API:

```typescript
export async function run(agent: Agent) {
  await agent.nav("https://www.xing.com/jobs/...");

  const state = await agent.extract("Is the apply modal open?", {
    schema: z.object({ isOpen: z.boolean() })
  });

  await agent.act("Fill the Vorname field with the user's first name", {
    context: { firstName: "Juan Pablo" },
    maxSteps: 5
  });

  const result = await agent.verify("The application was submitted successfully.");
  return { success: result.success };
}
```

### OpenBrowser Agent API (full)

| Method | Signature | What it does |
|--------|-----------|-------------|
| `agent.nav(url)` | `(url: string) => Promise<void>` | Navigate to URL |
| `agent.extract(prompt, {schema})` | Zod schema → structured data | LLM extracts structured info from current page |
| `agent.act(prompt, {context?, maxSteps?})` | Natural language → actions | LLM performs actions on page (multi-step) |
| `agent.verify(prompt)` | `=> {success, reason}` | LLM verifies a condition is true |

**`agent.act` with context:** Variables in `context` are interpolated into the prompt with `{{varName}}` syntax. This is how profile data gets passed to the agent without embedding it in the prompt string.

**This means we can write agent scripts and drop them in `graph/` for BrowserOS to execute.** The graph directory is the integration point for Level 2 execution from our pipeline.

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.