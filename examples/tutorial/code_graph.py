import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import requests
    import json
    import sys
    from typing import Dict, Any, Optional, List

    from lsproxy import GetReferencesRequest, FileRange, Position

    import marimo as mo
    return (
        Any,
        Dict,
        FileRange,
        GetReferencesRequest,
        List,
        Optional,
        Position,
        json,
        mo,
        requests,
        sys,
    )


@app.cell
def __(mo):
    mo.md("""### Welcome to the `lsproxy` tutorial! We'll be showing you how you can use `lsproxy` to easily navigate and search another codebase using python. Let's get started!\n> We will be using an open-source repo to demonstrate `lsproxy`. We chose [Trieve](https://github.com/devflowinc/trieve), a rust-based infrastructure solution for search, recommendations and RAG. They have rust for their backend, and typescript to run multiple frontend interfaces. We love their product and their team, check them out!""")
    return


@app.cell
def __(mo):
    mo.md("""<div style="height: 50px;"></div>""")
    return


@app.cell
def __(mo):
    # The first step is to create our API client
    from lsproxy import Lsproxy

    api_client = Lsproxy()
    mo.show_code()
    return Lsproxy, api_client


@app.cell
def __(mo):
    mo.md("""Other than starting the `lsproxy` docker container, no initialization is required to use `lsproxy`. Here, our "initialization" is just reading in the files to make the tutorial easier to navigate! Please click the button below to get started.""")
    return


@app.cell
def __(mo):
    start_button = mo.ui.run_button(label="Click to initialize")
    start_button
    return (start_button,)


@app.cell
def __(get_files, mo, start_button):
    # Reads all the files in the repo on initialization
    mo.stop(not start_button.value)
    file_symbol_dict = get_files()
    return (file_symbol_dict,)


@app.cell
def __(mo):
    mo.md("""<div style="height: 100px;"></div>""")
    return


@app.cell
def __(file_symbol_dict, mo):
    mo.stop(not file_symbol_dict)

    mo.md(
        """### `Example 1: Exploring symbols and their references in a file`\nYou'll see how easy it is to:\n\n- Get symbol definitions from a file.\n- Read the source code for any symbol.\n- Find references to the symbol across the codebase\n\n<p>Also note that we are only showing typescript and rust in this example, but we also support python!</p>\n---\n"""
    )
    return


@app.cell
def __(selections_ex1):
    selections_ex1
    return


@app.cell
def __(code_language_select_ex1, file_dropdown_ex1, mo):
    # This is just for controlling the flow of this tutorial
    mo.stop(not file_dropdown_ex1.value)
    selected_file_first_time = True
    code_language_ex1 = code_language_select_ex1.value
    selected_file_ex1 = file_dropdown_ex1.value
    return code_language_ex1, selected_file_ex1, selected_file_first_time


@app.cell
def __(code_language_ex1, mo, selected_file_first_time):
    # This is just for controlling the flow of this tutorial
    mo.stop(not selected_file_first_time)

    mo.md(
        f"Note that you selected a file in {code_language_ex1}, but `lsproxy` wraps language servers for all the supported languages, and routes your request to the right one, so you don't have to worry about configuring servers for each language. Go ahead and try a different language!"
    )
    return


@app.cell
def __(api_client, mo, selected_file_ex1):
    # Retrieving the symbols defined in a file is just a single call
    symbols_ex1 = api_client.definitions_in_file(selected_file_ex1)

    mo.show_code()
    return (symbols_ex1,)


@app.cell
def __(mo, symbols_ex1):
    # Pack the data from the symbols into a tabular format
    table_data_ex1 = [
        {
            "name": symbol.name,
            "kind": symbol.kind,
            "start_line": symbol.identifier_position.position.line,
            "start_character": symbol.identifier_position.position.character,
            "num_lines": symbol.range.end.line - symbol.range.start.line + 1,
            "index": i,
        }
        for i, symbol in enumerate(symbols_ex1)
    ]

    # Create the table element to display
    symbol_table_ex1 = mo.ui.table(
        data=table_data_ex1,
        page_size=10,
        selection="single",
        label="Now, select a symbol to view code and references",
    )
    # Display the table
    symbol_table_ex1
    return symbol_table_ex1, table_data_ex1


