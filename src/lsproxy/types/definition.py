# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Definition"]


class Definition(BaseModel):
    definitions: List[Definition]
    """
    The definition(s) of the symbol. Points to the start position of the symbol's
    identifier.

    e.g. for the definition of `User` on line 5 of `src/main.py` with the code:

    ```
    0: class User:
    _________^
    1:     def __init__(self, name, age):
    2:         self.name = name
    3:         self.age = age
    4:
    5: user = User("John", 30)
    __________^
    ```

    The definition(s) will be
    `[{"path": "src/main.py", "line": 0, "character": 6}]`.
    """

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
    """
