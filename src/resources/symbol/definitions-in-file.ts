// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as Core from '../../core';
import * as DefinitionsInFileAPI from './definitions-in-file';
import * as SymbolAPI from './symbol';

export class DefinitionsInFile extends APIResource {
  /**
   * Get symbols in a specific file
   *
   * Returns a list of symbols (functions, classes, variables, etc.) defined in the
   * specified file.
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
  list(
    query: DefinitionsInFileListParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<SymbolAPI.SymbolResponse> {
    return this._client.get('/symbol/definitions-in-file', { query, ...options });
  }
}

export interface DefinitionsInFileListParams {
  /**
   * The path to the file to get the symbols for, relative to the root of the
   * workspace.
   */
  file_path: string;

  /**
   * Whether to include the raw response from the langserver in the response.
   * Defaults to false.
   */
  include_raw_response?: boolean;
}

export namespace DefinitionsInFile {
  export import DefinitionsInFileListParams = DefinitionsInFileAPI.DefinitionsInFileListParams;
}
