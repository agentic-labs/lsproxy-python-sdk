# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    symbol_find_definition_params,
    symbol_find_references_params,
    symbol_definitions_in_file_params,
)
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
from ..types.references_response import ReferencesResponse
from ..types.shared.symbol_response import SymbolResponse
from ..types.shared_params.position import Position

__all__ = ["SymbolsResource", "AsyncSymbolsResource"]


class SymbolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return SymbolsResourceWithStreamingResponse(self)

    def definitions_in_file(
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
                    symbol_definitions_in_file_params.SymbolDefinitionsInFileParams,
                ),
            ),
            cast_to=SymbolResponse,
        )

    def find_definition(
        self,
        *,
        position: Position,
        include_code_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
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

          include_code_context_lines: Whether to include the source code around the symbol's identifier in the
              response. Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/definition",
            body=maybe_transform(
                {
                    "position": position,
                    "include_code_context_lines": include_code_context_lines,
                    "include_raw_response": include_raw_response,
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
        symbol_identifier_position: Position,
        include_code_context_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
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

          include_code_context_context_lines: Whether to include the source code of the symbol in the response. Defaults to
              false.

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
            "/references",
            body=maybe_transform(
                {
                    "symbol_identifier_position": symbol_identifier_position,
                    "include_code_context_context_lines": include_code_context_context_lines,
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


class AsyncSymbolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSymbolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSymbolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSymbolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return AsyncSymbolsResourceWithStreamingResponse(self)

    async def definitions_in_file(
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
                    symbol_definitions_in_file_params.SymbolDefinitionsInFileParams,
                ),
            ),
            cast_to=SymbolResponse,
        )

    async def find_definition(
        self,
        *,
        position: Position,
        include_code_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
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

          include_code_context_lines: Whether to include the source code around the symbol's identifier in the
              response. Defaults to false.

          include_raw_response: Whether to include the raw response from the langserver in the response.
              Defaults to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/definition",
            body=await async_maybe_transform(
                {
                    "position": position,
                    "include_code_context_lines": include_code_context_lines,
                    "include_raw_response": include_raw_response,
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
        symbol_identifier_position: Position,
        include_code_context_context_lines: Optional[int] | NotGiven = NOT_GIVEN,
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

          include_code_context_context_lines: Whether to include the source code of the symbol in the response. Defaults to
              false.

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
            "/references",
            body=await async_maybe_transform(
                {
                    "symbol_identifier_position": symbol_identifier_position,
                    "include_code_context_context_lines": include_code_context_context_lines,
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


class SymbolsResourceWithRawResponse:
    def __init__(self, symbols: SymbolsResource) -> None:
        self._symbols = symbols

        self.definitions_in_file = to_raw_response_wrapper(
            symbols.definitions_in_file,
        )
        self.find_definition = to_raw_response_wrapper(
            symbols.find_definition,
        )
        self.find_references = to_raw_response_wrapper(
            symbols.find_references,
        )


class AsyncSymbolsResourceWithRawResponse:
    def __init__(self, symbols: AsyncSymbolsResource) -> None:
        self._symbols = symbols

        self.definitions_in_file = async_to_raw_response_wrapper(
            symbols.definitions_in_file,
        )
        self.find_definition = async_to_raw_response_wrapper(
            symbols.find_definition,
        )
        self.find_references = async_to_raw_response_wrapper(
            symbols.find_references,
        )


class SymbolsResourceWithStreamingResponse:
    def __init__(self, symbols: SymbolsResource) -> None:
        self._symbols = symbols

        self.definitions_in_file = to_streamed_response_wrapper(
            symbols.definitions_in_file,
        )
        self.find_definition = to_streamed_response_wrapper(
            symbols.find_definition,
        )
        self.find_references = to_streamed_response_wrapper(
            symbols.find_references,
        )


class AsyncSymbolsResourceWithStreamingResponse:
    def __init__(self, symbols: AsyncSymbolsResource) -> None:
        self._symbols = symbols

        self.definitions_in_file = async_to_streamed_response_wrapper(
            symbols.definitions_in_file,
        )
        self.find_definition = async_to_streamed_response_wrapper(
            symbols.find_definition,
        )
        self.find_references = async_to_streamed_response_wrapper(
            symbols.find_references,
        )
