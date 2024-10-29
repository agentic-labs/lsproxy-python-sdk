import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import requests
    import json
    import sys
    from typing import Dict, Any, Optional

    from lsproxy import Lsproxy

    import marimo as mo
    from dataclasses import dataclass

    return Any, Dict, Lsproxy, Optional, dataclass, json, mo, requests, sys


@app.cell
def __(Lsproxy):
    api_client = Lsproxy()
    return (api_client,)


@app.cell
def __():
    def create_mermaid_from_dependencies(
        dependencies: dict, max_chars: int = 50
    ) -> str:
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
            return "..." + file_path[-(max_chars - 3) :]

        # Handle case where dependencies is just a root file string
        if isinstance(dependencies, str):
            clean_name = get_display_name(dependencies).replace('"', "&quot;")
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
            clean_name = display_name.replace('"', "&quot;")
            mermaid_lines.append(f'    {node_name}["{clean_name}"]')

        # Create reference nodes and connections
        for idx, ((defined_file, referenced_file), symbols) in enumerate(
            dependencies.items()
        ):
            from_node = node_names[defined_file]
            to_node = node_names[referenced_file]
            ref_node = f"ref{idx}"

            # Clean and truncate symbols
            cleaned_symbols = []
            for symbol in sorted(symbols):
                clean_symbol = str(symbol)
                clean_symbol = clean_symbol.replace('"', "&quot;")
                clean_symbol = clean_symbol.replace("<", "&lt;")
                clean_symbol = clean_symbol.replace(">", "&gt;")
                if len(clean_symbol) > 20:
                    clean_symbol = clean_symbol[:17] + "..."
                cleaned_symbols.append(clean_symbol)

            # Create symbol display with limited number of examples
            symbols_display = "<br/>" + "<br/>".join(cleaned_symbols)
            if len(cleaned_symbols) > 5:
                symbols_display = (
                    "<br/>" + "<br/>".join(cleaned_symbols[:5]) + "<br/>..."
                )

            # Add reference node and connections
            ref_node_def = f'    {ref_node}["{len(symbols)} refs{symbols_display}"]'
            mermaid_lines.append(ref_node_def)
            mermaid_lines.append(f"    {to_node} --> {ref_node} --> {from_node}")
            mermaid_lines.append(f"    class {ref_node} reference")

        # Add styling
        mermaid_lines.extend(
            [
                "    %% Styling",
                "    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;",
                "    classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px;",
                "    classDef reference fill:#e8e7ff,stroke:#6b69d6,stroke-width:2px;",
                f"    class {node_names[next(iter(dependencies))[0]]} source;",
            ]
        )

        return "\n".join(mermaid_lines)

    return (create_mermaid_from_dependencies,)


@app.cell
def __(create_dropdowns, mo):
    py_dropdown, js_dropdown, rs_dropdown, file_symbol_dict = create_dropdowns()
    hops = mo.ui.number(1, label="Number of hops (Recommend 1-2 to start)")
    lang_select = mo.ui.radio(
        options=["Python", "Typescript/Javascript", "Rust"], value="Python"
    )
    return (
        file_symbol_dict,
        hops,
        js_dropdown,
        lang_select,
        py_dropdown,
        rs_dropdown,
    )


@app.cell
def __(hops, js_dropdown, lang_select, mo, py_dropdown, rs_dropdown):
    lang_dropdown = None
    if lang_select.value == "Python":
        lang_dropdown = py_dropdown
    elif lang_select.value == "Typescript/Javascript":
        lang_dropdown = js_dropdown
    elif lang_select.value == "Rust":
        lang_dropdown = rs_dropdown

    submit_button = mo.ui.run_button(
        label="Click to submit", disabled=not lang_dropdown.value
    )
    selections = mo.hstack(
        [mo.vstack([lang_dropdown, hops, submit_button], align="end"), lang_select],
        gap=2,
        justify="end",
    )
    selections
    return lang_dropdown, selections, submit_button


