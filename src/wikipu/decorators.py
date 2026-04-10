"""
Decorators for exempting code from Wiki compliance checks.
Marks functions or classes to bypass strict House Rules validation.
"""
from functools import wraps
from typing import Any, Callable

def wiki_exempt(reason: str) -> Callable:
    """
    Marks a function or class as exempt from the House Rules.
    The wiki_compiler will read the AST, detect this decorator, and assign
    the 'exempt' status in the KnowledgeNode, recording the reason.
    
    Usage:
    @wiki_exempt(reason="Legacy library that does not support Pydantic")
    def my_old_function():
        ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)
        # Add a dunder attribute so other runtime scripts can also see it if needed
        wrapper.__wiki_exempt_reason__ = reason
        return wrapper
    return decorator