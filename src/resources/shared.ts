// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

/**
 * Specific position within a file.
 */
export interface Position {
  path: string;

  position: Position.Position;
}

export namespace Position {
  export interface Position {
    /**
     * 0-indexed character index.
     */
    character: number;

    /**
     * 0-indexed line number.
     */
    line: number;
  }
}

export interface Symbol {
  /**
   * Specific position within a file.
   */
  identifier_start_position: Position;

  /**
   * The kind of the symbol (e.g., function, class).
   */
  kind: string;

  /**
   * The name of the symbol.
   */
  name: string;

  source_code?: unknown | null;
}

export interface SymbolResponse {
  symbols: Array<Symbol>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#document_symbol
   */
  raw_response?: unknown | null;
}
