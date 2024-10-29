from typing import List, Set, Tuple
from pydantic import BaseModel
from lsproxy import (
    Lsproxy,
    CodeContext,
    FilePosition,
    GetReferencesRequest,
    GetDefinitionRequest,
)
import logging


def number_source_code(code_context: CodeContext) -> str:
    lines = code_context.source_code.splitlines()
    start_line = code_context.range.start.line
    numbered = "\n".join(f"{i + start_line}| {line}" for i, line in enumerate(lines))
    return f"```\n{numbered}\n```"


def to_prompt(code_context: CodeContext) -> str:
    return f"## {code_context.range.path}\n\n{number_source_code(code_context)}\n\n"


class HierarchyItem(BaseModel):
    name: str
    kind: str
    defined_at: FilePosition
    source_code_context: CodeContext

    def __hash__(self) -> int:
        return hash(
            (
                self.defined_at.path,
                self.defined_at.position.line,
                self.defined_at.position.character,
            )
        )

    def __repr__(self) -> str:
        filename = self.defined_at.path.rsplit("/", 1)[-1]
        return f"{filename}:{self.defined_at.position.line}#{self.name}"


def get_symbols_containing_positions(
    client: Lsproxy, target_positions: List[FilePosition], workspace_files: List[str]
) -> List[HierarchyItem]:
    assert all(
        pos.path == target_positions[0].path for pos in target_positions
    ), "All positions must be in the same file"
    file_path = target_positions[0].path
    if file_path not in workspace_files:
        logging.error(f"File {file_path} not found in workspace")
        return []

    symbols = client.definitions_in_file(file_path)
    symbols_containing_position = {
        HierarchyItem(
            name=symbol.name,
            kind=symbol.kind,
            defined_at=symbol.identifier_position,
            source_code_context=client.find_definition(
                GetDefinitionRequest(
                    position=symbol.identifier_position, include_source_code=True
                )
            ).source_code_context.pop(),
        )
        for symbol in symbols
        for target_position in target_positions
        if symbol.range.contains(target_position)
    }
    return symbols_containing_position


def get_hierarchy_incoming(
    client: Lsproxy, starting_positions: List[FilePosition]
) -> Tuple[Set[HierarchyItem], Set[Tuple[HierarchyItem, HierarchyItem]]]:
    """
    Compute the chain of code symbols that use the code at the starting positions.
    """
    nodes: Set[HierarchyItem] = set()
    edges: Set[Tuple[HierarchyItem, HierarchyItem]] = set()
    workspace_files = client.list_files()
    # Initialize with symbols that contain the starting positions
    stack = get_symbols_containing_positions(client, starting_positions, workspace_files)

    while stack:
        symbol = stack.pop()
        if symbol in nodes:
            continue
        nodes.add(symbol)

        # Find all references to this symbol across codebase
        references = client.find_references(
            GetReferencesRequest(
                start_position=symbol.defined_at, include_declaration=False
            )
        ).references

        references_by_file = {}
        for ref in references:
            references_by_file.setdefault(ref.path, []).append(ref)

        # Find symbols that contain the references, we will process these next
        related_symbols = [
            sym
            for refs in references_by_file.values()
            for sym in get_symbols_containing_positions(client, refs, workspace_files)
        ]

        for related_symbol in related_symbols:
            edges.add((symbol, related_symbol))
            stack.append(related_symbol)

    return nodes, edges
