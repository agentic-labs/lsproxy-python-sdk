# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import ReferenceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lsproxy) -> None:
        reference = client.references.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lsproxy) -> None:
        reference = client.references.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
            include_declaration=True,
            include_raw_response=True,
        )
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lsproxy) -> None:
        response = client.references.with_raw_response.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lsproxy) -> None:
        with client.references.with_streaming_response.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(ReferenceResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLsproxy) -> None:
        reference = await async_client.references.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLsproxy) -> None:
        reference = await async_client.references.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
            include_declaration=True,
            include_raw_response=True,
        )
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.references.with_raw_response.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(ReferenceResponse, reference, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLsproxy) -> None:
        async with async_client.references.with_streaming_response.list(
            symbol_identifier_position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(ReferenceResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True
