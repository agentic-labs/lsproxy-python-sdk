import marimo

__generated_with = "0.9.12"
app = marimo.App(width="medium")


@app.cell
def __(hops, js_dropdown, lang_select, mo, py_dropdown, rs_dropdown):
    lang_dropdown = None
    if lang_select.value == "Python":
        lang_dropdown = py_dropdown
    elif lang_select.value == "Typescript/Javascript":
        lang_dropdown = js_dropdown
    elif lang_select.value == "Rust":
        lang_dropdown = rs_dropdown

    submit_button = mo.ui.run_button(label="Click to submit", disabled=not py_dropdown.value and not js_dropdown.value and not rs_dropdown.value)
    selections = mo.hstack([mo.vstack([lang_dropdown, hops, submit_button], align="end"), lang_select], gap=2, justify="end")
    selections
    return lang_dropdown, selections, submit_button


@app.cell
def __(
    create_graph,
    create_mermaid_from_dependencies,
    hops,
    lang_dropdown,
    mo,
    submit_button,
):
    mo.stop(not submit_button.value, "Click `submit` to build the graph")
    edges = create_graph(lang_dropdown.value, hops.value)
    mermaid_string = create_mermaid_from_dependencies(edges)
    mo.mermaid(mermaid_string)
    return edges, mermaid_string


@app.cell
def __(create_dropdowns, mo):
    py_dropdown, js_dropdown, rs_dropdown, file_symbol_dict = create_dropdowns()
    hops = mo.ui.number(1, label="Number of hops")
    lang_select = mo.ui.radio(options=["Python", "Typescript/Javascript", "Rust"], value="Python")
    return (
        file_symbol_dict,
        hops,
        js_dropdown,
        lang_select,
        py_dropdown,
        rs_dropdown,
    )


@app.cell
def __(get_files, mo):
    def create_dropdowns():
        file_dict = get_files()
        file_with_symbol_count = [(file, len(symbols)) for file, symbols in file_dict.items()] 
        file_with_symbol_count = sorted(file_with_symbol_count, key=lambda item: -item[1])
        file_options_python = {f"{file}: ({symbols} symbols)": file for file, symbols in file_with_symbol_count if file.split(".")[-1] in ["py"]}
        python_dropdown = mo.ui.dropdown(options=file_options_python, label="Python files")
        file_options_js = {f"{file}: ({symbols} symbols)": file for file, symbols in file_with_symbol_count if file.split(".")[-1] in ["ts", "tsx", "js", "jsx"]}
        print(file_options_js)
        js_dropdown = mo.ui.dropdown(options=file_options_js, label="Typescript/Javascript Files")
        file_options_rust = {f"{file}: ({symbols} symbols)": file for file, symbols in file_with_symbol_count if file.split(".")[-1] in ["rs"]}
        rs_dropdown = mo.ui.dropdown(options=file_options_rust, label="Rust files")
        return python_dropdown, js_dropdown, rs_dropdown, file_dict
    return (create_dropdowns,)


@app.cell
def __(ApiClient, Configuration, SymbolApi, WorkspaceApi, mo):
    def get_files():
        file_dict = {}
        with ApiClient(Configuration()) as api_client:
            files = WorkspaceApi(api_client).list_files()
            for i in mo.status.progress_bar(range(len(files)), title="Files processed", remove_on_exit=True):
                file = files[i]
                symbols = SymbolApi(api_client).definitions_in_file(file)
                file_dict[file] = symbols
        return file_dict
    return (get_files,)


@app.cell
def __(
    ApiClient,
    Configuration,
    WorkspaceApi,
    file_symbol_dict,
    mo,
    process_symbols,
):
    def create_graph(file_path: str, hops: int = 1):
        with ApiClient(Configuration()) as api_client:
            current_files, processed_files, edges = [file_path], set(), {}
            workspace_files = set(WorkspaceApi(api_client).list_files())
            with mo.status.progress_bar(total=hops, title=f"On hop 1/{hops}", remove_on_exit=True) as hop_bar:
                for i in range(hops):
                    new_files = set()
                    if not current_files:
                        break
                    with mo.status.progress_bar(total=len(current_files), title=f"Processing file 1/{len(current_files)}: {current_files[0]}", remove_on_exit=True) as file_bar:
                        for j, file in enumerate(current_files):
                            if file in processed_files or file not in file_symbol_dict:
                                file_bar.update(title=f"Processing file {j+2}/{len(current_files)}: {current_files[j+1] if j+1 < len(current_files) else ''}")

                                continue
                            process_symbols(api_client, file, file_symbol_dict[file], new_files, edges)
                            file_bar.update(title=f"Processing file {j+2}/{len(current_files)}: {current_files[j+1] if j+1 < len(current_files) else ''}")
                            processed_files.add(file)
                        current_files = list(new_files)

                    hop_bar.update(title=f"On hop {i+2}/{hops}")
            if not edges:
                return file_path
            elif len(edges) >= 250:
                return "Too many edges to graph"
            return edges
    return (create_graph,)


