# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["FilePosition"]


class FilePosition(BaseModel):
    character: int

    line: int

    path: str
