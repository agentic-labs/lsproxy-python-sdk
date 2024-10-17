// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as WorkspaceSymbolsAPI from './workspace-symbols';
import * as Shared from './shared';

export class WorkspaceSymbols extends APIResource {
  /**
   * Search for symbols across the entire workspace
   *
   * Returns a list of symbols matching the given query string from all files in the
   * workspace.
   */
  list(query: WorkspaceSymbolListParams, options?: Core.RequestOptions): Core.APIPromise<SymbolResponse> {
    return this._client.get('/workspace-symbols', { query, ...options });
  }
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

export interface WorkspaceSymbolListParams {
  /**
   * The query to search for.
   */
  query: string;

  /**
   * Whether to include the raw response from the langserver in the response.
   * Defaults to false.
   */
  include_raw_response?: boolean;
}

export namespace WorkspaceSymbols {
  export import SymbolResponse = WorkspaceSymbolsAPI.SymbolResponse;
  export import WorkspaceSymbolListParams = WorkspaceSymbolsAPI.WorkspaceSymbolListParams;
}
