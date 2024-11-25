# lsproxy SDK

A Python SDK for interacting with the [lsproxy](https://github.com/agentic-labs/lsproxy) container, providing language-server protocol functionality for code analysis across multiple languages.

## Features

- Symbol definition lookup
- Reference lookup across files
- Support for analyzing Python, TypeScript/JavaScript, and Rust
- Pydantic models for type safety

## Try it out!
If you just want to get a feel for `lsproxy` try out the tutorial at [demo.lsproxy.dev](https://demo.lsproxy.dev)

## Installation

```bash
pip install lsproxy-sdk
```

## Usage

1. Start the LSProxy container:
```bash
docker run --rm -d -p 4444:4444 -v "/path/to/your/code:/mnt/workspace" --name lsproxy agenticlabs/lsproxy:0.1.0a1
```

2. Use the SDK:
```python
from lsproxy import Lsproxy

lsp = Lsproxy()
```

## List all files in the workspace
```python
lsp.list_files()
```

## Get symbols in a file
```python
lsp.definitions_in_file(path="path/to/file.py")
```

## Get references to a symbol
```python
# Find all references to a symbol at a specific position
references = lsp.find_references(
    GetReferencesRequest(
        identifier_position=FilePosition(
            file_path="path/to/file.py",
            line=10,
            character=15
        ),
        include_code_context_lines=2,  # Show 2 lines of context around each reference
        include_declaration=True       # Include the original declaration
    )
)

# Print found references
for ref in references.references:
    print(f"Reference in {ref.file_path} at line {ref.range.start.line}")
    if ref.code_context:
        print(ref.code_context)
```



