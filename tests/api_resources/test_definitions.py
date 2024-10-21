# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lsproxy import Lsproxy, AsyncLsproxy
from tests.utils import assert_matches_type
from lsproxy.types import Definition

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lsproxy) -> None:
        definition = client.definitions.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Lsproxy) -> None:
        definition = client.definitions.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
            include_raw_response=True,
        )
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lsproxy) -> None:
        response = client.definitions.with_raw_response.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lsproxy) -> None:
        with client.definitions.with_streaming_response.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(Definition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefinitions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLsproxy) -> None:
        definition = await async_client.definitions.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLsproxy) -> None:
        definition = await async_client.definitions.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
            include_raw_response=True,
        )
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLsproxy) -> None:
        response = await async_client.definitions.with_raw_response.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(Definition, definition, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLsproxy) -> None:
        async with async_client.definitions.with_streaming_response.retrieve(
            position={
                "character": 5,
                "line": 10,
                "path": "src/main.py",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(Definition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True