// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as SymbolsAPI from './symbols';
import * as Shared from './shared';

export class Symbols extends APIResource {
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
  definitionsInFile(
    query: SymbolDefinitionsInFileParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<Shared.SymbolResponse> {
    return this._client.get('/file-symbols', { query, ...options });
  }

  /**
   * Get the definition of a symbol at a specific position in a file
   *
   * Returns the location of the definition for the symbol at the given position.
   *
   * The input position should point inside the symbol's identifier, e.g.
   *
   * The returned position points to the identifier of the symbol, and the file_path
   * from workspace root
   *
   * e.g. for the definition of `User` on line 5 of `src/main.py` with the code:
   *
   * ```
   * 0: class User:
   * output___^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * input_____^^^^
   * ```
   */
  findDefinition(
    body: SymbolFindDefinitionParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<DefinitionResponse> {
    return this._client.post('/definition', { body, ...options });
  }

  /**
   * Find all references to a symbol
   *
   * The input position should point to the identifier of the symbol you want to get
   * the references for.
   *
   * Returns a list of locations where the symbol at the given position is
   * referenced.
   *
   * The returned positions point to the start of the reference identifier.
   *
   * e.g. for `User` on line 0 of `src/main.py`:
   *
   * ```
   * 0: class User:
   * input____^^^^
   * 1:     def __init__(self, name, age):
   * 2:         self.name = name
   * 3:         self.age = age
   * 4:
   * 5: user = User("John", 30)
   * output____^
   * ```
   */
  findReferences(body: SymbolFindReferencesParams, options?: Core.RequestOptions): Core.APIPromise<unknown> {
    return this._client.post('/references', { body, ...options });
  }
}

/**
 * Response to a definition request.
 *
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
export interface DefinitionResponse {
  definitions: Array<Shared.Position>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
   */
  raw_response?: unknown | null;
}

/**
 * Response to a references request.
 *
 * Points to the start position of the symbol's identifier.
 *
 * e.g. for the references of `User` on line 0 character 6 of `src/main.py` with
 * the code:
 *
 * ```
 * 0: class User:
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
export interface ReferencesResponse {
  references: Array<Shared.Position>;

  /**
   * The raw response from the langserver.
   *
   * https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
   */
  raw_response?: unknown | null;
}

export type SymbolFindReferencesResponse = unknown;

export interface SymbolDefinitionsInFileParams {
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

export interface SymbolFindDefinitionParams {
  /**
   * Specific position within a file.
   */
  position: Shared.Position;

  /**
   * Whether to include the raw response from the langserver in the response.
   * Defaults to false.
   */
  include_raw_response?: boolean;
}

export interface SymbolFindReferencesParams {
  /**
   * Specific position within a file.
   */
  symbol_identifier_position: Shared.Position;

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

export namespace Symbols {
  export import DefinitionResponse = SymbolsAPI.DefinitionResponse;
  export import ReferencesResponse = SymbolsAPI.ReferencesResponse;
  export import SymbolFindReferencesResponse = SymbolsAPI.SymbolFindReferencesResponse;
  export import SymbolDefinitionsInFileParams = SymbolsAPI.SymbolDefinitionsInFileParams;
  export import SymbolFindDefinitionParams = SymbolsAPI.SymbolFindDefinitionParams;
  export import SymbolFindReferencesParams = SymbolsAPI.SymbolFindReferencesParams;
}
