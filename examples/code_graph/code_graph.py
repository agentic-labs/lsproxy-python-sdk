import marimo

__generated_with = "0.9.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import requests
    import json
    import sys
    from typing import Dict, Any, Optional

    from lsproxy import Lsproxy, GetReferencesRequest, GetDefinitionRequest

    import marimo as mo
    from dataclasses import dataclass
    return (
        Any,
        Dict,
        GetDefinitionRequest,
        GetReferencesRequest,
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
def __(mo, start_button):
    mo.md("## Example 1: Exploring symbols in a file\n---\n") if start_button.value else ""
    return


@app.cell
def __(selections_1):
    selections_1
    return


@app.cell
def __(api_client, lang_dropdown_1, mo):
    table = None
    if lang_dropdown_1.value:
        # Pull the definitions inside a file
        symbols_1 = api_client.definitions_in_file(lang_dropdown_1.value)
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
    symbols_1,
    table,
):
    code_text = ""
    ref_text = ""
    if table is not None and table.value:
        symbol = symbols_1[table.value[0].get("index")]

        # Get the references to this symbol along with some code context on where it's used
        reference_request = GetReferencesRequest(
            identifier_position=symbol.identifier_position,
            include_code_context_lines=1,
        )
        reference_results = api_client.find_references(reference_request)
        ref_text = pretty_format_reference_results(reference_results)


        # Get the source code for the symbol
        definition_request = GetDefinitionRequest(
            position=symbol.identifier_position, include_source_code=True
        )
        code = (
            api_client.find_definition(definition_request)
            .source_code_context[0]
            .source_code
        )
        code_text = pretty_format_code_result(code, lang_select_1)


    mo.callout(mo.vstack(
        [
            mo.md(code_text),
            mo.md(ref_text),
        ])
    )
    return (
        code,
        code_text,
        definition_request,
        ref_text,
        reference_request,
        reference_results,
        symbol,
    )


@app.cell
def __():
    def pretty_format_code_result(code_result, lang_select):
        return f"""### `Code`\n---\n```{lang_select.value}\n\n{code_result}\n```\n"""
    return (pretty_format_code_result,)


@app.cell
def __(lang_select_1):
    def pretty_format_reference_results(reference_results):
        ref_text = ["\n### `References`\n---\n"] if reference_results.references else ["\n---\n### `No references found`"]
        refs = {}
        for ref, context in zip(reference_results.references, reference_results.context):
            code = context.source_code.split("\n")
            line_nums = range(
                context.range.start.line, context.range.end.line + 1
            )
            refs.setdefault(ref.path, []).extend(zip(line_nums, code))
            refs[ref.path].append(("@@@@@", "-----"))

        for ref_file, ref_lines in refs.items():
            ref_text.append(f"**{ref_file}**\n\n```{lang_select_1.value}")
            ref_text.extend([f"{num:5}: {line}" for num, line in ref_lines])
            ref_text.append(f"```\n\n")
        return "\n".join(ref_text)
    return (pretty_format_reference_results,)


@app.cell
def __():
    # Appendix A: UI code to run the example
    return


@app.cell
def __(get_files, mo, start_button):
    # Polls all the files in the repo on initialization
    mo.stop(not start_button.value, "Initializing will read all the files for what symbols they have")
    file_symbol_dict = get_files()
    return (file_symbol_dict,)


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
    # UI Elements for the first example
    py_dropdown_1, js_dropdown_1, rs_dropdown_1 = create_dropdowns(file_symbol_dict)
    selector_dict_1 = create_selector_dict(py_dropdown_1, js_dropdown_1, rs_dropdown_1)
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
    # Combining selections for the first example
    lang_dropdown_1 = selector_dict_1[lang_select_1.value]
    selections_1 = mo.hstack(
        [lang_dropdown_1, lang_select_1],
        gap=2,
        justify="end",
    )
    return lang_dropdown_1, selections_1


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
        rs_dropdown = create_lang_dropdown(file_with_symbol_count, ["rs"], "Select a rust file ->")
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
        return {"python": py_dropdown, "typescript": js_dropdown, "rust": rs_dropdown}
    return (create_selector_dict,)


if __name__ == "__main__":
    app.run()
