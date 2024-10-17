# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import workspace_symbol_list_params
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
from ..types.symbol_response import SymbolResponse

__all__ = ["WorkspaceSymbolsResource", "AsyncWorkspaceSymbolsResource"]


class WorkspaceSymbolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspaceSymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceSymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceSymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return WorkspaceSymbolsResourceWithStreamingResponse(self)

    def list(
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
                    workspace_symbol_list_params.WorkspaceSymbolListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class AsyncWorkspaceSymbolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceSymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceSymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceSymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return AsyncWorkspaceSymbolsResourceWithStreamingResponse(self)

    async def list(
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
                    workspace_symbol_list_params.WorkspaceSymbolListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class WorkspaceSymbolsResourceWithRawResponse:
    def __init__(self, workspace_symbols: WorkspaceSymbolsResource) -> None:
        self._workspace_symbols = workspace_symbols

        self.list = to_raw_response_wrapper(
            workspace_symbols.list,
        )


class AsyncWorkspaceSymbolsResourceWithRawResponse:
    def __init__(self, workspace_symbols: AsyncWorkspaceSymbolsResource) -> None:
        self._workspace_symbols = workspace_symbols

        self.list = async_to_raw_response_wrapper(
            workspace_symbols.list,
        )


class WorkspaceSymbolsResourceWithStreamingResponse:
    def __init__(self, workspace_symbols: WorkspaceSymbolsResource) -> None:
        self._workspace_symbols = workspace_symbols

        self.list = to_streamed_response_wrapper(
            workspace_symbols.list,
        )


class AsyncWorkspaceSymbolsResourceWithStreamingResponse:
    def __init__(self, workspace_symbols: AsyncWorkspaceSymbolsResource) -> None:
        self._workspace_symbols = workspace_symbols

        self.list = async_to_streamed_response_wrapper(
            workspace_symbols.list,
        )
