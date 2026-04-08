---
identity:
  node_id: "doc:wiki/drafts/1_mcp_server_port_9200.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

The main automation interface. Accepts JSON-RPC `tools/call` directly — **no LLM required**.

## Details

The main automation interface. Accepts JSON-RPC `tools/call` directly — **no LLM required**.

### Handshake (required once per session)

```python
import requests

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",  # MANDATORY — 500 without this
    "MCP-Protocol-Version": "2025-06-18",              # use this, not 2024-11-05
}
BASE_URL = "http://127.0.0.1:9200/mcp"

def mcp(method, params, call_id=1):
    payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": call_id}
    r = requests.post(BASE_URL, headers=HEADERS, json=payload)
    return r.json()

# Initialize (do this once — get Mcp-Session-Id back)
resp = requests.post(BASE_URL, headers=HEADERS, json={
    "jsonrpc": "2.0", "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {"tools": {"listChanged": True}, "sampling": {}},
        "clientInfo": {"name": "postulator", "version": "1.0"}
    },
    "id": 1
})
session_id = resp.headers.get("Mcp-Session-Id")
# Add to HEADERS for subsequent calls: HEADERS["Mcp-Session-Id"] = session_id
```

**Important:** The `Mcp-Session-Id` response header enables session continuity — add it to all subsequent calls to maintain browser context.

### Security flag

```json
"allow_remote_in_mcp": false
```

Only localhost connections are accepted. Remote MCP access is blocked at the server level.

### Available tools (60 total)

**Observation**
```
take_snapshot          — interactive elements with text + IDs (session-scoped IDs)
take_enhanced_snapshot — richer snapshot with more element metadata
get_dom                — full DOM HTML
search_dom             — query DOM by selector/text
get_page_content       — plain text content of page
get_page_links         — all links on page
get_console_logs       — browser console output
take_screenshot        — PNG screenshot as base64
```

**Navigation**
```
navigate_page          — load URL in current or new page
new_page               — open new tab
new_hidden_page        — open hidden tab (no focus change)
list_pages             — list all open tabs with URL + pageId
get_active_page        — get current focused tab
show_page              — bring tab to foreground
move_page              — reorder tabs
close_page             — close tab
```

**Interaction**
```
click                  — click by element ID or CSS selector
click_at               — click by absolute coordinates (x, y)
fill                   — set input value (WARNING: fails on React controlled inputs — see below)
check / uncheck        — checkbox state
select_option          — dropdown selection
upload_file            — file upload (handles OS file picker)
press_key              — keyboard key press
focus                  — focus element
clear                  — clear input field
hover / hover_at       — mouse hover
type_at                — type at coordinates
drag / drag_at         — drag and drop
scroll                 — scroll page
handle_dialog          — respond to browser dialogs (alert, confirm, prompt)
```

**Scripting**
```
evaluate_script        — execute JavaScript in page context (expression param, not script)
```

**Utilities**
```
save_pdf               — save page as PDF
save_screenshot        — save screenshot to file path
download_file          — download file from URL
browseros_info         — BrowserOS version and status
```

### Critical behaviors

**Snapshot IDs are session-scoped.** Element IDs (`[512] link "Apply"`) are stable within a page load but change on any navigation or reload. Always use `element_text` for replay, never numeric IDs.

**React controlled inputs.** `fill` sets the DOM value but does not trigger React's `onChange` — the form state stays unchanged. Use `evaluate_script` with the React native value setter:

```python
script = """
const el = document.querySelector('{selector}');
const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
setter.call(el, '{value}');
el.dispatchEvent(new Event('input', {{ bubbles: true }}));
"""
mcp("tools/call", {"name": "evaluate_script", "arguments": {"expression": script, "page": page_id}})
```

Confirmed required on: XING salary field, XING date spinbuttons, any React/Vue SPA.

**Date spinbuttons.** `<input type="number" role="spinbutton">` (used by XING for start date). Standard `fill` and `press_key` both fail. Only the React native setter via `evaluate_script` works reliably.

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.