# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.position import Position

__all__ = ["ReferencesResponse", "Context", "ContextRange", "ContextRangeEnd", "ContextRangeStart"]


class ContextRangeEnd(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class ContextRangeStart(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class ContextRange(BaseModel):
    end: ContextRangeEnd

    path: str
    """The path to the file."""

    start: ContextRangeStart


class Context(BaseModel):
    range: ContextRange

    source_code: str


class ReferencesResponse(BaseModel):
    references: List[Position]

    context: Optional[List[Context]] = None
    """The source code around the references."""

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
    """
