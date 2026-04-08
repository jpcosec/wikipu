---
identity:
  node_id: "doc:wiki/drafts/4_abc_applyadapter_smart_adapter_py.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

Adapters provide **only** portal-specific knowledge. All flow control lives in the base class.

## Details

Adapters provide **only** portal-specific knowledge. All flow control lives in the base class.

Portal-specific interaction sequences are expressed as **C4A-Script** — crawl4ai's human-readable DSL for web automation (`CLICK`, `SET`, `WAIT`, `IF/THEN`, `REPEAT`). This keeps each adapter file readable and maintainable without generating JS strings. File upload (`set_input_files`) remains the one exception handled via a Playwright hook, as C4A-Script has no file upload primitive.

```python
class PortalStructureChangedError(Exception):
    """Raised when a mandatory selector is absent from the live DOM."""


class ApplyAdapter(ABC):
    def __init__(self, data_manager: DataManager | None = None): ...

    @property
    @abstractmethod
    def source_name(self) -> str: ...

    @abstractmethod
    def get_form_selectors(self) -> FormSelectors:
        """Mandatory and optional selectors. Validated against the DOM before execution."""

    @abstractmethod
    def get_open_modal_script(self) -> str:
        """C4A-Script that only clicks the apply button and waits for the modal container.
        No field interaction — just opens the form so selectors become queryable.

        Must be idempotent: if the modal is already open (e.g. on a retry with persistent
        session), the script must not click again or break. Use IF/THEN to check first.

        Example:
            IF NOT `[data-testid="apply-modal"]` THEN
              CLICK `[data-testid="apply-button"]`
              WAIT `[data-testid="apply-modal"]` 5
            END
        """

    @abstractmethod
    def get_fill_form_script(self, profile: dict) -> str:
        """C4A-Script for filling text fields and dropdowns. Runs after _validate_selectors.

        Profile values are injected by the base class via _render_script(template, profile),
        which escapes all values through json.dumps() before interpolation to handle
        special characters (apostrophes, quotes, etc.) safely.

        File upload steps are omitted — handled by the before_retrieve_html hook
        in the same arun() call that executes this script.

        Example (XING Easy Apply):
            SET `input[name="firstName"]` "{{first_name}}"
            SET `input[name="lastName"]` "{{last_name}}"
            SET `input[type="email"]` "{{email}}"
            IF `select[name="salutation"]` THEN
              SET `select[name="salutation"]` "{{salutation}}"
            END
        """

    @abstractmethod
    def get_submit_script(self) -> str:
        """C4A-Script for the submit action — separated so dry-run can stop before it."""

    @abstractmethod
    def get_success_text(self) -> str:
        """Text fragment expected in the confirmation state (second validation layer)."""

    @abstractmethod
    def get_session_profile_dir(self) -> Path:
        """Path to the persistent browser profile for this portal."""

    # All logic below lives in the base class:
    async def run(self, job_id, cv_path, letter_path, dry_run) -> ApplyMeta: ...
    async def _validate_selectors(self, result, selectors) -> None: ...
    async def _validate_success_text(self, result) -> bool: ...
```

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.