# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.file_position import FilePosition

__all__ = ["DefinitionGetParams"]


class DefinitionGetParams(TypedDict, total=False):
    position: Required[FilePosition]
    """The position within the file to get the definition for.

    This should point to the identifier of the symbol you want to get the definition
    for.

    e.g. for getting the definition of `User` on line 10 of `src/main.py` with the
    code:

    ```
    0: class User:
    1:     def __init__(self, name, age):
    2:         self.name = name
    3:         self.age = age
    4:
    5: user = User("John", 30)
    __________^^^
    ```

    The (line, char) should be anywhere in (5, 7)-(5, 11).
    """

    include_raw_response: bool
    """
    Whether to include the raw response from the langserver in the response.
    Defaults to false.
    """
