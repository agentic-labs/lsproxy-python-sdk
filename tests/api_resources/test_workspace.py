# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import WorkspaceListFilesResponse
from lsproxy.types.shared import SymbolResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_files(self, client: Lsproxy) -> None:
        workspace = client.workspace.list_files()
        assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_list_files(self, client: Lsproxy) -> None:
        response = client.workspace.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_list_files(self, client: Lsproxy) -> None:
        with client.workspace.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_symbols(self, client: Lsproxy) -> None:
        workspace = client.workspace.search_symbols(
            query="query",
        )
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    def test_method_search_symbols_with_all_params(self, client: Lsproxy) -> None:
        workspace = client.workspace.search_symbols(
            query="query",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_search_symbols(self, client: Lsproxy) -> None:
        response = client.workspace.with_raw_response.search_symbols(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_search_symbols(self, client: Lsproxy) -> None:
        with client.workspace.with_streaming_response.search_symbols(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(SymbolResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspace:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_files(self, async_client: AsyncLsproxy) -> None:
        workspace = await async_client.workspace.list_files()
        assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.workspace.with_raw_response.list_files()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncLsproxy) -> None:
        async with async_client.workspace.with_streaming_response.list_files() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListFilesResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_symbols(self, async_client: AsyncLsproxy) -> None:
        workspace = await async_client.workspace.search_symbols(
            query="query",
        )
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    async def test_method_search_symbols_with_all_params(self, async_client: AsyncLsproxy) -> None:
        workspace = await async_client.workspace.search_symbols(
            query="query",
            include_raw_response=True,
        )
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_search_symbols(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.workspace.with_raw_response.search_symbols(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(SymbolResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_search_symbols(self, async_client: AsyncLsproxy) -> None:
        async with async_client.workspace.with_streaming_response.search_symbols(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(SymbolResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True
