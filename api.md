# Symbol

Types:

```python
from lsproxy.types import (
    CodeContext,
    DefinitionResponse,
    FilePostion,
    FileRange,
    Position,
    ReferencesResponse,
    SymbolResponse,
)
```

Methods:

- <code title="post /symbol/find-definition">client.symbol.<a href="./src/lsproxy/resources/symbol/symbol.py">find_definition</a>(\*\*<a href="src/lsproxy/types/symbol_find_definition_params.py">params</a>) -> <a href="./src/lsproxy/types/definition_response.py">DefinitionResponse</a></code>
- <code title="post /symbol/find-references">client.symbol.<a href="./src/lsproxy/resources/symbol/symbol.py">find_references</a>(\*\*<a href="src/lsproxy/types/symbol_find_references_params.py">params</a>) -> <a href="./src/lsproxy/types/references_response.py">ReferencesResponse</a></code>

## DefinitionsInFile

Methods:

- <code title="get /symbol/definitions-in-file">client.symbol.definitions_in_file.<a href="./src/lsproxy/resources/symbol/definitions_in_file.py">list</a>(\*\*<a href="src/lsproxy/types/symbol/definitions_in_file_list_params.py">params</a>) -> <a href="./src/lsproxy/types/symbol_response.py">SymbolResponse</a></code>

# Workspace

## Files

Types:

```python
from lsproxy.types.workspace import FileListResponse
```

Methods:

- <code title="get /workspace/list-files">client.workspace.files.<a href="./src/lsproxy/resources/workspace/files.py">list</a>() -> <a href="./src/lsproxy/types/workspace/file_list_response.py">FileListResponse</a></code>
