// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as FileSymbolsAPI from './file-symbols';
import * as Shared from './shared';

export class FileSymbols extends APIResource {
  /**
   * Get symbols in a specific file
   *
   * Returns a list of symbols (functions, classes, variables, etc.) defined in the
   * specified file.
   */
  list(query: FileSymbolListParams, options?: Core.RequestOptions): Core.APIPromise<Shared.SymbolResponse> {
    return this._client.get('/file-symbols', { query, ...options });
  }
}

export interface FileSymbolListParams {
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

export namespace FileSymbols {
  export import FileSymbolListParams = FileSymbolsAPI.FileSymbolListParams;
}