@app.cell
def __(GetReferencesRequest, SymbolApi, mo):
    def process_symbols(api_client, file, symbols, new_files, edges):
        for symbol_idx in mo.status.progress_bar(range(len(symbols)), remove_on_exit=True, title="Symbols Processed"):
            symbol = symbols[symbol_idx]
            get_references_request = GetReferencesRequest(identifier_position=symbol.identifier_position)
            references = SymbolApi(api_client).find_references(get_references_request).references
            for reference in references:
                dest_file = reference.path
                if dest_file != file:
                    new_files.add(dest_file)
                    edges.setdefault((file, dest_file), set()).add(symbol.name)
    return (process_symbols,)


@app.cell
def __():
    def create_mermaid_from_dependencies(dependencies: dict, max_chars: int = 50) -> str:
        """
        Convert a dictionary of file dependencies and their referenced symbols into a Mermaid diagram string.
        Arrows point from referenced file back to source file through reference nodes.

        Args:
            dependencies: Dict where keys are tuples of (defined_file, referenced_file) and values are sets of referenced symbols
                         OR a string representing the root file path when there are no dependencies
            max_chars: Maximum length for displayed file paths, truncating from left if needed

        Returns:
            String containing the Mermaid diagram definition
        """
        def get_display_name(file_path: str) -> str:
            """Get display name for a file, truncating from left if needed."""
            if len(file_path) <= max_chars:
                return file_path
            return "..." + file_path[-(max_chars-3):]

        # Handle case where dependencies is just a root file string
        if isinstance(dependencies, str):
            clean_name = get_display_name(dependencies).replace('"', '&quot;')
            return f"""graph LR
        root["{clean_name}"]
        classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
        classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;
        class root source;"""

        if not dependencies:
            return "graph LR\n    %% No dependencies to display"

        mermaid_lines = ["graph LR"]

        # Collect all unique files and create nodes
        unique_files = set()
        for defined_file, referenced_file in dependencies.keys():
            unique_files.add(defined_file)
            unique_files.add(referenced_file)

        # Create nodes for each unique file
        node_names = {}
        for idx, file in enumerate(unique_files):
            node_name = f"n{idx}"
            node_names[file] = node_name
            display_name = get_display_name(file)
            clean_name = display_name.replace('"', '&quot;')
            mermaid_lines.append(f'    {node_name}["{clean_name}"]')

        # Create reference nodes and connections
        for idx, ((defined_file, referenced_file), symbols) in enumerate(dependencies.items()):
            from_node = node_names[defined_file]
            to_node = node_names[referenced_file]
            ref_node = f"ref{idx}"

            # Clean and truncate symbols
            cleaned_symbols = []
            for symbol in sorted(symbols):
                clean_symbol = str(symbol)
                clean_symbol = clean_symbol.replace('"', '&quot;')
                clean_symbol = clean_symbol.replace('<', '&lt;')
                clean_symbol = clean_symbol.replace('>', '&gt;')
                if len(clean_symbol) > 20:
                    clean_symbol = clean_symbol[:17] + "..."
                cleaned_symbols.append(clean_symbol)

            # Create symbol display with limited number of examples
            symbols_display = "<br/>" + "<br/>".join(cleaned_symbols)
            if len(cleaned_symbols) > 5:
                symbols_display = "<br/>" + "<br/>".join(cleaned_symbols[:5]) + "<br/>..."

            # Add reference node and connections
            ref_node_def = f'    {ref_node}["{len(symbols)} refs{symbols_display}"]'
            mermaid_lines.append(ref_node_def)
            mermaid_lines.append(f'    {to_node} --> {ref_node} --> {from_node}')
            mermaid_lines.append(f'    class {ref_node} reference')

        # Add styling
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
