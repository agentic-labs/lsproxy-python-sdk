# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PositionParam"]


class PositionParam(TypedDict, total=False):
    character: Required[int]
    """0-indexed character index."""

    line: Required[int]
    """0-indexed line number."""
