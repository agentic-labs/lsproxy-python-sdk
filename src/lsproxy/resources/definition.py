# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import definition_get_params
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
from ..types.definition_response import DefinitionResponse
from ..types.shared_params.file_position import FilePosition

__all__ = ["DefinitionResource", "AsyncDefinitionResource"]


class DefinitionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefinitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return DefinitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefinitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return DefinitionResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        position: FilePosition,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefinitionResponse:
        """
        Get the definition of a symbol at a specific position in a file

        Returns the location of the definition for the symbol at the given position.

        Args:
          position: The position within the file to get the definition for. This should point to the
              identifier of the symbol you want to get the definition for.

              e.g. for getting the definition of `User` on line 10 of `src/main.py` with the
              code:

              ```
              0: class User:
              1:     def __init__(self, name, age):
              2:         self.name = name
              3:         self.age = age
              4:
              5: user = User("John", 30)
              __________^^^
              ```

              The (line, char) should be anywhere in (5, 7)-(5, 11).

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/definition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "position": position,
                        "include_raw_response": include_raw_response,
                    },
                    definition_get_params.DefinitionGetParams,
                ),
            ),
            cast_to=DefinitionResponse,
        )


class AsyncDefinitionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefinitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefinitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefinitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return AsyncDefinitionResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        position: FilePosition,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefinitionResponse:
        """
        Get the definition of a symbol at a specific position in a file

        Returns the location of the definition for the symbol at the given position.

        Args:
          position: The position within the file to get the definition for. This should point to the
              identifier of the symbol you want to get the definition for.

              e.g. for getting the definition of `User` on line 10 of `src/main.py` with the
              code:

              ```
              0: class User:
              1:     def __init__(self, name, age):
              2:         self.name = name
              3:         self.age = age
              4:
              5: user = User("John", 30)
              __________^^^
              ```

              The (line, char) should be anywhere in (5, 7)-(5, 11).

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/definition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "position": position,
                        "include_raw_response": include_raw_response,
                    },
                    definition_get_params.DefinitionGetParams,
                ),
            ),
            cast_to=DefinitionResponse,
        )


class DefinitionResourceWithRawResponse:
    def __init__(self, definition: DefinitionResource) -> None:
        self._definition = definition

        self.get = to_raw_response_wrapper(
            definition.get,
        )


class AsyncDefinitionResourceWithRawResponse:
    def __init__(self, definition: AsyncDefinitionResource) -> None:
        self._definition = definition

        self.get = async_to_raw_response_wrapper(
            definition.get,
        )


class DefinitionResourceWithStreamingResponse:
    def __init__(self, definition: DefinitionResource) -> None:
        self._definition = definition

        self.get = to_streamed_response_wrapper(
            definition.get,
        )


class AsyncDefinitionResourceWithStreamingResponse:
    def __init__(self, definition: AsyncDefinitionResource) -> None:
        self._definition = definition

        self.get = async_to_streamed_response_wrapper(
            definition.get,
        )
