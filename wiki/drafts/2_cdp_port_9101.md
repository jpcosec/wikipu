---
identity:
  node_id: "doc:wiki/drafts/2_cdp_port_9101.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

Full Chrome DevTools Protocol access. This is our **recording interface**.

## Details

Full Chrome DevTools Protocol access. This is our **recording interface**.

```python
import asyncio, websockets, json

CDP_BASE = "http://127.0.0.1:9101"

async def get_targets():
    """List all debuggable pages."""
    import requests
    return requests.get(f"{CDP_BASE}/json").json()

async def cdp_session(target_id: str):
    ws_url = f"ws://127.0.0.1:9101/devtools/page/{target_id}"
    async with websockets.connect(ws_url) as ws:
        # Enable event domains
        await ws.send(json.dumps({"method": "Page.enable", "id": 1}))
        await ws.send(json.dumps({"method": "Runtime.enable", "id": 2}))
        await ws.send(json.dumps({"method": "Input.enable", "id": 3}))  # if available

        # Inject in-page event capture
        await ws.send(json.dumps({
            "method": "Runtime.evaluate",
            "params": {"expression": CAPTURE_SCRIPT},
            "id": 4
        }))

        async for msg in ws:
            event = json.loads(msg)
            yield event
```

### CDP capabilities for recording

| Domain | Event | What we get |
|--------|-------|-------------|
| `Page` | `frameNavigated` | URL changes, redirects |
| `Runtime` | `consoleAPICalled` | Our injected capture script output |
| `Network` | `requestWillBeSent` | Form submissions (POST requests) |
| `Input` | (if enabled) | Raw input events |

### In-page capture script

```javascript
(function() {
  if (window.__postulator_recorder) return;
  window.__postulator_recorder = true;

  const log = (type, data) =>
    console.log(JSON.stringify({__rec: true, type, ts: Date.now(), ...data}));

  document.addEventListener('click', e => log('click', {
    tag: e.target.tagName,
    text: (e.target.innerText || e.target.value || '').trim().slice(0, 100),
    x: e.clientX, y: e.clientY,
    name: e.target.name || e.target.id || null
  }), true);

  document.addEventListener('change', e => log('change', {
    tag: e.target.tagName, name: e.target.name,
    value: e.target.type === 'password' ? '{{REDACTED}}' : e.target.value,
    type: e.target.type
  }), true);

  document.addEventListener('submit', e => log('submit', {
    action: e.target.action, method: e.target.method
  }), true);
})();
```

Events arrive via `Runtime.consoleAPICalled` with `__rec: true` in the JSON. Filter and accumulate. On navigation (`Page.frameNavigated`), re-inject the script on the new page.

### Correlating CDP events → playbook steps

After capturing raw events, correlate with periodic snapshots:
1. Click at `(x, y)` → take snapshot → find element whose text matches what's visible at those coordinates
2. Change on `input[name="salary"]` → find element in snapshot with that name → `fill(element_text="Gehalt", value="{{salary_expectation}}")`
3. Submit → `click(element_text="Jetzt bewerben")`

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.