@app.cell
def __(mo, symbol_table_ex1, symbols_ex1):
    mo.stop(not symbol_table_ex1.value)
    selected_symbol_ex1 = symbols_ex1[symbol_table_ex1.value[0].get("index")]
    return (selected_symbol_ex1,)


@app.cell
def __(
    FileRange,
    GetReferencesRequest,
    api_client,
    mo,
    selected_file_ex1,
    selected_symbol_ex1,
):
    # Read the source code for a particular range in a file by just asking for it!
    file_range_ex1 = FileRange(
        path=selected_file_ex1,
        start=selected_symbol_ex1.range.start,
        end=selected_symbol_ex1.range.end,
    )
    source_code_ex1 = api_client.read_source_code(file_range_ex1).source_code

    # Get references to the symbol and optionally include context lines surrounding the usage
    reference_request_ex1 = GetReferencesRequest(
        identifier_position=selected_symbol_ex1.identifier_position,
        include_code_context_lines=2,
    )
    reference_results_ex1 = api_client.find_references(reference_request_ex1)
    viewed_symbol = True
    mo.show_code()
    return (
        file_range_ex1,
        reference_request_ex1,
        reference_results_ex1,
        source_code_ex1,
        viewed_symbol,
    )


@app.cell
def __(
    code_language_ex1,
    mo,
    pretty_format_code_result,
    pretty_format_reference_results,
    reference_results_ex1,
    source_code_ex1,
):
    # Format the code and reference results for display
    code_text_ex1 = pretty_format_code_result(source_code_ex1, code_language_ex1)
    reference_text_ex1 = pretty_format_reference_results(
        reference_results_ex1, code_language_ex1
    )

    # Display the code and reference text
    mo.callout(
        mo.vstack(
            [
                mo.md(code_text_ex1),
                mo.md(reference_text_ex1),
            ]
        )
    )
    return code_text_ex1, reference_text_ex1


@app.cell
def __(mo, viewed_symbol):
    mo.stop(not viewed_symbol)
    example_2 = mo.ui.run_button(label="Click to move on to example 2: Exploring connections between files", full_width=True)
    example_2
    return (example_2,)


@app.cell
def __(mo):
    mo.md("""<div style="height: 100px;"></div>""")
    return


@app.cell
def __(example_2, mo):
    mo.stop(not example_2.value)
    ex2_unlocked = True
    return (ex2_unlocked,)


@app.cell
def __(ex2_unlocked, mo, selections_2):
    mo.stop(not ex2_unlocked)
    mo.vstack([
    mo.md("""### Example 2: Exploring connections between files\nThe examples above are similar to the kind of functionality you can find in your IDE, but having everything accessible with easy python functions means that you can compose these operations to be much more powerful.\n\nIn this example, we show:\n\n- Finding all the files that reference a given file\n- Tagging each file with the symbols it references\n\n---"""),
    selections_2,
    ])
    return


@app.cell
def __(ex2_unlocked, file_dropdown_2, mo):
    mo.stop(not ex2_unlocked)
    # Pull the symbols inside a file
    selected_file_ex2 = file_dropdown_2.value
    return (selected_file_ex2,)


@app.cell
def __(api_client, mo, selected_file_ex2):
    # As before we can get all of the symbols from a file
    symbols_ex2 = api_client.definitions_in_file(selected_file_ex2)
    mo.show_code()
    return (symbols_ex2,)


@app.cell
def __(
    GetReferencesRequest,
    api_client,
    mo,
    selected_file_ex2,
    symbols_ex2,
):
    # But now we can repeatedly look for references on EVERY symbol in the file and build up a graph of the references
    referenced_symbols_in_file_dict = {}
    for symbol in mo.status.progress_bar(
        symbols_ex2, title="Symbols processed", remove_on_exit=True
    ):
        reference_request_ex2 = GetReferencesRequest(
            identifier_position=symbol.identifier_position,
        )
        references_ex2 = api_client.find_references(reference_request_ex2).references

        # Save which symbols were referenced by which file
        for ref in references_ex2:
            referencing_file = ref.path
            if referencing_file != selected_file_ex2:
                referenced_symbols_in_file_dict.setdefault(
                    (selected_file_ex2, referencing_file), set()
                ).add(symbol.name)
    mo.show_code()
    return (
        ref,
        reference_request_ex2,
        referenced_symbols_in_file_dict,
        references_ex2,
        referencing_file,
        symbol,
    )


