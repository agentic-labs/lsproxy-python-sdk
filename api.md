# Shared Types

```python
from lsproxy.types import Symbol
```

# Definitions

Types:

```python
from lsproxy.types import Definition
```

Methods:

- <code title="get /definition">client.definitions.<a href="./src/lsproxy/resources/definitions.py">retrieve</a>(\*\*<a href="src/lsproxy/types/definition_retrieve_params.py">params</a>) -> <a href="./src/lsproxy/types/definition.py">Definition</a></code>

# FileSymbols

Methods:

- <code title="get /file-symbols">client.file_symbols.<a href="./src/lsproxy/resources/file_symbols.py">list</a>(\*\*<a href="src/lsproxy/types/file_symbol_list_params.py">params</a>) -> <a href="./src/lsproxy/types/shared/symbol.py">Symbol</a></code>

# References

Types:

```python
from lsproxy.types import Reference
```

Methods:

- <code title="get /references">client.references.<a href="./src/lsproxy/resources/references.py">list</a>(\*\*<a href="src/lsproxy/types/reference_list_params.py">params</a>) -> <a href="./src/lsproxy/types/reference.py">Reference</a></code>

# WorkspaceFiles

Types:

```python
from lsproxy.types import WorkspaceFileListResponse
```

Methods:

- <code title="get /workspace-files">client.workspace_files.<a href="./src/lsproxy/resources/workspace_files.py">list</a>() -> <a href="./src/lsproxy/types/workspace_file_list_response.py">WorkspaceFileListResponse</a></code>

# WorkspaceSymbols

Methods:

- <code title="get /workspace-symbols">client.workspace_symbols.<a href="./src/lsproxy/resources/workspace_symbols.py">list</a>(\*\*<a href="src/lsproxy/types/workspace_symbol_list_params.py">params</a>) -> <a href="./src/lsproxy/types/shared/symbol.py">Symbol</a></code>
