# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .file_position_param import FilePositionParam

__all__ = ["SymbolFindReferencesParams"]


class SymbolFindReferencesParams(TypedDict, total=False):
    symbol_identifier_position: Required[FilePositionParam]
    """Specific position within a file."""

    include_code_context_lines: Optional[int]
    """
    Whether to include the source code of the symbol in the response. Defaults to
    none.
    """

    include_declaration: bool
    """
    Whether to include the declaration (definition) of the symbol in the response.
    Defaults to false.
    """

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
