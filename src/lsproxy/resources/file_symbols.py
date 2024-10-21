# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import file_symbol_list_params
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

__all__ = ["FileSymbolsResource", "AsyncFileSymbolsResource"]


class FileSymbolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileSymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return FileSymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileSymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return FileSymbolsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        file_path: str,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SymbolResponse:
        """
        Get symbols in a specific file

        Returns a list of symbols (functions, classes, variables, etc.) defined in the
        specified file.

        Args:
          file_path: The path to the file to get the symbols for, relative to the root of the
              workspace.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/file-symbols",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_path": file_path,
                        "include_raw_response": include_raw_response,
                    },
                    file_symbol_list_params.FileSymbolListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class AsyncFileSymbolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileSymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFileSymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileSymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return AsyncFileSymbolsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        file_path: str,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SymbolResponse:
        """
        Get symbols in a specific file

        Returns a list of symbols (functions, classes, variables, etc.) defined in the
        specified file.

        Args:
          file_path: The path to the file to get the symbols for, relative to the root of the
              workspace.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/file-symbols",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "file_path": file_path,
                        "include_raw_response": include_raw_response,
                    },
                    file_symbol_list_params.FileSymbolListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class FileSymbolsResourceWithRawResponse:
    def __init__(self, file_symbols: FileSymbolsResource) -> None:
        self._file_symbols = file_symbols

        self.list = to_raw_response_wrapper(
            file_symbols.list,
        )


class AsyncFileSymbolsResourceWithRawResponse:
    def __init__(self, file_symbols: AsyncFileSymbolsResource) -> None:
        self._file_symbols = file_symbols

        self.list = async_to_raw_response_wrapper(
            file_symbols.list,
        )


class FileSymbolsResourceWithStreamingResponse:
    def __init__(self, file_symbols: FileSymbolsResource) -> None:
        self._file_symbols = file_symbols

        self.list = to_streamed_response_wrapper(
            file_symbols.list,
        )


class AsyncFileSymbolsResourceWithStreamingResponse:
    def __init__(self, file_symbols: AsyncFileSymbolsResource) -> None:
        self._file_symbols = file_symbols

        self.list = async_to_streamed_response_wrapper(
            file_symbols.list,
        )
