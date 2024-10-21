# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.position import Position

__all__ = ["SymbolFindReferencesParams"]


class SymbolFindReferencesParams(TypedDict, total=False):
    symbol_identifier_position: Required[Position]
    """Specific position within a file."""

    include_code_context_context_lines: Optional[int]
    """
    Whether to include the source code of the symbol in the response. Defaults to
    false.
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
