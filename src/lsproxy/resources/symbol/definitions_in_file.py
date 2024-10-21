# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.symbol import definitions_in_file_list_params
from ...types.symbol_response import SymbolResponse

__all__ = ["DefinitionsInFileResource", "AsyncDefinitionsInFileResource"]


class DefinitionsInFileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefinitionsInFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return DefinitionsInFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefinitionsInFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return DefinitionsInFileResourceWithStreamingResponse(self)

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
            "/symbol/definitions-in-file",
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
                    definitions_in_file_list_params.DefinitionsInFileListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class AsyncDefinitionsInFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefinitionsInFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefinitionsInFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefinitionsInFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return AsyncDefinitionsInFileResourceWithStreamingResponse(self)

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
            "/symbol/definitions-in-file",
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
                    definitions_in_file_list_params.DefinitionsInFileListParams,
                ),
            ),
            cast_to=SymbolResponse,
        )


class DefinitionsInFileResourceWithRawResponse:
    def __init__(self, definitions_in_file: DefinitionsInFileResource) -> None:
        self._definitions_in_file = definitions_in_file

        self.list = to_raw_response_wrapper(
            definitions_in_file.list,
        )


class AsyncDefinitionsInFileResourceWithRawResponse:
    def __init__(self, definitions_in_file: AsyncDefinitionsInFileResource) -> None:
        self._definitions_in_file = definitions_in_file

        self.list = async_to_raw_response_wrapper(
            definitions_in_file.list,
        )


class DefinitionsInFileResourceWithStreamingResponse:
    def __init__(self, definitions_in_file: DefinitionsInFileResource) -> None:
        self._definitions_in_file = definitions_in_file

        self.list = to_streamed_response_wrapper(
            definitions_in_file.list,
        )


class AsyncDefinitionsInFileResourceWithStreamingResponse:
    def __init__(self, definitions_in_file: AsyncDefinitionsInFileResource) -> None:
        self._definitions_in_file = definitions_in_file

        self.list = async_to_streamed_response_wrapper(
            definitions_in_file.list,
        )
