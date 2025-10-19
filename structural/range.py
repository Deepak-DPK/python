"""Compatibility shim: old `range.py` re-exports `break_examples_from_range.py`.

This module intentionally imports only the non-interactive examples
to ensure safe imports without blocking on input().
"""

from .break_examples_from_range import *  # noqa: F401,F403
