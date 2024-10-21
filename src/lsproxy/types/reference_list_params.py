# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.file_position import FilePosition

__all__ = ["ReferenceListParams"]


class ReferenceListParams(TypedDict, total=False):
    symbol_identifier_position: Required[FilePosition]
    """The position within the file to get the references for.

    This should point to the identifier of the definition.

    e.g. for getting the references of `User` on line 0 of `src/main.py` with the
    code:

    ```
    0: class User:
    _________^^^^
    1:     def __init__(self, name, age):
    2:         self.name = name
    3:         self.age = age
    4:
    5: user = User("John", 30)
    ```
    """

    include_declaration: bool
    """
    Whether to include the declaration (definition) of the symbol in the response.
    Defaults to false.
    """

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
