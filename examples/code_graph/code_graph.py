import marimo

__generated_with = "0.9.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import requests
    import json
    import sys
    from typing import Dict, Any, Optional, List

    from lsproxy import Lsproxy, GetReferencesRequest, GetDefinitionRequest

    import marimo as mo
    from dataclasses import dataclass
    return (
        Any,
        Dict,
        GetDefinitionRequest,
        GetReferencesRequest,
        List,
        Lsproxy,
        Optional,
        dataclass,
        json,
        mo,
        requests,
        sys,
    )


@app.cell
def __(Lsproxy):
    api_client = Lsproxy()
    return (api_client,)


@app.cell
def __(mo):
    start_button = mo.ui.run_button(label="Click to initialize")
    start_button
    return (start_button,)


@app.cell
def __(get_files, mo, start_button):
    # Polls all the files in the repo on initialization
    mo.stop(not start_button.value, "Initializing will read all the files for what symbols they have")
    file_symbol_dict = get_files()
    return (file_symbol_dict,)


@app.cell
def __(mo):
    mo.md("""### Example 1: Exploring symbols and their references in a file\n---\n""")
    return


@app.cell
def __(selections_1):
    selections_1
    return


@app.cell
def __(api_client, lang_dropdown_1, mo):
    table = None
    if lang_dropdown_1.value:
        # Pull the symbols inside a file
        _selected_file = lang_dropdown_1.value
        symbols_1 = api_client.definitions_in_file(_selected_file)
        symbols_for_table = [
            {
                "name": symbol.name,
                "kind": symbol.kind,
                "start_line": symbol.identifier_position.position.line,
                "start_character": symbol.identifier_position.position.character,
                "num_lines": symbol.range.end.line - symbol.range.start.line,
                "index": i,
            }
            for i, symbol in enumerate(symbols_1)
        ]

        # Create the table element to display
        table = mo.ui.table(
            data=symbols_for_table,
            page_size=10,
            selection="single",
            label="Select a symbol to view code and references",
        )
    return symbols_1, symbols_for_table, table


@app.cell
def __(table):
    table
    return


@app.cell
def __(
    GetDefinitionRequest,
    GetReferencesRequest,
    api_client,
    lang_select_1,
    mo,
    pretty_format_code_result,
    pretty_format_reference_results,
    symbol,
    symbols_1,
    table,
):
    # The leading underscore is just to indicate that the variable is only used in this cell
    _code_text = "`Select a file and symbol above`"
    _ref_text = ""
    if table is not None and table.value:
        _symbol = symbols_1[table.value[0].get("index")]

        # Get the references to this symbol along with some code context on where it's used
        _reference_request = GetReferencesRequest(
            identifier_position=_symbol.identifier_position,
            include_code_context_lines=2,
        )
        _reference_results = api_client.find_references(_reference_request)
        _ref_text = pretty_format_reference_results(_reference_results, lang_select_1.value)

        # Get the source code for the symbol
        _definition_request = GetDefinitionRequest(
            position=symbol.identifier_position, include_source_code=True
        )
        _code = (
            api_client.find_definition(_definition_request)
            .source_code_context[0]
            .source_code
        )
        _code_text = pretty_format_code_result(_code, lang_select_1.value)


    mo.callout(
        mo.vstack(
            [
                mo.md(_code_text),
                mo.md(_ref_text),
            ]
        )
    )
    return


@app.cell
def __(mo):
    mo.md("""### Example 2: Exploring connections between files\n---\n""")
    return


@app.cell
def __(selections_2):
    selections_2
    return


@app.cell
def __(
    GetReferencesRequest,
    api_client,
    generate_reference_diagram,
    lang_dropdown_2,
    mo,
):
    if lang_dropdown_2.value:
        # Pull the symbols inside a file
        _selected_file = lang_dropdown_2.value
        symbols_2 = api_client.definitions_in_file(_selected_file)

        # For each symbol find its references and save which file references which symbols
        _reference_dict = {}
        for symbol in mo.status.progress_bar(symbols_2, title="Symbols processed", remove_on_exit=True):
            _reference_request = GetReferencesRequest(
                identifier_position=symbol.identifier_position,
            )
            _references = api_client.find_references(_reference_request).references

            # Save which symbols were referenced by which file
            for ref in _references:
                _file = ref.path
                if _file != _selected_file:
                    _reference_dict.setdefault((_selected_file, _file), set()).add(symbol.name)
        mermaid_diagram = generate_reference_diagram(_reference_dict)
    mo.mermaid(mermaid_diagram) if lang_dropdown_2.value else None
    return mermaid_diagram, ref, symbol, symbols_2


