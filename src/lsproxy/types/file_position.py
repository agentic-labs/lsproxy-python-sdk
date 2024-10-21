# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .position import Position

__all__ = ["FilePosition"]


class FilePosition(BaseModel):
    path: str

    position: Position
