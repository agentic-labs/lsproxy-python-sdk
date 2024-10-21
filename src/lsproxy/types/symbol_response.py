# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.file_position import FilePosition

__all__ = ["SymbolResponse", "Symbol"]


class Symbol(BaseModel):
    identifier_start_position: FilePosition
    """Specific position within a file."""

    kind: str
    """The kind of the symbol (e.g., function, class)."""

    name: str
    """The name of the symbol."""


class SymbolResponse(BaseModel):
    symbols: List[Symbol]

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#document_symbol
    """
