# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.file_position import FilePosition

__all__ = ["ReferenceResponse"]


class ReferenceResponse(BaseModel):
    references: List[FilePosition]
    """
    The references to the symbol. Points to the start position of the symbol's
    identifier.

    e.g. for the references of `User` on line 0 character 6 of `src/main.py` with
    the code:

    ```
    0: class User:
    _________^
    1:     def __init__(self, name, age):
    2:         self.name = name
    3:         self.age = age
    4:
    5: user = User("John", 30)
    _________^
    6:
    7: print(user.name)
    ```

    The references will be `[{"path": "src/main.py", "line": 5, "character": 7}]`.
    """

    raw_response: Optional[object] = None
    """The raw response from the langserver.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
    """
