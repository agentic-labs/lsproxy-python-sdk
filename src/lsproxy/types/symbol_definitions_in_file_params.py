# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SymbolDefinitionsInFileParams"]


class SymbolDefinitionsInFileParams(TypedDict, total=False):
    file_path: Required[str]
    """
    The path to the file to get the symbols for, relative to the root of the
    workspace.
    """

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
