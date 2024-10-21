# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .position import Position

__all__ = ["FileRange"]


class FileRange(BaseModel):
    end: Position

    path: str
    """The path to the file."""

    start: Position
