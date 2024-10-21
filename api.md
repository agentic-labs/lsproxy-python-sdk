# Symbol

Types:

- <code><a href="./src/resources/symbol/symbol.ts">CodeContext</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">DefinitionResponse</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">FilePostion</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">FileRange</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">Position</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">ReferencesResponse</a></code>
- <code><a href="./src/resources/symbol/symbol.ts">SymbolResponse</a></code>

Methods:

- <code title="post /symbol/find-definition">client.symbol.<a href="./src/resources/symbol/symbol.ts">findDefinition</a>({ ...params }) -> DefinitionResponse</code>
- <code title="post /symbol/find-references">client.symbol.<a href="./src/resources/symbol/symbol.ts">findReferences</a>({ ...params }) -> ReferencesResponse</code>

## DefinitionsInFile

Methods:

- <code title="get /symbol/definitions-in-file">client.symbol.definitionsInFile.<a href="./src/resources/symbol/definitions-in-file.ts">list</a>({ ...params }) -> SymbolResponse</code>

# Workspace

## Files

Types:

- <code><a href="./src/resources/workspace/files.ts">FileListResponse</a></code>

Methods:

- <code title="get /workspace/list-files">client.workspace.files.<a href="./src/resources/workspace/files.ts">list</a>() -> FileListResponse</code>
