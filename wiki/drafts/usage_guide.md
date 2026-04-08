---
identity:
  node_id: "doc:wiki/drafts/usage_guide.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md", relation_type: "documents"}
---

### What is this page?

## Details

### What is this page?

The Extract page is the first human gate in the pipeline. The LLM has already read the job posting and extracted a list of requirements (must-haves and nice-to-haves). Your job is to:

1. **Audit** the extracted list — is anything missing, duplicated, or wrong?
2. **Correct** requirements — edit text, change priority, delete obvious errors
3. **Add** anything the LLM missed — select the text in the source, tag it
4. **Commit** to advance to the Match stage

---

### Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Portfolio > tu_berlin > 999001     FLOW SCRAPE EXTRACT MATCH   │  ← job nav
├──────────────────────────┬───────────────────────┬──────────────┤
│                          │  EXTRACTED REQS (3)   │  PHASE       │
│  SOURCE TEXT             │  ┌─────────────────┐  │  EXTRACT     │
│                          │  │ R1 [MUST] Python │  │             │
│  # PhD Researcher ...    │  │ ─────────────── │  │  (selected  │
│  - Python (required) ██  │  │ R2 [MUST] Eng.. │  │   req JSON) │
│  - English C1 (req.) ██  │  │ R3 [NICE] Res.. │  │             │
│  - Research in AI ...    │  └─────────────────┘  │  SAVE DRAFT │
│                          │  [ + ADD ]             │  COMMIT→MATCH│
└──────────────────────────┴───────────────────────┴──────────────┘
```

**Left pane — Source Text:** The raw job posting (markdown). Line numbers on the left.
When you hover or select a requirement card, the relevant lines highlight in cyan.
*(After span porting: the exact text fragment highlights inline.)*

**Center pane — Extracted Reqs:** The LLM's requirement list. Each card shows:
- **ID** (R1, R2, …)
- **Priority badge** — `MUST` (amber) or `NICE` (muted) — click to change
- **Requirement text** — double-click to edit
- **Delete button** (×) — confirm before deleting MUST requirements

**Right panel — Control Panel:**
- When a requirement is selected: shows its full JSON (→ will become structured fields)
- Shortcut hints: `Ctrl+S` / `Ctrl+Enter`
- `SAVE DRAFT` — persist edits without committing
- `COMMIT → MATCH` — saves and navigates to the Match stage

---

### Step-by-step workflow

#### 1. Read the source text (left pane)
Scan the job posting. Mentally note any requirements the LLM may have missed.

#### 2. Review each requirement card (center pane)
- Hover a card → source text highlights the matching lines
- Is the priority right? `MUST` = truly required; `NICE` = desirable but not blocking
- Is the text accurate? Double-click to edit inline

#### 3. Delete a wrong requirement
Click the × button on any card. For `MUST` cards you'll get a confirm dialog.

#### 4. Add a missing requirement (two ways)

**Method A — Type it:**
Click `+ ADD` → a blank card appears at the bottom. Double-click the text to edit it. Set the priority.

**Method B — Select from source *(after span porting)*:**
Click and drag to select text in the left pane → press `1` (MUST) or `2` (NICE) → a new card appears with the selected text pre-filled and the source span recorded.

#### 5. Annotate a requirement *(after details porting)*
Click a card to expand it → add a note in the "Notes" field (e.g. "LLM paraphrased — original says 'proficiency in R or Python'").

#### 6. Save draft
`Ctrl+S` saves your current list. Use this to pause and return. The list will reload from the saved state on next visit.

#### 7. Commit to Match
When satisfied: `Ctrl+Enter` or **COMMIT → MATCH** button.
This saves and navigates to the Match page. The pipeline uses your final requirement list to run matching.

> ⚠ Note: Currently COMMIT → MATCH just navigates — it does not send a formal gate decision to the backend yet. A `useGateDecide` hook call will be added in a future iteration.

---

### Keyboard shortcuts

| Key | Action |
|---|---|
| `Ctrl+S` | Save draft |
| `Ctrl+Enter` | Save + navigate to Match |
| `1` | Tag selected source text as MUST *(after span porting)* |
| `2` | Tag selected source text as NICE *(after span porting)* |
| `Escape` | Clear text selection / deselect card |

---

### Empty and error states

| State | What the operator sees |
|---|---|
| Extract not yet run | `EXTRACT_DATA_NOT_FOUND` monospace error message |
| Loading | Spinner centered in page |
| No requirements extracted | "NO_REQUIREMENTS_EXTRACTED" + "+ Add Manual" button |
| Delete MUST requirement | Browser confirm dialog: `Delete MUST requirement "…"?` |
| Save failed | *(not yet shown — add error toast)* |

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/extract_text_tagger_merge.md`.