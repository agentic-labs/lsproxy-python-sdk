# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import (
    DefinitionResponse,
    ReferencesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSymbol:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_find_definition(self, client: Lsproxy) -> None:
        symbol = client.symbol.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    def test_method_find_definition_with_all_params(self, client: Lsproxy) -> None:
        symbol = client.symbol.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
            include_raw_response=False,
            include_source_code=False,
        )
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    def test_raw_response_find_definition(self, client: Lsproxy) -> None:
        response = client.symbol.with_raw_response.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        symbol = response.parse()
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    def test_streaming_response_find_definition(self, client: Lsproxy) -> None:
        with client.symbol.with_streaming_response.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            symbol = response.parse()
            assert_matches_type(DefinitionResponse, symbol, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_references(self, client: Lsproxy) -> None:
        symbol = client.symbol.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    def test_method_find_references_with_all_params(self, client: Lsproxy) -> None:
        symbol = client.symbol.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
            include_code_context_lines=5,
            include_declaration=True,
            include_raw_response=False,
        )
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    def test_raw_response_find_references(self, client: Lsproxy) -> None:
        response = client.symbol.with_raw_response.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        symbol = response.parse()
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    def test_streaming_response_find_references(self, client: Lsproxy) -> None:
        with client.symbol.with_streaming_response.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            symbol = response.parse()
            assert_matches_type(ReferencesResponse, symbol, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSymbol:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_find_definition(self, async_client: AsyncLsproxy) -> None:
        symbol = await async_client.symbol.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    async def test_method_find_definition_with_all_params(self, async_client: AsyncLsproxy) -> None:
        symbol = await async_client.symbol.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
            include_raw_response=False,
            include_source_code=False,
        )
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    async def test_raw_response_find_definition(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.symbol.with_raw_response.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        symbol = await response.parse()
        assert_matches_type(DefinitionResponse, symbol, path=["response"])

    @parametrize
    async def test_streaming_response_find_definition(self, async_client: AsyncLsproxy) -> None:
        async with async_client.symbol.with_streaming_response.find_definition(
            position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            symbol = await response.parse()
            assert_matches_type(DefinitionResponse, symbol, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_references(self, async_client: AsyncLsproxy) -> None:
        symbol = await async_client.symbol.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    async def test_method_find_references_with_all_params(self, async_client: AsyncLsproxy) -> None:
        symbol = await async_client.symbol.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
            include_code_context_lines=5,
            include_declaration=True,
            include_raw_response=False,
        )
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    async def test_raw_response_find_references(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.symbol.with_raw_response.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        symbol = await response.parse()
        assert_matches_type(ReferencesResponse, symbol, path=["response"])

    @parametrize
    async def test_streaming_response_find_references(self, async_client: AsyncLsproxy) -> None:
        async with async_client.symbol.with_streaming_response.find_references(
            symbol_identifier_position={
                "path": "src/main.py",
                "position": {
                    "character": 5,
                    "line": 10,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            symbol = await response.parse()
            assert_matches_type(ReferencesResponse, symbol, path=["response"])

        assert cast(Any, response.is_closed) is True
