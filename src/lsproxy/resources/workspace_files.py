# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.workspace_file_list_response import WorkspaceFileListResponse

__all__ = ["WorkspaceFilesResource", "AsyncWorkspaceFilesResource"]


class WorkspaceFilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspaceFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WorkspaceFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return WorkspaceFilesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceFileListResponse:
        """
        Get a list of all files in the workspace

        Returns an array of file paths for all files in the current workspace.

        This is a convenience endpoint that does not use the underlying Language Servers
        directly, but it does apply the same filtering.
        """
        return self._get(
            "/workspace-files",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceFileListResponse,
        )


class AsyncWorkspaceFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/agentic-labs/lsproxy-python-sdk#with_streaming_response
        """
        return AsyncWorkspaceFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceFileListResponse:
        """
        Get a list of all files in the workspace

        Returns an array of file paths for all files in the current workspace.

        This is a convenience endpoint that does not use the underlying Language Servers
        directly, but it does apply the same filtering.
        """
        return await self._get(
            "/workspace-files",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceFileListResponse,
        )


class WorkspaceFilesResourceWithRawResponse:
    def __init__(self, workspace_files: WorkspaceFilesResource) -> None:
        self._workspace_files = workspace_files

        self.list = to_raw_response_wrapper(
            workspace_files.list,
        )


class AsyncWorkspaceFilesResourceWithRawResponse:
    def __init__(self, workspace_files: AsyncWorkspaceFilesResource) -> None:
        self._workspace_files = workspace_files

        self.list = async_to_raw_response_wrapper(
            workspace_files.list,
        )


class WorkspaceFilesResourceWithStreamingResponse:
    def __init__(self, workspace_files: WorkspaceFilesResource) -> None:
        self._workspace_files = workspace_files

        self.list = to_streamed_response_wrapper(
            workspace_files.list,
        )


class AsyncWorkspaceFilesResourceWithStreamingResponse:
    def __init__(self, workspace_files: AsyncWorkspaceFilesResource) -> None:
        self._workspace_files = workspace_files

        self.list = async_to_streamed_response_wrapper(
            workspace_files.list,
        )
