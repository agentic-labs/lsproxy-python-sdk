// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as WorkspaceAPI from './workspace';
import * as Shared from './shared';

export class Workspace extends APIResource {
  /**
   * Get a list of all files in the workspace
   *
   * Returns an array of file paths for all files in the current workspace.
   *
   * This is a convenience endpoint that does not use the underlying Language Servers
   * directly, but it does apply the same filtering.
   */
  listFiles(options?: Core.RequestOptions): Core.APIPromise<WorkspaceListFilesResponse> {
    return this._client.get('/workspace-files', options);
  }

  /**
   * Search for symbols across the entire workspace
   *
   * Returns a list of symbols matching the given query string from all files in the
   * workspace.
   *
   * The returned positions point to the start of the symbol's identifier.
   *
   * e.g. for `User` on line 0 of `src/main.py`:
   *
   * ```
   * 0: class User:
   * _________^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * ```
   */
  searchSymbols(
    query: WorkspaceSearchSymbolsParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<Shared.SymbolResponse> {
    return this._client.get('/workspace-symbols', { query, ...options });
  }
}

export type WorkspaceListFilesResponse = Array<string>;

export interface WorkspaceSearchSymbolsParams {
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

export namespace Workspace {
  export import WorkspaceListFilesResponse = WorkspaceAPI.WorkspaceListFilesResponse;
  export import WorkspaceSearchSymbolsParams = WorkspaceAPI.WorkspaceSearchSymbolsParams;
}
