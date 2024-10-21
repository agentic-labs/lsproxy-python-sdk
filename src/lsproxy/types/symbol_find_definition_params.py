# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.position import Position

__all__ = ["SymbolFindDefinitionParams"]


class SymbolFindDefinitionParams(TypedDict, total=False):
    position: Required[Position]
    """Specific position within a file."""

    include_code_context_lines: Optional[int]
    """
    Whether to include the source code around the symbol's identifier in the
    response. Defaults to false.
    """

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
