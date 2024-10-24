import marimo

__generated_with = "0.9.12"
app = marimo.App(width="medium")


@app.cell
def __(create_file_dropdown, mo):
    file_options, file_dict = create_file_dropdown()
    hops = mo.ui.number(1, 3)
    get_status, set_status = mo.state("Starting")
    return file_dict, file_options, get_status, hops, set_status


@app.cell
def __(file_options, hops, mo):
    submit_button = mo.ui.run_button(label="Click to submit", disabled=not file_options.value)
    files_unit = mo.vstack([mo.md("Available files"),file_options])
    hops_unit = mo.vstack([mo.md("Number of hops"), hops])
    selections = mo.hstack([files_unit, hops_unit], justify="center")
    mo.vstack([selections, submit_button], align="center")
    return files_unit, hops_unit, selections, submit_button


@app.cell
def __(
    create_mermaid_from_dependencies,
    file_options,
    hops,
    mo,
    process_file,
    submit_button,
):
    mo.stop(not submit_button.value, "Click `submit` to build the graph")
    edges = process_file(file_options.value, hops.value)
    mermaid_string = create_mermaid_from_dependencies(edges)
    mo.mermaid(mermaid_string)
    return edges, mermaid_string


@app.cell
def __(get_files, mo):
    def create_file_dropdown():
        file_dict = get_files()
        file_with_symbol_count = sorted([(file, len(symbols)) for file, symbols in file_dict.items()], key=lambda file_item: -file_item[1])
        filtered = filter(lambda x: x[1]<100 and x[1]>10, file_with_symbol_count)
        file_options = {f"{file}: ({symbols} symbols)": file for file, symbols in filtered}
        return mo.ui.dropdown(options=file_options), file_dict
    return (create_file_dropdown,)


@app.cell
def __(ApiClient, Configuration, SymbolApi, WorkspaceApi, mo):
    def get_files():
        file_dict = {}
        with ApiClient(Configuration()) as api_client:
            files = WorkspaceApi(api_client).list_files()
            for i in mo.status.progress_bar(range(len(files)), title="Files processed", remove_on_exit=True):
                file = files[i]
                if file.endswith(".rs"):
                    continue
                symbols = SymbolApi(api_client).definitions_in_file(file).symbols or []
                file_dict[file] = symbols
        return file_dict
    return (get_files,)


@app.cell
def __(
    ApiClient,
    Configuration,
    GetDefinitionRequest,
    GetReferencesRequest,
    SymbolApi,
    WorkspaceApi,
    mo,
):
    def process_file(file_path: str, hops: int = 1):
        with ApiClient(Configuration()) as api_client:
            edges = {}
            workspace_files = {file: True for file in WorkspaceApi(api_client).list_files()}
            current_files = [file_path]
            with mo.status.progress_bar(total=hops, title=f"On hop 1/{hops}", remove_on_exit=True) as hop_bar:
                for i in range(hops):
                    new_files = set()
                    if not current_files:
                        break
                    with mo.status.progress_bar(total=len(current_files), title=f"Processing file 1/{len(current_files)}: {current_files[0]}", remove_on_exit=True) as file_bar:
                        for j, file in enumerate(current_files):
                            symbols = SymbolApi(api_client).definitions_in_file(file, include_raw_response=True).symbols or []
                            for symbol_idx in mo.status.progress_bar(range(len(symbols)), remove_on_exit=True, title="Symbols Processed"):
                                symbol = symbols[symbol_idx]
                                if symbol.name.startswith("\"") and symbol.name.endswith("\""):
                                    print(f"{symbol.name}:{symbol.kind}")
                                    print("SKIPPY THE STRINGY")
                                    continue
                                get_definition_request = GetDefinitionRequest(position=symbol.start_position)
                                definitions = SymbolApi(api_client).find_definition(get_definition_request).definitions
                                #print(f"Symbol: {symbol.name}")
                                #for definition in definitions:
                                    #print(f"    {definition.path}:{definition.position.line}:{definition.position.character}")
                                get_references_request = GetReferencesRequest(start_position=symbol.start_position, include_declaration=True)
                                references = SymbolApi(api_client).find_references(get_references_request).references
                                skip = False
                                for reference in references:
                                    dest_file = reference.path
                                    if reference.path not in workspace_files:
                                        print(f"FUCK YOU: {symbol}")
                                        skip = True
                                        break
                                if skip:
                                    continue
                                for reference in references:
                                    dest_file = reference.path
                                    if dest_file == file:
                                        continue
                                    new_files.add(dest_file)
                                    #print(f"{symbol.name}:{file}:{symbol.start_position.position.line}:{symbol.start_position.position.character} is referenced at {dest_file}:{reference.position.line}:{reference.position.character}")
                                    edges.setdefault((file, dest_file), set()).add(symbol.name)
                            file_bar.update(title=f"Processing file {j+2}/{len(current_files)}: {current_files[j+1] if j+1 < len(current_files) else ''}")
                        current_files = list(new_files)

                    hop_bar.update(title=f"On hop {i+2}/{hops}")
            if not edges:
                return file_path
            return edges
    return (process_file,)


