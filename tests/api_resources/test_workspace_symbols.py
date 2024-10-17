# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import SymbolResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaceSymbols:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lsproxy) -> None:
        workspace_symbol = client.workspace_symbols.list(
            query="query",
        )
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lsproxy) -> None:
        workspace_symbol = client.workspace_symbols.list(
            query="query",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lsproxy) -> None:
        response = client.workspace_symbols.with_raw_response.list(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_symbol = response.parse()
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lsproxy) -> None:
        with client.workspace_symbols.with_streaming_response.list(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_symbol = response.parse()
            assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspaceSymbols:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLsproxy) -> None:
        workspace_symbol = await async_client.workspace_symbols.list(
            query="query",
        )
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLsproxy) -> None:
        workspace_symbol = await async_client.workspace_symbols.list(
            query="query",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.workspace_symbols.with_raw_response.list(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_symbol = await response.parse()
        assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLsproxy) -> None:
        async with async_client.workspace_symbols.with_streaming_response.list(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_symbol = await response.parse()
            assert_matches_type(SymbolResponse, workspace_symbol, path=["response"])

        assert cast(Any, response.is_closed) is True
