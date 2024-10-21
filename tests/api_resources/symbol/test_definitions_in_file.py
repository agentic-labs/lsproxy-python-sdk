# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import SymbolResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitionsInFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lsproxy) -> None:
        definitions_in_file = client.symbol.definitions_in_file.list(
            file_path="file_path",
        )
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lsproxy) -> None:
        definitions_in_file = client.symbol.definitions_in_file.list(
            file_path="file_path",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lsproxy) -> None:
        response = client.symbol.definitions_in_file.with_raw_response.list(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definitions_in_file = response.parse()
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lsproxy) -> None:
        with client.symbol.definitions_in_file.with_streaming_response.list(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definitions_in_file = response.parse()
            assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefinitionsInFile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLsproxy) -> None:
        definitions_in_file = await async_client.symbol.definitions_in_file.list(
            file_path="file_path",
        )
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLsproxy) -> None:
        definitions_in_file = await async_client.symbol.definitions_in_file.list(
            file_path="file_path",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.symbol.definitions_in_file.with_raw_response.list(
            file_path="file_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definitions_in_file = await response.parse()
        assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLsproxy) -> None:
        async with async_client.symbol.definitions_in_file.with_streaming_response.list(
            file_path="file_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definitions_in_file = await response.parse()
            assert_matches_type(SymbolResponse, definitions_in_file, path=["response"])

        assert cast(Any, response.is_closed) is True
