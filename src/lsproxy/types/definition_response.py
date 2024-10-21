# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .code_context import CodeContext
from .file_position import FilePosition

__all__ = ["DefinitionResponse"]


class DefinitionResponse(BaseModel):
    definitions: List[FilePosition]

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
    """

    source_code_context: Optional[List[CodeContext]] = None
    """The source code of symbol definitions."""
