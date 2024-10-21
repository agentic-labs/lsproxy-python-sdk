# Shared

Types:

- <code><a href="./src/resources/shared.ts">Position</a></code>
- <code><a href="./src/resources/shared.ts">Symbol</a></code>
- <code><a href="./src/resources/shared.ts">SymbolResponse</a></code>

# Symbols

Types:

- <code><a href="./src/resources/symbols.ts">DefinitionResponse</a></code>
- <code><a href="./src/resources/symbols.ts">DefinitionResponse</a></code>
- <code><a href="./src/resources/symbols.ts">ReferencesResponse</a></code>
- <code><a href="./src/resources/symbols.ts">ReferencesResponse</a></code>
- <code><a href="./src/resources/symbols.ts">SymbolResponse</a></code>

Methods:

- <code title="get /symbol/definitions-in-file">client.symbols.<a href="./src/resources/symbols.ts">definitionsInFile</a>({ ...params }) -> SymbolResponse</code>
- <code title="post /symbol/find-definition">client.symbols.<a href="./src/resources/symbols.ts">findDefinition</a>({ ...params }) -> DefinitionResponse</code>
- <code title="post /symbol/find-references">client.symbols.<a href="./src/resources/symbols.ts">findReferences</a>({ ...params }) -> ReferencesResponse</code>

# Workspace

Types:

- <code><a href="./src/resources/workspace.ts">WorkspaceListFilesResponse</a></code>

Methods:

- <code title="get /workspace/list-files">client.workspace.<a href="./src/resources/workspace.ts">listFiles</a>() -> WorkspaceListFilesResponse</code>