@app.cell
def __(
    GraphBuilder,
    api_client,
    create_mermaid_from_dependencies,
    hops,
    lang_dropdown,
    mo,
    submit_button,
):
    mo.stop(not submit_button.value, "Click `submit` to build the graph")
    builder = GraphBuilder(api_client, lang_dropdown.value, hops.value)
    mermaid_string = create_mermaid_from_dependencies(builder.edges)
    mo.mermaid(mermaid_string)
    return builder, mermaid_string


@app.cell
def __(create_lang_dropdown, get_files):
    def create_dropdowns():
        file_dict = get_files()
        file_with_symbol_count = [
            (file, len(symbols))
            for file, symbols in file_dict.items()
            if len(symbols) > 0
        ]
        file_with_symbol_count = sorted(
            file_with_symbol_count, key=lambda item: -item[1]
        )
        py_dropdown = create_lang_dropdown(
            file_with_symbol_count, ["py"], "Python files"
        )
        js_dropdown = create_lang_dropdown(
            file_with_symbol_count,
            ["ts", "tsx", "js", "jsx"],
            "Typescript/Javascript files",
        )
        rs_dropdown = create_lang_dropdown(file_with_symbol_count, ["rs"], "Rust files")
        return py_dropdown, js_dropdown, rs_dropdown, file_dict

    return (create_dropdowns,)


@app.cell
def __(api_client, mo):
    def get_files():
        file_dict = {}
        files = api_client.list_files()
        for file in mo.status.progress_bar(
            files, title="Files processed", remove_on_exit=True
        ):
            symbols = api_client.definitions_in_file(file)
            file_dict[file] = symbols
        return file_dict

    return (get_files,)


@app.cell
def __(mo):
    def create_lang_dropdown(file_symbol_dict, endings, label):
        file_options = {
            f"{file}: ({symbols} symbols)": file
            for file, symbols in file_symbol_dict
            if file.split(".")[-1] in endings
        }
        return mo.ui.dropdown(options=file_options, label=label)

    return (create_lang_dropdown,)


@app.cell
def __(GetReferencesRequest, SymbolApi, file_symbol_dict, mo):
    class GraphBuilder:
        def __init__(self, api_client, root_file, hops):
            # data
            self.api_client = api_client

            # State for graph generation
            self.root_file = root_file
            self.current_files = [root_file]
            self.next_hop_files = set()
            self.processed_files = set()
            self.edges = {}
            self.create_graph(hops)

        def create_graph(self, hops):
            with mo.status.progress_bar(
                total=hops, title=f"On hop 1/{hops}", remove_on_exit=True
            ) as hop_bar:
                for i in range(hops):
                    if not self.current_files:
                        break
                    self.process_hop()
                    hop_bar.update(title=f"On hop {i+2}/{hops}")

            # If we don't have any or too many edges just return a string
            if not self.edges:
                self.edges = self.root_file
            elif len(self.edges) >= 250:
                self.edges = "Too many edges to graph"

        def process_hop(self):
            with mo.status.progress_bar(
                total=len(self.current_files),
                title=f"Processing file 1/{len(self.current_files)}: {self.current_files[0]}",
                remove_on_exit=True,
            ) as file_bar:
                for j, file in enumerate(self.current_files):
                    if file not in self.processed_files and file in file_symbol_dict:
                        self.process_symbols_in_file(file)
                    if j + 1 < len(self.current_files):
                        file_bar.update(
                            title=f"Processing file {j+2}/{len(self.current_files)}: {self.current_files[j+1]}"
                        )
                self.current_files = list(self.next_hop_files)

        def process_symbols_in_file(self, file):
            for symbol in mo.status.progress_bar(
                file_symbol_dict[file], remove_on_exit=True, title="Symbols Processed"
            ):
                get_references_request = GetReferencesRequest(
                    identifier_position=symbol.identifier_position
                )
                references = (
                    SymbolApi(self.api_client)
                    .find_references(get_references_request)
                    .references
                )
                for reference in references:
                    dest_file = reference.path
                    if dest_file != file:
                        self.next_hop_files.add(dest_file)
                        self.edges.setdefault((file, dest_file), set()).add(symbol.name)
            self.processed_files.add(file)

    return (GraphBuilder,)


if __name__ == "__main__":
    app.run()
