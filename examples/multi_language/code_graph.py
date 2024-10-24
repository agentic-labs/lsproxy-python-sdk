import marimo

__generated_with = "0.9.12"
app = marimo.App(width="medium")


@app.cell
def __(args):
    import requests
    import json
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

            return edges

    file_path = "backend/src/code_search/codebase_searcher/redis_codebase_searcher.py"
    process_file(args.file_path)

    return (
        Any,
        ApiClient,
        ApiException,
        Configuration,
        Dict,
        FilePosition,
        GetReferencesRequest,
        Optional,
        Position,
        SymbolApi,
        file_path,
        json,
        process_file,
        requests,
        save_edge_data,
        sys,
    )


if __name__ == "__main__":
    app.run()
