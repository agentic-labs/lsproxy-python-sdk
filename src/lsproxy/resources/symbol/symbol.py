# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import symbol_find_definition_params, symbol_find_references_params
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
from .definitions_in_file import (
    DefinitionsInFileResource,
    AsyncDefinitionsInFileResource,
    DefinitionsInFileResourceWithRawResponse,
    AsyncDefinitionsInFileResourceWithRawResponse,
    DefinitionsInFileResourceWithStreamingResponse,
    AsyncDefinitionsInFileResourceWithStreamingResponse,
)
from ...types.file_postion_param import FilePostionParam
from ...types.definition_response import DefinitionResponse
from ...types.references_response import ReferencesResponse

__all__ = ["SymbolResource", "AsyncSymbolResource"]


class SymbolResource(SyncAPIResource):
    @cached_property
    def definitions_in_file(self) -> DefinitionsInFileResource:
        return DefinitionsInFileResource(self._client)

    @cached_property
    def with_raw_response(self) -> SymbolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return SymbolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SymbolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return SymbolResourceWithStreamingResponse(self)

    def find_definition(
        self,
        *,
        position: FilePostionParam,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        include_source_code: bool | NotGiven = NOT_GIVEN,
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

        The input position should point inside the symbol's identifier, e.g.

        The returned position points to the identifier of the symbol, and the file_path
        from workspace root

        e.g. for the definition of `User` on line 5 of `src/main.py` with the code:

        ```
        0: class User:
        output___^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        4:
        5: user = User("John", 30)
        input_____^^^^
        ```

        Args:
          position: Specific position within a file.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          include_source_code: Whether to include the source code around the symbol's identifier in the
              response. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/symbol/find-definition",
            body=maybe_transform(
                {
                    "position": position,
                    "include_raw_response": include_raw_response,
                    "include_source_code": include_source_code,
                },
                symbol_find_definition_params.SymbolFindDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefinitionResponse,
        )

    def find_references(
        self,
        *,
        symbol_identifier_position: FilePostionParam,
        include_code_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
        include_declaration: bool | NotGiven = NOT_GIVEN,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferencesResponse:
        """
        Find all references to a symbol

        The input position should point to the identifier of the symbol you want to get
        the references for.

        Returns a list of locations where the symbol at the given position is
        referenced.

        The returned positions point to the start of the reference identifier.

        e.g. for `User` on line 0 of `src/main.py`:

        ```
        0: class User:
        input____^^^^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        4:
        5: user = User("John", 30)
        output____^
        ```

        Args:
          symbol_identifier_position: Specific position within a file.

          include_code_context_lines: Whether to include the source code of the symbol in the response. Defaults to
              none.

          include_declaration: Whether to include the declaration (definition) of the symbol in the response.
              Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/symbol/find-references",
            body=maybe_transform(
                {
                    "symbol_identifier_position": symbol_identifier_position,
                    "include_code_context_lines": include_code_context_lines,
                    "include_declaration": include_declaration,
                    "include_raw_response": include_raw_response,
                },
                symbol_find_references_params.SymbolFindReferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferencesResponse,
        )


class AsyncSymbolResource(AsyncAPIResource):
    @cached_property
    def definitions_in_file(self) -> AsyncDefinitionsInFileResource:
        return AsyncDefinitionsInFileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSymbolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSymbolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSymbolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return AsyncSymbolResourceWithStreamingResponse(self)

    async def find_definition(
        self,
        *,
        position: FilePostionParam,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        include_source_code: bool | NotGiven = NOT_GIVEN,
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

        The input position should point inside the symbol's identifier, e.g.

        The returned position points to the identifier of the symbol, and the file_path
        from workspace root

        e.g. for the definition of `User` on line 5 of `src/main.py` with the code:

        ```
        0: class User:
        output___^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        4:
        5: user = User("John", 30)
        input_____^^^^
        ```

        Args:
          position: Specific position within a file.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          include_source_code: Whether to include the source code around the symbol's identifier in the
              response. Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/symbol/find-definition",
            body=await async_maybe_transform(
                {
                    "position": position,
                    "include_raw_response": include_raw_response,
                    "include_source_code": include_source_code,
                },
                symbol_find_definition_params.SymbolFindDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DefinitionResponse,
        )

    async def find_references(
        self,
        *,
        symbol_identifier_position: FilePostionParam,
        include_code_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
        include_declaration: bool | NotGiven = NOT_GIVEN,
        include_raw_response: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReferencesResponse:
        """
        Find all references to a symbol

        The input position should point to the identifier of the symbol you want to get
        the references for.

        Returns a list of locations where the symbol at the given position is
        referenced.

        The returned positions point to the start of the reference identifier.

        e.g. for `User` on line 0 of `src/main.py`:

        ```
        0: class User:
        input____^^^^
        1:     def __init__(self, name, age):
        2:         self.name = name
        3:         self.age = age
        4:
        5: user = User("John", 30)
        output____^
        ```

        Args:
          symbol_identifier_position: Specific position within a file.

          include_code_context_lines: Whether to include the source code of the symbol in the response. Defaults to
              none.

          include_declaration: Whether to include the declaration (definition) of the symbol in the response.
              Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/symbol/find-references",
            body=await async_maybe_transform(
                {
                    "symbol_identifier_position": symbol_identifier_position,
                    "include_code_context_lines": include_code_context_lines,
                    "include_declaration": include_declaration,
                    "include_raw_response": include_raw_response,
                },
                symbol_find_references_params.SymbolFindReferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferencesResponse,
        )


class SymbolResourceWithRawResponse:
    def __init__(self, symbol: SymbolResource) -> None:
        self._symbol = symbol

        self.find_definition = to_raw_response_wrapper(
            symbol.find_definition,
        )
        self.find_references = to_raw_response_wrapper(
            symbol.find_references,
        )

    @cached_property
    def definitions_in_file(self) -> DefinitionsInFileResourceWithRawResponse:
        return DefinitionsInFileResourceWithRawResponse(self._symbol.definitions_in_file)


class AsyncSymbolResourceWithRawResponse:
    def __init__(self, symbol: AsyncSymbolResource) -> None:
        self._symbol = symbol

        self.find_definition = async_to_raw_response_wrapper(
            symbol.find_definition,
        )
        self.find_references = async_to_raw_response_wrapper(
            symbol.find_references,
        )

    @cached_property
    def definitions_in_file(self) -> AsyncDefinitionsInFileResourceWithRawResponse:
        return AsyncDefinitionsInFileResourceWithRawResponse(self._symbol.definitions_in_file)


class SymbolResourceWithStreamingResponse:
    def __init__(self, symbol: SymbolResource) -> None:
        self._symbol = symbol

        self.find_definition = to_streamed_response_wrapper(
            symbol.find_definition,
        )
        self.find_references = to_streamed_response_wrapper(
            symbol.find_references,
        )

    @cached_property
    def definitions_in_file(self) -> DefinitionsInFileResourceWithStreamingResponse:
        return DefinitionsInFileResourceWithStreamingResponse(self._symbol.definitions_in_file)


class AsyncSymbolResourceWithStreamingResponse:
    def __init__(self, symbol: AsyncSymbolResource) -> None:
        self._symbol = symbol

        self.find_definition = async_to_streamed_response_wrapper(
            symbol.find_definition,
        )
        self.find_references = async_to_streamed_response_wrapper(
            symbol.find_references,
        )

    @cached_property
    def definitions_in_file(self) -> AsyncDefinitionsInFileResourceWithStreamingResponse:
        return AsyncDefinitionsInFileResourceWithStreamingResponse(self._symbol.definitions_in_file)