@app.cell
def __(ex2_unlocked, mo):
    mo.stop(not ex2_unlocked)

    mo.md(
        "From this information we can build a simple graph showing how a file's symbols are referenced by other files in the codebase."
    )
    return


@app.cell
def __(generate_reference_diagram, mo, referenced_symbols_in_file_dict):
    if not referenced_symbols_in_file_dict:
        mermaid_diagram = generate_reference_diagram("No external references found")
    else:
        mermaid_diagram = generate_reference_diagram(referenced_symbols_in_file_dict)
    diagram_shown = True
    mo.mermaid(mermaid_diagram)
    return diagram_shown, mermaid_diagram


@app.cell
def __(mo):
    mo.md("""<div style="height: 100px;"></div>""")
    return


@app.cell
def __(diagram_shown, mo):
    mo.stop(not diagram_shown)
    example_3 = mo.ui.run_button(label="Click to move on to example 3: Analyzing a change diff with call hierarchy.", full_width=True)
    example_3
    return (example_3,)


@app.cell
def __(example_3, mo):
    mo.stop(not example_3.value)
    mo.md(
        """### Example 3 (Advanced): Analyzing a change diff with call hierarchy.\n We can compose definitions and references to identify the full code paths that are affected by a particular change, and uncover ripple effects through the codebase.\n\n---"""
    )
    return


@app.cell
def __(example_3, mo):
    mo.stop(not example_3.value)
    import subprocess
    import io
    from pydantic import BaseModel
    mo.md("""Let's start with a diff of a change to the deletion logic in Trieve in this [PR](https://github.com/devflowinc/trieve/pull/2649)""")
    return BaseModel, io, subprocess


@app.cell
def __(mo, subprocess):
    parent_commit = "1910d6867877bfdd64ca822e266372335392a8be"

    # Load in the diff
    diff_text = subprocess.check_output(
        ["git", "diff", parent_commit], cwd="./trieve"
    ).decode("utf-8")

    mo.show_code(f"Output: Diff has {len(diff_text.splitlines())} lines")
    return diff_text, parent_commit


@app.cell
def __(example_3, mo):
    mo.stop(not example_3.value)
    mo.md("""First, we extract affected lines from the diff text.""")
    return


@app.cell
def __(Dict, List, Tuple, diff_text, io, mo):
    from unidiff import PatchSet

    def parse_diff(diff_text) -> Tuple[Dict[str, List[int]], str]:
        patch = PatchSet(io.StringIO(diff_text))
        affected_lines = {}
        for patched_file in patch:
            for hunk in patched_file:
                for line in hunk:
                    if line.is_added:
                        affected_lines.setdefault(patched_file.path, set()).add(
                            line.target_line_no
                        )
                    elif line.is_removed:
                        affected_lines.setdefault(patched_file.path, set()).add(
                            line.source_line_no
                        )
        return affected_lines


    affected_lines = parse_diff(diff_text)

    mo.show_code(
        f"Output: Diff contains {sum([len(lines) for lines in affected_lines.values()])} changed lines in {len(affected_lines)} files."
    )
    return PatchSet, affected_lines, parse_diff


@app.cell
def __(example_3, mo):
    mo.stop(not example_3.value)
    mo.md("""Then we define logic to \n\n 1. Find symbol definitions containing affected lines\n\n 2. Find references to these symbols.\n\n 3. Repeat with lines containing references, until we reach the end.\n\nWe also save the symbols that are direct parents of affected lines, so we can distinguish them from the symbols indirectly affected by the change.""")
    return


