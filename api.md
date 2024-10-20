# Shared Types

```python
from lsproxy.types import Position, Symbol, SymbolResponse
```

# Symbols

Types:

```python
from lsproxy.types import DefinitionResponse, ReferencesResponse
```

Methods:

- <code title="get /file-symbols">client.symbols.<a href="./src/lsproxy/resources/symbols.py">definitions_in_file</a>(\*\*<a href="src/lsproxy/types/symbol_definitions_in_file_params.py">params</a>) -> <a href="./src/lsproxy/types/shared/symbol_response.py">SymbolResponse</a></code>
- <code title="post /definition">client.symbols.<a href="./src/lsproxy/resources/symbols.py">find_definition</a>(\*\*<a href="src/lsproxy/types/symbol_find_definition_params.py">params</a>) -> <a href="./src/lsproxy/types/definition_response.py">DefinitionResponse</a></code>
- <code title="post /references">client.symbols.<a href="./src/lsproxy/resources/symbols.py">find_references</a>(\*\*<a href="src/lsproxy/types/symbol_find_references_params.py">params</a>) -> <a href="./src/lsproxy/types/references_response.py">ReferencesResponse</a></code>

# Workspace

Types:

```python
from lsproxy.types import WorkspaceListFilesResponse
```

Methods:

- <code title="get /workspace-files">client.workspace.<a href="./src/lsproxy/resources/workspace.py">list_files</a>() -> <a href="./src/lsproxy/types/workspace_list_files_response.py">WorkspaceListFilesResponse</a></code>
