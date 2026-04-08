---
identity:
  node_id: "doc:wiki/drafts/6_humaninteracttool_the_formal_hitl_api.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

Built into the OpenBrowser agent framework. When the agent needs human input, it calls this tool. The `callback` registered with the agent handles it.

## Details

Built into the OpenBrowser agent framework. When the agent needs human input, it calls this tool. The `callback` registered with the agent handles it.

```typescript
// interactType options:
"confirm"      // "Are you sure you want to submit?" → boolean
"input"        // "Enter your salary expectation" → string
"select"       // "Choose your German level" + options → string[]
"request_help" // "Login required" or "CAPTCHA" → boolean (solved?)
```

```typescript
// helpType for request_help:
"request_login"       // Portal requires authentication
"request_assistance"  // Anything else (CAPTCHA, unknown form, etc.)
```

**Login check:** Before surfacing `request_login` to the human, the tool takes a screenshot and asks the LLM "is this page logged in?" If yes, it skips the interruption. This is built-in.

**For our pipeline:** We implement the `callback` interface in Python (via the `/chat` endpoint or by writing a TypeScript wrapper) to route `request_help` and `input` calls to our HITL channel (terminal → Textual TUI).

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.