@app.cell
def __(BaseModel, GetReferencesRequest, List, Set, Tuple, api_client, mo):
    from lsproxy import FilePosition


    class HierarchyItem(BaseModel):
        name: str
        kind: str
        defined_at: FilePosition
        source_code: str

        def __hash__(self) -> int:
            return hash(
                (
                    self.defined_at.path,
                    self.defined_at.position.line,
                    self.defined_at.position.character,
                )
            )


    def get_symbols_containing_positions(
        target_positions: List[FilePosition],
    ) -> List[HierarchyItem]:
        file_path = target_positions[0].path

        #######################
        ### Get definitions ###
        #######################
        symbols = api_client.definitions_in_file(file_path)
        symbols_containing_position = {
            HierarchyItem(
                name=symbol.name,
                kind=symbol.kind,
                defined_at=symbol.identifier_position,
                source_code=api_client.read_source_code(symbol.range).source_code,
            )
            for symbol in symbols
            for target_position in target_positions
            if symbol.range.contains(target_position)
        }
        return symbols_containing_position


    def get_hierarchy_incoming(starting_positions: List[FilePosition]):
        """
        Compute the chain of code symbols that touch the code at the starting positions.
        """
        nodes: Set[HierarchyItem] = set()
        edges: Set[Tuple[HierarchyItem, HierarchyItem]] = set()

        # Initialize with symbols that contain the starting positions
        initial_symbols = get_symbols_containing_positions(starting_positions)
        stack = list(initial_symbols)

        while stack:
            symbol = stack.pop()
            if symbol in nodes:
                continue
            nodes.add(symbol)

            #######################
            ### Find references ###
            #######################
            references = api_client.find_references(
                GetReferencesRequest(
                    identifier_position=symbol.defined_at,
                    include_declaration=False,
                )
            ).references

            references_by_file = {}
            for ref in references:
                references_by_file.setdefault(ref.path, []).append(ref)

            # Find symbols that contain the references, we will process these next
            related_symbols = [
                sym
                for refs in references_by_file.values()
                for sym in get_symbols_containing_positions(refs)
            ]

            for related_symbol in related_symbols:
                if related_symbol != symbol:
                    edges.add((symbol, related_symbol))
                    stack.append(related_symbol)

        return nodes, edges, initial_symbols


    mo.show_code()
    return (
        FilePosition,
        HierarchyItem,
        get_hierarchy_incoming,
        get_symbols_containing_positions,
    )


@app.cell
def __(
    FilePosition,
    Position,
    affected_lines,
    api_client,
    get_hierarchy_incoming,
    mo,
):
    affected_files = list(affected_lines.keys())
    lsp_files = api_client.list_files()
    affected_files = [file for file in affected_files if file in lsp_files]

    all_nodes = set()
    all_edges = set()
    symbols_changed_directly = set()
    for file in affected_files:
        starting_positions = [
            FilePosition(path=file, position=Position(line=line, character=0))
            for line in affected_lines[file]
        ]
        nodes, edges, initial = get_hierarchy_incoming(starting_positions)
        all_nodes.update(nodes)
        all_edges.update(edges)
        symbols_changed_directly.update(initial)
    mo.show_code()
    return (
        affected_files,
        all_edges,
        all_nodes,
        edges,
        file,
        initial,
        lsp_files,
        nodes,
        starting_positions,
        symbols_changed_directly,
    )


