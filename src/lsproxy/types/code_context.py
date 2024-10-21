# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .file_range import FileRange

__all__ = ["CodeContext"]


class CodeContext(BaseModel):
    range: FileRange

    source_code: str
