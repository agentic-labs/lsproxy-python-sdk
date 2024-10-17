// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import * as Shared from './shared';

/**
 * Specific position within a file.
 */
export interface FilePosition {
  character: number;

  line: number;

  path: string;
}

export interface SymbolResponse {
  symbols: Array<SymbolResponse.Symbol>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#document_symbol
   */
  raw_response?: unknown | null;
}

export namespace SymbolResponse {
  /**
   * Represents a symbol within the codebase.
   */
  export interface Symbol {
    /**
     * Specific position within a file.
     */
    identifier_start_position: Shared.FilePosition;

    /**
     * The kind of the symbol (e.g., function, class).
     */
    kind: string;

    /**
     * The name of the symbol.
     */
    name: string;
  }
}