@app.cell
def __(HierarchyItem, Set, Tuple):
    def hierarchy_to_mermaid(
        nodes: Set[HierarchyItem],
        edges: Set[Tuple[HierarchyItem, HierarchyItem]],
        symbols_changed_directly: Set[HierarchyItem],
    ) -> str:
        """
        Convert hierarchy nodes and edges to a Mermaid diagram string with subgraphs by file.
        Uses hash codes as node identifiers. Nodes that were changed directly are colored red.

        Args:
            nodes: Set of HierarchyItem objects representing code symbols
            edges: Set of tuples containing (from_symbol, to_symbol) relationships
            symbols_changed_directly: Set of HierarchyItem objects that were changed directly

        Returns:
            str: Mermaid diagram representation of the hierarchy with file-based subgraphs
        """
        mermaid_lines = [
            "%%{",
            "  init: {",
            "    'flowchart': {",
            "      'rankSpacing': 100,",  # Increase vertical space between ranks
            "      'nodeSpacing': 50,",  # Increase horizontal space between nodes
            "      'padding': 20",  # Add padding around the entire diagram
            "    }",
            "  }",
            "}%%",
            "graph TD",
        ]

        # Track nodes that need red styling
        direct_node_ids = set()
        indirect_node_ids = set()

        # Group nodes by file
        nodes_by_file = {}
        for node in nodes:
            file_path = node.defined_at.path
            if file_path not in nodes_by_file:
                nodes_by_file[file_path] = []
            nodes_by_file[file_path].append(node)

            # Track node IDs that need to be colored red
            if node in symbols_changed_directly:
                direct_node_ids.add(f"node{abs(hash(node))}")
            else:
                indirect_node_ids.add(f"node{abs(hash(node))}")

        # Create subgraphs for each file
        for file_idx, (file_path, file_nodes) in enumerate(nodes_by_file.items()):
            # Create subgraph with unique ID
            subgraph_id = f"subgraph_{file_idx}"
            mermaid_lines.append(f"    subgraph {subgraph_id}[{file_path}]")

            # Add nodes for this file
            for node in file_nodes:
                # Escape quotes and special characters in names
                escaped_name = node.name.replace('"', '\\"')
                # Add kind as a suffix in italics
                label = f'"{escaped_name}<br><i>{node.kind}</i>"'
                # Use absolute value of hash to ensure positive ID
                node_id = f"node{abs(hash(node))}"
                mermaid_lines.append(f"        {node_id}[{label}]")

            # Close subgraph
            mermaid_lines.append("    end")

        # Add edges using hash IDs (outside subgraphs)
        for from_node, to_node in edges:
            from_id = f"node{abs(hash(from_node))}"
            to_id = f"node{abs(hash(to_node))}"
            mermaid_lines.append(f"    {from_id} --> {to_id}")

        # Add styling for red nodes
        for node_id in indirect_node_ids:
            mermaid_lines.append(f"    style {node_id} fill:#ffcccc,color:#000")
        for node_id in direct_node_ids:
            mermaid_lines.append(f"    style {node_id} fill:#ffffff,color:#000")

        return "\n".join(mermaid_lines)
    return (hierarchy_to_mermaid,)


@app.cell
def __(
    all_edges,
    all_nodes,
    hierarchy_to_mermaid,
    mo,
    symbols_changed_directly,
):
    mm = hierarchy_to_mermaid(all_nodes, all_edges, symbols_changed_directly)
    mo.vstack([
        mo.md("### Call graph of the code affected by the change.\n #### The white nodes are present in the diff, while the red ones are affected indirectly."),
        mo.mermaid(mm)
    ])
    return (mm,)


@app.cell
def __(affected_lines, all_nodes, mo):
    diff_files = set(affected_lines.keys())
    call_hierarchy_files = set([n.defined_at.path for n in all_nodes])
    affected_files_not_in_diff = call_hierarchy_files - diff_files
    affected_files_not_in_diff_str = '\n'.join([f'{i+1}. {f}' for i, f in enumerate(affected_files_not_in_diff)])
    mo.md(f"We now see code paths crossing {len(affected_files_not_in_diff)} files that are not in the diff:\n\n{affected_files_not_in_diff_str}")
    return (
        affected_files_not_in_diff,
        affected_files_not_in_diff_str,
        call_hierarchy_files,
        diff_files,
    )


@app.cell
def __(mo):
    mo.md("""<div style="height: 400px;"></div>""")
    return


@app.cell
def __(mo):
    mo.md("""Thanks for trying `lsproxy`! See the README on our [github repo](https://github.com/agentic-labs/lsproxy) to run on your own code. Or if you want to play with the code in this example, you can use:\n\n```./examples/run.sh --edit```""")
    return


@app.cell
def __():
    # Appendix A: UI code to run the example
    return


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
    # UI Elements for the first example
    js_dropdown_1, rs_dropdown_1 = create_dropdowns(file_symbol_dict, "server/src/handlers/chunk_handler.rs: (65 symbols)")
    selector_dict_1 = create_selector_dict(js_dropdown_1, rs_dropdown_1)
    code_language_select_ex1 = mo.ui.radio(options=["typescript", "rust"], value="rust")
    return (
        code_language_select_ex1,
        js_dropdown_1,
        rs_dropdown_1,
        selector_dict_1,
    )


@app.cell
def __(code_language_select_ex1, mo, selector_dict_1):
    # Combining UI selections for the first example
    file_dropdown_ex1 = selector_dict_1[code_language_select_ex1.value]
    selections_ex1 = mo.hstack(
        [file_dropdown_ex1, code_language_select_ex1],
        gap=2,
        justify="end",
    )
    return file_dropdown_ex1, selections_ex1