@app.cell
def __():
    def generate_reference_diagram(
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
                "    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000;",
                "    classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#000;",
                "    classDef reference fill:#e8e7ff,stroke:#6b69d6,stroke-width:2px,color:#000;",
                f"    class {node_names[next(iter(dependencies))[0]]} source;",
            ]
        )
        return "\n".join(mermaid_lines)
    return (generate_reference_diagram,)


@app.cell
def __():
    def pretty_format_code_result(code_result, code_language):
        return (
            f"""### `Code`\n---\n```{code_language}\n\n{code_result}\n```\n"""
        )
    return (pretty_format_code_result,)


@app.cell
def __():
    def pretty_format_reference_results(reference_results, code_language):
        # Header or no references
        ref_text = (
            ["\n### `References`\n---\n"]
            if reference_results.references
            else ["\n---\n### `No references found`"]
        )
        refs = {}
        for ref, context in zip(
            reference_results.references, reference_results.context
        ):
            # Split the code into it's lines and combine with the line number
            code = context.source_code.split("\n")
            line_nums = range(context.range.start.line, context.range.end.line + 1)
            code_with_line_nums = zip(line_nums, code)

            # Extend the list for the file with the new the (line_num, code) plus a separator
            file = ref.path
            refs.setdefault(file, []).extend(code_with_line_nums)
            refs[file].append(("@@@@@", "-----"))

        # For each file 
        for ref_file, ref_lines in refs.items():
            ref_text.append(f"**{ref_file}**\n\n```{code_language}")
            ref_text.extend([f"{num:5}: {line}" for num, line in ref_lines])
            ref_text.append(f"```\n\n")
        return "\n".join(ref_text)
    return (pretty_format_reference_results,)


@app.cell
def __():
    # Appendix A: UI code to run the example
    return


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
    # UI Elements for the first example
    py_dropdown_1, js_dropdown_1, rs_dropdown_1 = create_dropdowns(
        file_symbol_dict
    )
    selector_dict_1 = create_selector_dict(
        py_dropdown_1, js_dropdown_1, rs_dropdown_1
    )
    lang_select_1 = mo.ui.radio(
        options=["python", "typescript", "rust"], value="python"
    )
    return (
        js_dropdown_1,
        lang_select_1,
        py_dropdown_1,
        rs_dropdown_1,
        selector_dict_1,
    )


@app.cell
def __(lang_select_1, mo, selector_dict_1):
    # Combining UI selections for the first example
    lang_dropdown_1 = selector_dict_1[lang_select_1.value]
    selections_1 = mo.hstack(
        [lang_dropdown_1, lang_select_1],
        gap=2,
        justify="end",
    )
    return lang_dropdown_1, selections_1


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
    # UI Elements for the second example
    py_dropdown_2, js_dropdown_2, rs_dropdown_2 = create_dropdowns(
        file_symbol_dict
    )
    selector_dict_2 = create_selector_dict(
        py_dropdown_2, js_dropdown_2, rs_dropdown_2
    )
    submit_button_2 = mo.ui.run_button(label="Find referenced files")
    lang_select_2 = mo.ui.radio(
        options=["python", "typescript", "rust"], value="python"
    )
    return (
        js_dropdown_2,
        lang_select_2,
        py_dropdown_2,
        rs_dropdown_2,
        selector_dict_2,
        submit_button_2,
    )


@app.cell
def __(lang_select_2, mo, selector_dict_2, submit_button_2):
    # Combining UI selections for the second example
    lang_dropdown_2 = selector_dict_2[lang_select_2.value]
    selections_2 = mo.hstack(
        [
            mo.vstack([lang_dropdown_2, submit_button_2], align="end"),
            lang_select_2,
        ],
        gap=2,
        justify="end",
    )
    return lang_dropdown_2, selections_2


@app.cell
def __():
    # Appendix B: Helper functions to create the UI code
    return


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
def __(create_lang_dropdown):
    def create_dropdowns(file_dict):
        file_with_symbol_count = [
            (file, len(symbols))
            for file, symbols in file_dict.items()
            if len(symbols) > 0
        ]
        file_with_symbol_count = sorted(
            file_with_symbol_count, key=lambda item: -item[1]
        )
        py_dropdown = create_lang_dropdown(
            file_with_symbol_count, ["py"], "Select a python file ->"
        )
        js_dropdown = create_lang_dropdown(
            file_with_symbol_count,
            ["ts", "tsx", "js", "jsx"],
            "Select a typescript/javascript file ->",
        )
        rs_dropdown = create_lang_dropdown(
            file_with_symbol_count, ["rs"], "Select a rust file ->"
        )
        return py_dropdown, js_dropdown, rs_dropdown
    return (create_dropdowns,)


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
def __():
    def create_selector_dict(py_dropdown, js_dropdown, rs_dropdown):
        return {
            "python": py_dropdown,
            "typescript": js_dropdown,
            "rust": rs_dropdown,
        }
    return (create_selector_dict,)


if __name__ == "__main__":
    app.run()