@app.cell
def __(GetReferencesRequest, SymbolApi, api_client, file, update_status):
    def process_symbol(symbol, new_files, edges):
        update_status(symbol.name)
        get_references_request = GetReferencesRequest(start_position=symbol.start_position)
        references = SymbolApi(api_client).find_references(get_references_request).references
        for reference in references:
            dest_file = reference.path
            new_files.add(dest_file)
            if dest_file == file:
                continue
            edges.setdefault((file, dest_file), set()).add(symbol.name)
    return (process_symbol,)


@app.cell
def __():
    def create_mermaid_from_dependencies(dependencies: dict) -> str:
        """
        Convert a dictionary of file dependencies and their referenced symbols into a Mermaid diagram string.
        Arrows point from referenced file back to source file through reference nodes.
        If no dependencies exist, displays a single node for the root file.
        
        Args:
            dependencies: Dict where keys are tuples of (defined_file, referenced_file) and values are sets of referenced symbols
                         OR a string representing the root file path when there are no dependencies
        Returns:
            String containing the Mermaid diagram definition
        """
        # Handle case where dependencies is just a root file string
        if isinstance(dependencies, str):
            base_name = dependencies.split('/')[-1]  # Get just the filename
            clean_name = base_name.replace('"', '&quot;')
            return f"""graph LR
        root["{clean_name}"]
        classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
        classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;
        class root source;"""

        if not dependencies:
            return "graph LR\n    %% No dependencies to display"

        # Rest of the function remains the same...
        mermaid_lines = ["graph LR"]
        
        unique_files = set()
        node_names = {}
        
        for defined_file, referenced_file in dependencies.keys():
            unique_files.add(defined_file)
            unique_files.add(referenced_file)
        
        for idx, file in enumerate(unique_files):
            node_name = f"n{idx}"
            node_names[file] = node_name
            base_name = file.split('/')[-1]
            clean_name = base_name.replace('"', '&quot;')
            mermaid_lines.append(f'    {node_name}["{clean_name}"]')
        
        for idx, ((defined_file, referenced_file), symbols) in enumerate(dependencies.items()):
            from_node = node_names[defined_file]
            to_node = node_names[referenced_file]
            ref_node = f"ref{idx}"
            
            cleaned_symbols = []
            for symbol in sorted(symbols):
                clean_symbol = str(symbol)
                clean_symbol = clean_symbol.replace('"', '&quot;')
                clean_symbol = clean_symbol.replace('<', '&lt;')
                clean_symbol = clean_symbol.replace('>', '&gt;')
                if len(clean_symbol) > 20:
                    clean_symbol = clean_symbol[:17] + "..."
                cleaned_symbols.append(clean_symbol)
            
            symbols_display = "<br/>" + "<br/>".join(cleaned_symbols)
            if len(cleaned_symbols) > 5:
                symbols_display = "<br/>" + "<br/>".join(cleaned_symbols[:5]) + "<br/>..."
            
            ref_node_def = f'    {ref_node}["{len(symbols)} refs{symbols_display}"]'
            mermaid_lines.append(ref_node_def)
            
            mermaid_lines.append(f'    {to_node} --> {ref_node} --> {from_node}')
            mermaid_lines.append(f'    class {ref_node} reference')
        
        mermaid_lines.extend([
            "    %% Styling",
            "    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;",
            "    classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;",
            "    classDef reference fill:#e8e7ff,stroke:#6b69d6,stroke-width:2px;",
            f"    class {node_names[next(iter(dependencies))[0]]} source;"
        ])
        
        return '\n'.join(mermaid_lines)
    return (create_mermaid_from_dependencies,)


@app.cell
def __():
    import requests
    import json
    import sys
    from typing import Dict, Any, Optional

    from lsproxy import ApiClient, Configuration, SymbolApi, WorkspaceApi
    from lsproxy.models.file_position import FilePosition
    from lsproxy.models.position import Position
    from lsproxy.models.get_references_request import GetReferencesRequest
    from lsproxy.models.get_definition_request import GetDefinitionRequest
    from lsproxy.rest import ApiException
    import marimo as mo
    from dataclasses import dataclass
    return (
        Any,
        ApiClient,
        ApiException,
        Configuration,
        Dict,
        FilePosition,
        GetDefinitionRequest,
        GetReferencesRequest,
        Optional,
        Position,
        SymbolApi,
        WorkspaceApi,
        dataclass,
        json,
        mo,
        requests,
        sys,
    )


if __name__ == "__main__":
    app.run()