@app.cell
def __(create_dropdowns, create_selector_dict, file_symbol_dict, mo):
    # UI Elements for the second example
    js_dropdown_2, rs_dropdown_2 = create_dropdowns(file_symbol_dict, "server/src/handlers/analytics_handler.rs: (15 symbols)")
    selector_dict_2 = create_selector_dict(js_dropdown_2, rs_dropdown_2)
    submit_button_2 = mo.ui.run_button(label="Find referenced files")
    code_language_select_ex2 = mo.ui.radio(options=["typescript", "rust"], value="rust")
    return (
        code_language_select_ex2,
        js_dropdown_2,
        rs_dropdown_2,
        selector_dict_2,
        submit_button_2,
    )


@app.cell
def __(code_language_select_ex2, mo, selector_dict_2):
    # Combining UI selections for the second example
    file_dropdown_2 = selector_dict_2[code_language_select_ex2.value]
    selections_2 = mo.hstack(
        [
            file_dropdown_2,
            code_language_select_ex2,
        ],
        gap=2,
        justify="end",
    )
    return file_dropdown_2, selections_2


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
    def create_dropdowns(file_dict, value = None):
        file_with_symbol_count = [
            (file, len(symbols))
            for file, symbols in file_dict.items()
            if len(symbols) > 0
        ]
        file_with_symbol_count = sorted(
            file_with_symbol_count, key=lambda item: -item[1]
        )
        js_dropdown = create_lang_dropdown(
            file_with_symbol_count,
            ["ts", "tsx", "js", "jsx"],
            "Select a typescript/javascript file ->", None
        )
        rs_dropdown = create_lang_dropdown(
            file_with_symbol_count, ["rs"], "Select a rust file ->", value
        )
        return js_dropdown, rs_dropdown
    return (create_dropdowns,)


@app.cell
def __(mo):
    def create_lang_dropdown(file_symbol_dict, endings, label, value):
        file_options = {
            f"{file}: ({symbols} symbols)": file
            for file, symbols in file_symbol_dict
            if file.split(".")[-1] in endings
        }
        if value:
            return mo.ui.dropdown(options=file_options, label=label, value=value)
        else:
            return mo.ui.dropdown(options=file_options, label=label)
    return (create_lang_dropdown,)


@app.cell
def __():
    def create_selector_dict(js_dropdown, rs_dropdown):
        return {
            "typescript": js_dropdown,
            "rust": rs_dropdown,
        }
    return (create_selector_dict,)


@app.cell
def __():
    # Appendix C: Formatting functions for the text and mermaid charts
    return


@app.cell
def __():
    def pretty_format_code_result(code_result, code_language):
        return f"""### `Code`\n---\n```{code_language}\n\n{code_result}\n```\n"""
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
            # Split the code into it's lines and add an indicator for where the reference is
            code = context.source_code.split("\n")
            line_nums = range(context.range.start.line, context.range.end.line + 1)
            before_reference = filter(
                lambda num_code: num_code[0] < ref.position.line + 1,
                zip(line_nums, code),
            )
            after_reference = filter(
                lambda num_code: num_code[0] > ref.position.line,
                zip(line_nums, code),
            )
            code_with_line_nums = (
                list(before_reference)
                + [("", "_" * ref.position.character + "^")]
                + list(after_reference)
            )

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
    def generate_reference_diagram(dependencies: dict, max_chars: int = 28) -> str:
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
            return f"""graph LR
        root["{dependencies}"]
        classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000;
        classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#000;
        class root source;"""

        if not dependencies:
            return "graph LR\n    %% No dependencies to display"

        mermaid_lines = ["graph LR"]
        # Add styling with reduced padding
        mermaid_lines.extend(
            [
                "    %% Styling",
                "    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px,color:#000,max-width:none,text-overflow:clip,padding:0px;",
                "    classDef source fill:#e1f5fe,stroke:#0277bd,stroke-width:2px,color:#000,max-width:none,text-overflow:clip,padding:0px;",
                "    classDef reference fill:#e8e7ff,stroke:#6b69d6,stroke-width:2px,color:#000,max-width:none,text-overflow:clip,padding:0px;",
            ]
        )

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

        mermaid_lines.extend(
            [
                f"    class {node_names[next(iter(dependencies))[0]]} source;",
            ]
        )

        return "\n".join(mermaid_lines)
    return (generate_reference_diagram,)


if __name__ == "__main__":
    app.run()
