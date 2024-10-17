// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as ReferencesAPI from './references';

export class References extends APIResource {
  /**
   * Find all references to a symbol
   *
   * Returns a list of locations where the symbol at the given position is
   * referenced.
   */
  list(query: ReferenceListParams, options?: Core.RequestOptions): Core.APIPromise<Reference> {
    return this._client.get('/references', { query, ...options });
  }
}

export interface Reference {
  /**
   * The references to the symbol. Points to the start position of the symbol's
   * identifier.
   *
   * e.g. for the references of `User` on line 0 character 6 of `src/main.py` with
   * the code:
   *
   * ```
   * 0: class User:
   * _________^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * _________^
   * 6:
   * 7: print(user.name)
   * ```
   *
   * The references will be `[{"path": "src/main.py", "line": 5, "character": 7}]`.
   */
  references: Array<Reference.Reference>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
   */
  raw_response?: unknown | null;
}

export namespace Reference {
  /**
   * Specific position within a file.
   */
  export interface Reference {
    character: number;

    line: number;

    path: string;
  }
}

export interface ReferenceListParams {
  /**
   * The position within the file to get the references for. This should point to the
   * identifier of the definition.
   *
   * e.g. for getting the references of `User` on line 0 of `src/main.py` with the
   * code:
   *
   * ```
   * 0: class User:
   * _________^^^^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * ```
   */
  symbol_identifier_position: ReferenceListParams.SymbolIdentifierPosition;

  /**
   * Whether to include the declaration (definition) of the symbol in the response.
   * Defaults to false.
   */
  include_declaration?: boolean;

  /**
   * Whether to include the raw response from the langserver in the response.
   * Defaults to false.
   */
  include_raw_response?: boolean;
}

export namespace ReferenceListParams {
  /**
   * The position within the file to get the references for. This should point to the
   * identifier of the definition.
   *
   * e.g. for getting the references of `User` on line 0 of `src/main.py` with the
   * code:
   *
   * ```
   * 0: class User:
   * _________^^^^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * ```
   */
  export interface SymbolIdentifierPosition {
    character: number;

    line: number;

    path: string;
  }
}

export namespace References {
  export import Reference = ReferencesAPI.Reference;
  export import ReferenceListParams = ReferencesAPI.ReferenceListParams;
}
