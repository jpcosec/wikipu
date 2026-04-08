---
identity:
  node_id: "doc:wiki/drafts/steps_03b_03f_rich_content_renderers.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

Each follows the same template. Key details:

## Details

Each follows the same template. Key details:

### 03b — Markdown Formatted Editor
- Split source/preview, no WYSIWYG. Markdown is source of truth.
- Anchors reference source offsets. Debounced commit.
- Libraries: decision matrix (Lexical vs Tiptap vs CodeMirror markdown mode) + rendering lib (marked or remark+rehype).

### 03c — JSON/YAML Views
- Stored as parsed object, not raw string. Collapsible tree inspector (focus), validated text edit (edit).
- JSON↔YAML toggle is display-only. Key-path anchors.
- Libraries: decision matrix (@uiw/react-json-view vs react-inspector) + CodeMirror for edit mode.

### 03d — Table Editor
- Typed columns, inline cell editing, add/remove row/column. No spreadsheet parity.
- Cell coordinate anchors. Structured object storage.
- Libraries: TanStack Table (recommended) vs AG Grid.

### 03e — Code Display & Annotation
- Syntax highlighting, line-range anchors with gutter markers. Optional editing + explicit format-on-save.
- Libraries: CodeMirror 6 (recommended) vs Monaco. No LSP.

### 03f — Image Annotation
- Rectangle regions with normalized coordinates (0-1). Images as external asset references.
- Libraries: decision matrix (Annotorious vs react-image-annotate).

### html_safe — Sanitized HTML Rendering
- Renders sanitized HTML within nodes. Used for embedded HTML snippets from external sources.
- **Sanitization strategy:** DOMPurify with restrictive tag allowlist (no `<script>`, `<iframe>`, `<object>`, `<embed>`, `<form>`). Allowed tags: semantic HTML (`<h1>`–`<h6>`, `<p>`, `<ul>`, `<ol>`, `<li>`, `<table>`, `<tr>`, `<td>`, `<th>`, `<span>`, `<div>`, `<a>`, `<img>`, `<code>`, `<pre>`, `<blockquote>`). Attributes stripped except `class`, `id`, `href`, `src`, `alt`.
- **CSP:** Inline styles stripped. All styling via CSS classes that the theme can target.
- **Fallback:** If sanitization removes >50% of input HTML, show a warning with "View raw source" option.
- No anchoring support (HTML structure too variable). Read-only display mode only.
- Libraries: DOMPurify (committed — standard, well-maintained).

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.