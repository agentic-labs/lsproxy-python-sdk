# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceSearchSymbolsParams"]


class WorkspaceSearchSymbolsParams(TypedDict, total=False):
    query: Required[str]
    """The query to search for."""

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
