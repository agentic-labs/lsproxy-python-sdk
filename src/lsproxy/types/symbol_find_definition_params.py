# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .file_position_param import FilePositionParam

__all__ = ["SymbolFindDefinitionParams"]


class SymbolFindDefinitionParams(TypedDict, total=False):
    position: Required[FilePositionParam]
    """Specific position within a file."""

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """

    include_source_code: bool
    """
    Whether to include the source code around the symbol's identifier in the
    response. Defaults to false.
    """
