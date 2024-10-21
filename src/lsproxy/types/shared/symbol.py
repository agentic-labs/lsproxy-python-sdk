# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .position import Position
from ..._models import BaseModel

__all__ = ["Symbol", "SourceCode", "SourceCodeRange", "SourceCodeRangeEnd", "SourceCodeRangeStart"]


class SourceCodeRangeEnd(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class SourceCodeRangeStart(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class SourceCodeRange(BaseModel):
    end: SourceCodeRangeEnd

    path: str
    """The path to the file."""

    start: SourceCodeRangeStart


class SourceCode(BaseModel):
    range: SourceCodeRange

    source_code: str


class Symbol(BaseModel):
    identifier_start_position: Position
    """Specific position within a file."""

    kind: str
    """The kind of the symbol (e.g., function, class)."""

    name: str
    """The name of the symbol."""

    source_code: Optional[SourceCode] = None
