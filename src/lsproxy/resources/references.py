# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import reference_list_params
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
from ..types.reference_response import ReferenceResponse
from ..types.shared_params.file_position import FilePosition

__all__ = ["ReferencesResource", "AsyncReferencesResource"]


class ReferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return ReferencesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        symbol_identifier_position: FilePosition,
        include_declaration: bool | NotGiven = NOT_GIVEN,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferenceResponse:
        """
        Find all references to a symbol

        Returns a list of locations where the symbol at the given position is
        referenced.

        Args:
          symbol_identifier_position: The position within the file to get the references for. This should point to the
              identifier of the definition.

              e.g. for getting the references of `User` on line 0 of `src/main.py` with the
              code:

              ```
              0: class User:
              _________^^^^
              1:     def __init__(self, name, age):
              2:         self.name = name
              3:         self.age = age
              4:
              5: user = User("John", 30)
              ```

          include_declaration: Whether to include the declaration (definition) of the symbol in the response.
              Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbol_identifier_position": symbol_identifier_position,
                        "include_declaration": include_declaration,
                        "include_raw_response": include_raw_response,
                    },
                    reference_list_params.ReferenceListParams,
                ),
            ),
            cast_to=ReferenceResponse,
        )


class AsyncReferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return AsyncReferencesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        symbol_identifier_position: FilePosition,
        include_declaration: bool | NotGiven = NOT_GIVEN,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferenceResponse:
        """
        Find all references to a symbol

        Returns a list of locations where the symbol at the given position is
        referenced.

        Args:
          symbol_identifier_position: The position within the file to get the references for. This should point to the
              identifier of the definition.

              e.g. for getting the references of `User` on line 0 of `src/main.py` with the
              code:

              ```
              0: class User:
              _________^^^^
              1:     def __init__(self, name, age):
              2:         self.name = name
              3:         self.age = age
              4:
              5: user = User("John", 30)
              ```

          include_declaration: Whether to include the declaration (definition) of the symbol in the response.
              Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbol_identifier_position": symbol_identifier_position,
                        "include_declaration": include_declaration,
                        "include_raw_response": include_raw_response,
                    },
                    reference_list_params.ReferenceListParams,
                ),
            ),
            cast_to=ReferenceResponse,
        )


class ReferencesResourceWithRawResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.list = to_raw_response_wrapper(
            references.list,
        )


class AsyncReferencesResourceWithRawResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.list = async_to_raw_response_wrapper(
            references.list,
        )


class ReferencesResourceWithStreamingResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.list = to_streamed_response_wrapper(
            references.list,
        )


class AsyncReferencesResourceWithStreamingResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.list = async_to_streamed_response_wrapper(
            references.list,
        )
