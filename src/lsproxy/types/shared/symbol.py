# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Symbol"]


class Symbol(BaseModel):
    symbols: List[Symbol]

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#document_symbol
    """