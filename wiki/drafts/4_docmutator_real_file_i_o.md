---
identity:
  node_id: "doc:wiki/drafts/4_docmutator_real_file_i_o.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md", relation_type: "documents"}
---

### ⚠️ CRITICAL: This class WRITES to disk

## Details

### ⚠️ CRITICAL: This class WRITES to disk

Unlike ContextRouter (read-only), DocMutator modifies the filesystem. Use with caution.

```python
# src/tools/doc_mutator.py

import json
import shutil
from pathlib import Path
from typing import Optional, Dict
from context_router import ContextRouter

class DocMutator:
    """Tools for mutating documentation and code with REAL I/O."""
    
    def __init__(self, router: ContextRouter):
        self.router = router
        self.base_path = Path(".")
    
    def _write_file(self, path: str, content: str) -> bool:
        """Write content to file. Creates directories if needed."""
        try:
            file_path = self.base_path / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
            return True
        except Exception as e:
            print(f"ERROR writing {path}: {e}")
            return False
    
    def _delete_file(self, path: str) -> bool:
        """Delete a file. Does not fail if missing."""
        try:
            file_path = self.base_path / path
            file_path.unlink(missing_ok=True)
            return True
        except Exception as e:
            print(f"ERROR deleting {path}: {e}")
            return False
    
    def _acquire_lock(self, file_path: str) -> Optional[str]:
        """
        Acquire lock for race condition protection using ATOMIC exclusive create.
        Returns lock_path if acquired, None if already locked (atomic op prevents TOCTOU).
        """
        lock_path = f".{file_path}.lock"
        lock_file = self.base_path / lock_path
        try:
            # 'x' mode = exclusive create, fails if file exists (atomic)
            lock_file.open('x').close()
            return lock_path
        except FileExistsError:
            return None
    
    def _release_lock(self, lock_path: str) -> None:
        """Release lock atomically."""
        try:
            (self.base_path / lock_path).unlink(missing_ok=True)
        except Exception:
            pass

    # ─────────────────────────────────────────────────────────────
    # WORKFLOW A: Sync Code → Docs
    # ─────────────────────────────────────────────────────────────
    
    def sync_code_to_docs(
        self,
        domain: str,
        stage: str,
        generated_docs: Dict[str, str]
    ) -> str:
        """
        Sync documentation to reflect current code state.
        
        Args:
            domain: Technical domain
            stage: Pipeline stage
            generated_docs: Dict of {doc_path: content} to write
        """
        results = []
        
        for doc_path, content in generated_docs.items():
            # Acquire lock to prevent race conditions
            lock_path = self._acquire_lock(doc_path)
            if lock_path is None:
                results.append(f"SKIPPED (locked): {doc_path}")
                continue
            
            if self._write_file(doc_path, content):
                results.append(f"UPDATED: {doc_path}")
            else:
                results.append(f"FAILED: {doc_path}")
            
            self._release_lock(lock_path)
        
        return "\n".join(results)
    
    # ─────────────────────────────────────────────────────────────
    # WORKFLOW B: Implement Plan → Code → Docs
    # ─────────────────────────────────────────────────────────────
    
    def implement_plan(
        self,
        domain: str,
        stage: str,
        plan_doc: str,
        generated_code: Dict[str, str],
        generated_docs: Dict[str, str]
    ) -> str:
        """
        Implement a plan: write code, update docs, delete plan.
        
        Args:
            domain: Technical domain
            stage: Pipeline stage
            plan_doc: Path to plan file to delete after implementation
            generated_code: Dict of {file_path: content}
            generated_docs: Dict of {doc_path: content}
        """
        results = []
        
        # 1. Write code files
        for file_path, content in generated_code.items():
            lock_path = self._acquire_lock(file_path)
            if lock_path is None:
                results.append(f"LOCKED (aborted): {file_path}")
                continue
            
            if self._write_file(file_path, content):
                results.append(f"CREATED/MODIFIED: {file_path}")
            else:
                results.append(f"FAILED: {file_path}")
            
            self._release_lock(lock_path)
        
        # 2. Write docs
        for doc_path, content in generated_docs.items():
            lock_path = self._acquire_lock(doc_path)
            if lock_path is None:
                results.append(f"LOCKED (skipped): {doc_path}")
                continue
            
            if self._write_file(doc_path, content):
                results.append(f"PROMOTED TO RUNTIME: {doc_path}")
            
            self._release_lock(lock_path)
        
        # 3. Delete plan (CRITICAL: prevents orphaned plans)
        if self._delete_file(plan_doc):
            results.append(f"ARCHIVED: {plan_doc}")
        else:
            results.append(f"WARNING: Could not delete {plan_doc}")
        
        return "\n".join(results)
    
    # ─────────────────────────────────────────────────────────────
    # WORKFLOW C: Draft Plan (Runtime → Plan)
    # ─────────────────────────────────────────────────────────────
    
    def draft_plan(
        self,
        domain: str,
        stage: str,
        plan_filename: str,
        plan_content: str
    ) -> str:
        """
        Create a new plan document.
        
        Args:
            domain: Technical domain
            stage: Pipeline stage
            plan_filename: Name of the plan file
            plan_content: Full plan content
        """
        plan_path = f"plan/{domain}/{plan_filename}"
        
        if self._write_file(plan_path, plan_content):
            return f"CREATED: {plan_path}"
        else:
            return f"FAILED: {plan_path}"
    
    # ─────────────────────────────────────────────────────────────
    # WORKFLOW D: Hotfix (Code → Code + Docs)
    # ─────────────────────────────────────────────────────────────
    
    def hotfix(
        self,
        domain: str,
        stage: str,
        fixed_code: Dict[str, str],
        updated_docs: Dict[str, str],
        skip_docs: bool = False
    ) -> str:
        """
        Apply a hotfix to code and optionally update docs.
        
        Args:
            domain: Technical domain
            stage: Pipeline stage
            fixed_code: Dict of {file_path: patched_content}
            updated_docs: Dict of {doc_path: updated_content}
            skip_docs: If True, skip doc update (creates 24h debt)
        """
        results = []
        
        # 1. Fix code
        for file_path, content in fixed_code.items():
            lock_path = self._acquire_lock(file_path)
            if lock_path is None:
                results.append(f"LOCKED (aborted): {file_path}")
                continue
            
            if self._write_file(file_path, content):
                results.append(f"FIXED: {file_path}")
            else:
                results.append(f"FAILED: {file_path}")
            
            self._release_lock(lock_path)
        
        # 2. Update docs (unless --skip-docs)
        if skip_docs:
            results.append("⚠️  DOCS SKIPPED (--skip-docs flag). Run sync within 24h!")
        else:
            for doc_path, content in updated_docs.items():
                lock_path = self._acquire_lock(doc_path)
                if lock_path is None:
                    results.append(f"LOCKED (skipped): {doc_path}")
                    continue
                
                if self._write_file(doc_path, content):
                    results.append(f"DOCS UPDATED: {doc_path}")
                
                self._release_lock(lock_path)
        
        return "\n".join(results)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md`.