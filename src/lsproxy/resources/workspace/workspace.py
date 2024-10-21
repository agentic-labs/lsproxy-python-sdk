# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WorkspaceResource", "AsyncWorkspaceResource"]


class WorkspaceResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return WorkspaceResourceWithStreamingResponse(self)


class AsyncWorkspaceResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lsproxy-python#with_streaming_response
        """
        return AsyncWorkspaceResourceWithStreamingResponse(self)


class WorkspaceResourceWithRawResponse:
    def __init__(self, workspace: WorkspaceResource) -> None:
        self._workspace = workspace

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._workspace.files)


class AsyncWorkspaceResourceWithRawResponse:
    def __init__(self, workspace: AsyncWorkspaceResource) -> None:
        self._workspace = workspace

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._workspace.files)


class WorkspaceResourceWithStreamingResponse:
    def __init__(self, workspace: WorkspaceResource) -> None:
        self._workspace = workspace

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._workspace.files)


class AsyncWorkspaceResourceWithStreamingResponse:
    def __init__(self, workspace: AsyncWorkspaceResource) -> None:
        self._workspace = workspace

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._workspace.files)
