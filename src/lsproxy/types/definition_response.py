# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.position import Position

__all__ = ["DefinitionResponse"]


class DefinitionResponse(BaseModel):
    definitions: List[Position]

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
    """
