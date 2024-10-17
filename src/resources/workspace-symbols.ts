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
  list(
    query: WorkspaceSymbolListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<Shared.SymbolResponse> {
    return this._client.get('/workspace-symbols', { query, ...options });
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
  export import WorkspaceSymbolListParams = WorkspaceSymbolsAPI.WorkspaceSymbolListParams;
}
