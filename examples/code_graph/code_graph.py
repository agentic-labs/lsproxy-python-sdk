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
def __(mo):
    mo.center(mo.md("""### Choose a file below to view the symbols defined within it"""))
    return


@app.cell
def __(selections):
    selections
    return


@app.cell
def __(api_client, lang_dropdown_1, mo):
    table = None
    if lang_dropdown_1.value:
        symbols_1 = api_client.definitions_in_file(lang_dropdown_1.value)
        symbols_for_table = [
            {
                "name": symbol.name,
                "kind": symbol.kind,
                "start_line": symbol.range.start.line,
                "num_lines": symbol.range.end.line-symbol.range.start.line,
                "index": i,
            }
            for i, symbol in enumerate(symbols_1)
        ]
        table = mo.ui.table(data=symbols_for_table, page_size=10, selection="single", label="Select a symbol to view the code")
    return symbols_1, symbols_for_table, table


@app.cell
def __(table):
    table
    return


@app.cell
def __(
    GetDefinitionRequest,
    api_client,
    lang_select_1,
    mo,
    symbols_1,
    table,
):
    code = ""
    if table is not None and table.value:
        symbol = symbols_1[table.value[0].get("index")]
        definition_request = GetDefinitionRequest(position=symbol.identifier_position, include_source_code=True)
        code = api_client.find_definition(definition_request).source_code_context[0].source_code
    mo.md(f"```{lang_select_1.value}\n{code}\n```")
    return code, definition_request, symbol


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
            file_with_symbol_count, ["py"], "Python files"
        )
        js_dropdown = create_lang_dropdown(
            file_with_symbol_count,
            ["ts", "tsx", "js", "jsx"],
            "Typescript/Javascript files",
        )
        rs_dropdown = create_lang_dropdown(file_with_symbol_count, ["rs"], "Rust files")
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


@app.cell
def __(get_files, mo, start_button):
    mo.stop(not start_button.value, "Initializing will read all the files for what symbols they have")
    file_symbol_dict = get_files()
    return (file_symbol_dict,)


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
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
    lang_dropdown_1 = selector_dict_1[lang_select_1.value]
    selections = mo.hstack(
        [lang_dropdown_1, lang_select_1],
        gap=2,
        justify="end",
    )
    return lang_dropdown_1, selections


if __name__ == "__main__":
    app.run()
