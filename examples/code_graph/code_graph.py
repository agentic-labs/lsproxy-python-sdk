import requests
import json
import argparse
import sys
from typing import Dict, Any, Optional

from lsproxy import ApiClient, Configuration, SymbolApi
from lsproxy.models.file_position import FilePosition
from lsproxy.models.position import Position
from lsproxy.models.get_references_request import GetReferencesRequest
from lsproxy.rest import ApiException

def save_edge_data(data: Dict[str, set], output_file: str = 'edge_data.json'):
    graph_data = [{'from': edge[0], 'to': edge[1], 'referenced_symbols': list(referenced_symbols)} for edge, referenced_symbols in data.items()]
    with open(output_file, 'w') as f:
        json.dump(graph_data, f, indent=2)
    print(f"Dependency data saved to {output_file}")

def process_file(file_path: str):
    with ApiClient(Configuration()) as api_client:
        edges = {}
        symbols = SymbolApi(api_client).definitions_in_file(file_path).symbols or []

        for symbol in symbols:
            get_references_request = GetReferencesRequest(start_position=symbol.start_position)
            references = SymbolApi(api_client).find_references(get_references_request).references
            for reference in references:
                dest_file = reference.path
                if dest_file == file_path:
                    continue
                print(f"`{dest_file}` references `{symbol.name}` from `{file_path}`")
                edges.setdefault((file_path, dest_file), set()).add(symbol.name)

        save_edge_data(edges)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process file symbols and references using LSP Proxy API.")
    parser.add_argument("file_path", help="Path to the file to be processed")
    args = parser.parse_args()

    process_file(args.file_path)
