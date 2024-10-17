// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as DefinitionAPI from './definition';
import * as Shared from './shared';

export class Definition extends APIResource {
  /**
   * Get the definition of a symbol at a specific position in a file
   *
   * Returns the location of the definition for the symbol at the given position.
   */
  get(query: DefinitionGetParams, options?: Core.RequestOptions): Core.APIPromise<DefinitionResponse> {
    return this._client.get('/definition', { query, ...options });
  }
}

/**
 * Response to a definition request.
 */
export interface DefinitionResponse {
  /**
   * The definition(s) of the symbol. Points to the start position of the symbol's
   * identifier.
   *
   * e.g. for the definition of `User` on line 5 of `src/main.py` with the code:
   *
   * ```
   * 0: class User:
   * _________^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * __________^
   * ```
   *
   * The definition(s) will be
   * `[{"path": "src/main.py", "line": 0, "character": 6}]`.
   */
  definitions: Array<Shared.FilePosition>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
   */
  raw_response?: unknown | null;
}

export interface DefinitionGetParams {
  /**
   * The position within the file to get the definition for. This should point to the
   * identifier of the symbol you want to get the definition for.
   *
   * e.g. for getting the definition of `User` on line 10 of `src/main.py` with the
   * code:
   *
   * ```
   * 0: class User:
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * __________^^^
   * ```
   *
   * The (line, char) should be anywhere in (5, 7)-(5, 11).
   */
  position: Shared.FilePosition;

  /**
   * Whether to include the raw response from the langserver in the response.
   * Defaults to false.
   */
  include_raw_response?: boolean;
}

export namespace Definition {
  export import DefinitionResponse = DefinitionAPI.DefinitionResponse;
  export import DefinitionGetParams = DefinitionAPI.DefinitionGetParams;
}
