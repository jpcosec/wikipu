---
identity:
  node_id: "doc:wiki/drafts/9_mcp_proxy_architecture_gap_4_recording_level_2.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

When the OpenBrowser LLM agent runs, it calls BrowserOS tools via `SimpleHttpMcpClient` pointing at `http://127.0.0.1:9200/mcp`. From the source code, `httpUrl` is a constructor parameter — **it is configurable**.

## Details

When the OpenBrowser LLM agent runs, it calls BrowserOS tools via `SimpleHttpMcpClient` pointing at `http://127.0.0.1:9200/mcp`. From the source code, `httpUrl` is a constructor parameter — **it is configurable**.

A transparent proxy between OpenBrowser and BrowserOS gives us the full tool call log for free:

```
OpenBrowser agent
    │  tools/call {"name": "click", "arguments": {"element": 512}}
    ▼
[Postulator MCP Proxy :9201]
    │  log call + correlate element ID with last snapshot → playbook step
    │  forward unchanged
    ▼
BrowserOS MCP :9200
    │  response
    ▼
[Proxy]
    │  log response
    ▼
OpenBrowser agent
```

### Python proxy skeleton

```python
from fastapi import FastAPI, Request
import httpx, asyncio

app = FastAPI()
BROWSEROS_URL = "http://127.0.0.1:9200/mcp"
last_snapshot: dict = {}  # updated on every take_snapshot call
playbook_steps: list = []

@app.post("/mcp")
async def proxy_mcp(request: Request):
    body = await request.json()
    method = body.get("method")
    params = body.get("params", {})

    # Intercept and record tool calls
    if method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        _record_step(tool_name, args)

    # Forward to BrowserOS
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            BROWSEROS_URL,
            json=body,
            headers=dict(request.headers),
        )
        result = resp.json()

    # Capture snapshots for element ID correlation
    if method == "tools/call" and params.get("name") == "take_snapshot":
        last_snapshot["elements"] = _parse_snapshot(result)

    return result

def _record_step(tool_name: str, args: dict):
    """Normalize tool call to a playbook step."""
    step = {"action": tool_name, "args": args}

    # Resolve numeric element IDs to text
    element_id = args.get("element")
    if element_id and last_snapshot.get("elements"):
        text = last_snapshot["elements"].get(int(element_id), {}).get("text")
        if text:
            step["args"] = {**args, "element_text": text}
            del step["args"]["element"]

    # Replace known profile values with {{variables}}
    step = _substitute_variables(step)
    playbook_steps.append(step)
```

### If OpenBrowser MCP URL is not configurable at runtime

Use `iptables` to transparently intercept without modifying OpenBrowser:

```bash
# Redirect all local traffic to 9200 → our proxy at 9201
sudo iptables -t nat -A OUTPUT -p tcp --dport 9200 -m owner ! --uid-owner proxy_uid -j REDIRECT --to-port 9201
# Our proxy runs on 9201 and forwards to 9200 using a direct socket (bypasses iptables)
```

Or simpler with `socat` for testing:
```bash
socat TCP-LISTEN:9201,fork,reuseaddr TCP:127.0.0.1:9200
```

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.