# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.position import Position

__all__ = [
    "DefinitionResponse",
    "SourceCodeContext",
    "SourceCodeContextRange",
    "SourceCodeContextRangeEnd",
    "SourceCodeContextRangeStart",
]


class SourceCodeContextRangeEnd(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class SourceCodeContextRangeStart(BaseModel):
    character: int
    """0-indexed character index."""

    line: int
    """0-indexed line number."""


class SourceCodeContextRange(BaseModel):
    end: SourceCodeContextRangeEnd

    path: str
    """The path to the file."""

    start: SourceCodeContextRangeStart


class SourceCodeContext(BaseModel):
    range: SourceCodeContextRange

    source_code: str


class DefinitionResponse(BaseModel):
    definitions: List[Position]

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
    """

    source_code_context: Optional[List[SourceCodeContext]] = None
    """The source code of symbol definitions."""
