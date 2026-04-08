---
identity:
  node_id: "doc:wiki/drafts/4_sqlite_database_config_browser_os_browseros_browseros_db.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md", relation_type: "documents"}
---

```sql

## Details

```sql
-- Tables
identity       -- single row: browseros_id (install UUID)
rate_limiter   -- LLM provider rate limiting records
oauth_tokens   -- provider credentials (see below)
```

### `oauth_tokens` schema

```sql
CREATE TABLE oauth_tokens (
  browseros_id TEXT NOT NULL,
  provider TEXT NOT NULL,          -- "google", "github", etc.
  access_token TEXT NOT NULL,      -- LIVE ACCESS TOKEN — plaintext
  refresh_token TEXT NOT NULL,     -- LIVE REFRESH TOKEN — plaintext
  expires_at INTEGER NOT NULL,
  email TEXT,
  account_id TEXT,
  created_at TEXT,
  updated_at TEXT,
  PRIMARY KEY (browseros_id, provider)
);
```

**This is a significant interface.** OAuth access tokens for whatever accounts the user has connected to BrowserOS are stored here in plaintext. This is useful for:
- Reading the user's connected accounts and their email addresses
- Verifying which providers are authenticated without making any network calls
- Understanding session state before attempting portal navigation

**Security note:** Never write to this table, never log its contents, never include it in artifacts. Read-only use only, and only for session state verification.

```python
import sqlite3
DB = "/home/jp/.config/browser-os/.browseros/browseros.db"

def get_connected_providers():
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT provider, email, expires_at FROM oauth_tokens").fetchall()
    conn.close()
    return [{"provider": r[0], "email": r[1], "expires_at": r[2]} for r in rows]
```

---

Generated from `raw/docs_postulador_v2/docs/reference/external_libs/browseros_interfaces.md`.