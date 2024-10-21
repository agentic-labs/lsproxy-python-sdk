# Symbols

Types:

```python
from lsproxy.types import (
    CodeContext,
    DefinitionResponse,
    FilePosition,
    FileRange,
    Position,
    ReferencesResponse,
    SymbolResponse,
)
```

Methods:

- <code title="get /symbol/definitions-in-file">client.symbols.<a href="./src/lsproxy/resources/symbols.py">definitions_in_file</a>(\*\*<a href="src/lsproxy/types/symbol_definitions_in_file_params.py">params</a>) -> <a href="./src/lsproxy/types/symbol_response.py">SymbolResponse</a></code>
- <code title="post /symbol/find-definition">client.symbols.<a href="./src/lsproxy/resources/symbols.py">find_definition</a>(\*\*<a href="src/lsproxy/types/symbol_find_definition_params.py">params</a>) -> <a href="./src/lsproxy/types/definition_response.py">DefinitionResponse</a></code>
- <code title="post /symbol/find-references">client.symbols.<a href="./src/lsproxy/resources/symbols.py">find_references</a>(\*\*<a href="src/lsproxy/types/symbol_find_references_params.py">params</a>) -> <a href="./src/lsproxy/types/references_response.py">ReferencesResponse</a></code>
