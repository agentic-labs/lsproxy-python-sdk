# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .position import Position
from ..._models import BaseModel

__all__ = ["Symbol"]


class Symbol(BaseModel):
    identifier_start_position: Position
    """Specific position within a file."""

    kind: str
    """The kind of the symbol (e.g., function, class)."""

    name: str
    """The name of the symbol."""

    source_code: Optional[object] = None
