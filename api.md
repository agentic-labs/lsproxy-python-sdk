# Shared Types

```python
from lsproxy.types import FilePosition, SymbolResponse
```

# Definition

Types:

```python
from lsproxy.types import DefinitionResponse
```

Methods:

- <code title="get /definition">client.definition.<a href="./src/lsproxy/resources/definition.py">get</a>(\*\*<a href="src/lsproxy/types/definition_get_params.py">params</a>) -> <a href="./src/lsproxy/types/definition_response.py">DefinitionResponse</a></code>

# FileSymbols

Methods:

- <code title="get /file-symbols">client.file_symbols.<a href="./src/lsproxy/resources/file_symbols.py">list</a>(\*\*<a href="src/lsproxy/types/file_symbol_list_params.py">params</a>) -> <a href="./src/lsproxy/types/symbol_response.py">SymbolResponse</a></code>

# References

Types:

```python
from lsproxy.types import ReferenceResponse
```

Methods:

- <code title="get /references">client.references.<a href="./src/lsproxy/resources/references.py">list</a>(\*\*<a href="src/lsproxy/types/reference_list_params.py">params</a>) -> <a href="./src/lsproxy/types/reference_response.py">ReferenceResponse</a></code>

# WorkspaceFiles

Types:

```python
from lsproxy.types import WorkspaceFileListResponse
```

Methods:

- <code title="get /workspace-files">client.workspace_files.<a href="./src/lsproxy/resources/workspace_files.py">list</a>() -> <a href="./src/lsproxy/types/workspace_file_list_response.py">WorkspaceFileListResponse</a></code>

# WorkspaceSymbols

Types:

```python
from lsproxy.types import SymbolResponse
```

Methods:

- <code title="get /workspace-symbols">client.workspace_symbols.<a href="./src/lsproxy/resources/workspace_symbols.py">list</a>(\*\*<a href="src/lsproxy/types/workspace_symbol_list_params.py">params</a>) -> <a href="./src/lsproxy/types/symbol_response.py">SymbolResponse</a></code>
