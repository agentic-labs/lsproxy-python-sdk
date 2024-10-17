# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import workspace_search_symbols_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.symbol_response import SymbolResponse
from ..types.workspace_list_files_response import WorkspaceListFilesResponse

__all__ = ["WorkspaceResource", "AsyncWorkspaceResource"]


class WorkspaceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkspaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return WorkspaceResourceWithStreamingResponse(self)

    def list_files(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListFilesResponse:
        """
        Get a list of all files in the workspace

        Returns an array of file paths for all files in the current workspace.

        This is a convenience endpoint that does not use the underlying Language Servers
        directly, but it does apply the same filtering.
        """
        return self._get(
            "/workspace-files",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListFilesResponse,
        )

    def search_symbols(
        self,
        *,
        query: str,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SymbolResponse:
        """
        Search for symbols across the entire workspace

        Returns a list of symbols matching the given query string from all files in the
        workspace.

        The returned positions point to the start of the symbol's identifier.

        e.g. for `User` on line 0 of `src/main.py`:

        ```
        0: class User:
        _________^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        ```

        Args:
          query: The query to search for.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/workspace-symbols",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "include_raw_response": include_raw_response,
                    },
                    workspace_search_symbols_params.WorkspaceSearchSymbolsParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class AsyncWorkspaceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return AsyncWorkspaceResourceWithStreamingResponse(self)

    async def list_files(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceListFilesResponse:
        """
        Get a list of all files in the workspace

        Returns an array of file paths for all files in the current workspace.

        This is a convenience endpoint that does not use the underlying Language Servers
        directly, but it does apply the same filtering.
        """
        return await self._get(
            "/workspace-files",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceListFilesResponse,
        )

    async def search_symbols(
        self,
        *,
        query: str,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SymbolResponse:
        """
        Search for symbols across the entire workspace

        Returns a list of symbols matching the given query string from all files in the
        workspace.

        The returned positions point to the start of the symbol's identifier.

        e.g. for `User` on line 0 of `src/main.py`:

        ```
        0: class User:
        _________^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        ```

        Args:
          query: The query to search for.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/workspace-symbols",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "include_raw_response": include_raw_response,
                    },
                    workspace_search_symbols_params.WorkspaceSearchSymbolsParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class WorkspaceResourceWithRawResponse:
    def __init__(self, workspace: WorkspaceResource) -> None:
        self._workspace = workspace

        self.list_files = to_raw_response_wrapper(
            workspace.list_files,
        )
        self.search_symbols = to_raw_response_wrapper(
            workspace.search_symbols,
        )


class AsyncWorkspaceResourceWithRawResponse:
    def __init__(self, workspace: AsyncWorkspaceResource) -> None:
        self._workspace = workspace

        self.list_files = async_to_raw_response_wrapper(
            workspace.list_files,
        )
        self.search_symbols = async_to_raw_response_wrapper(
            workspace.search_symbols,
        )


class WorkspaceResourceWithStreamingResponse:
    def __init__(self, workspace: WorkspaceResource) -> None:
        self._workspace = workspace

        self.list_files = to_streamed_response_wrapper(
            workspace.list_files,
        )
        self.search_symbols = to_streamed_response_wrapper(
            workspace.search_symbols,
        )


class AsyncWorkspaceResourceWithStreamingResponse:
    def __init__(self, workspace: AsyncWorkspaceResource) -> None:
        self._workspace = workspace

        self.list_files = async_to_streamed_response_wrapper(
            workspace.list_files,
        )
        self.search_symbols = async_to_streamed_response_wrapper(
            workspace.search_symbols,
        )
