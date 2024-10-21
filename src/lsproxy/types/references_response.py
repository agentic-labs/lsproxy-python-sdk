# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .code_context import CodeContext
from .file_postion import FilePostion

__all__ = ["ReferencesResponse"]


class ReferencesResponse(BaseModel):
    references: List[FilePostion]

    context: Optional[List[CodeContext]] = None
    """The source code around the references."""

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
    """
