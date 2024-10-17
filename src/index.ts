// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import * as Errors from './error';
import * as Uploads from './uploads';
import { type Agent } from './_shims/index';
import * as qs from './internal/qs';
import * as Core from './core';
import * as API from './resources/index';

export interface ClientOptions {
  /**
   * URL of the lsproxy server
   */
  baseURL?: string | undefined;

  /**
   * Override the default base URL for the API, e.g., "https://api.example.com/v2/"
   *
   * Defaults to process.env['LSPROXY_BASE_URL'].
   */
  baseURL?: string | null | undefined;

  /**
   * The maximum amount of time (in milliseconds) that the client should wait for a response
   * from the server before timing out a single request.
   *
   * Note that request timeouts are retried by default, so in a worst-case scenario you may wait
   * much longer than this timeout before the promise succeeds or fails.
   */
  timeout?: number;

  /**
   * An HTTP agent used to manage HTTP(S) connections.
   *
   * If not provided, an agent will be constructed by default in the Node.js environment,
   * otherwise no agent is used.
   */
  httpAgent?: Agent;

  /**
   * Specify a custom `fetch` function implementation.
   *
   * If not provided, we use `node-fetch` on Node.js and otherwise expect that `fetch` is
   * defined globally.
   */
  fetch?: Core.Fetch | undefined;

  /**
   * The maximum number of times that the client will retry a request in case of a
   * temporary failure, like a network error or a 5XX error from the server.
   *
   * @default 2
   */
  maxRetries?: number;

  /**
   * Default headers to include with every request to the API.
   *
   * These can be removed in individual requests by explicitly setting the
   * header to `undefined` or `null` in request options.
   */
  defaultHeaders?: Core.Headers;

  /**
   * Default query parameters to include with every request to the API.
   *
   * These can be removed in individual requests by explicitly setting the
   * param to `undefined` in request options.
   */
  defaultQuery?: Core.DefaultQuery;
}

/**
 * API Client for interfacing with the Lsproxy API.
 */
export class Lsproxy extends Core.APIClient {
  baseURL: string;

  private _options: ClientOptions;

  /**
   * API Client for interfacing with the Lsproxy API.
   *
   * @param {string | undefined} [opts.baseURL=process.env['LSPROXY_BASE_URL'] ?? undefined]
   * @param {string} [opts.baseURL=process.env['LSPROXY_BASE_URL'] ?? /v1] - Override the default base URL for the API.
   * @param {number} [opts.timeout=1 minute] - The maximum amount of time (in milliseconds) the client will wait for a response before timing out.
   * @param {number} [opts.httpAgent] - An HTTP agent used to manage HTTP(s) connections.
   * @param {Core.Fetch} [opts.fetch] - Specify a custom `fetch` function implementation.
   * @param {number} [opts.maxRetries=2] - The maximum number of times the client will retry a request.
   * @param {Core.Headers} opts.defaultHeaders - Default headers to include with every request to the API.
   * @param {Core.DefaultQuery} opts.defaultQuery - Default query parameters to include with every request to the API.
   */
  constructor({
    baseURL = Core.readEnv('LSPROXY_BASE_URL'),
    baseURL = Core.readEnv('LSPROXY_BASE_URL'),
    ...opts
  }: ClientOptions = {}) {
    if (baseURL === undefined) {
      throw new Errors.LsproxyError(
        "The LSPROXY_BASE_URL environment variable is missing or empty; either provide it, or instantiate the Lsproxy client with an baseURL option, like new Lsproxy({ baseURL: 'http://localhost:4444' }).",
      );
    }

    const options: ClientOptions = {
      baseURL,
      ...opts,
      baseURL: baseURL || `/v1`,
    };

    super({
      baseURL: options.baseURL!,
      timeout: options.timeout ?? 60000 /* 1 minute */,
      httpAgent: options.httpAgent,
      maxRetries: options.maxRetries,
      fetch: options.fetch,
    });

    this._options = options;

    this.baseURL = baseURL;
  }

  definition: API.Definition = new API.Definition(this);
  fileSymbols: API.FileSymbols = new API.FileSymbols(this);
  references: API.References = new API.References(this);
  workspaceFiles: API.WorkspaceFiles = new API.WorkspaceFiles(this);
  workspaceSymbols: API.WorkspaceSymbols = new API.WorkspaceSymbols(this);

  protected override defaultQuery(): Core.DefaultQuery | undefined {
    return this._options.defaultQuery;
  }

  protected override defaultHeaders(opts: Core.FinalRequestOptions): Core.Headers {
    return {
      ...super.defaultHeaders(opts),
      ...this._options.defaultHeaders,
    };
  }

  protected override stringifyQuery(query: Record<string, unknown>): string {
    return qs.stringify(query, { arrayFormat: 'comma' });
  }

  static Lsproxy = this;
  static DEFAULT_TIMEOUT = 60000; // 1 minute

  static LsproxyError = Errors.LsproxyError;
  static APIError = Errors.APIError;
  static APIConnectionError = Errors.APIConnectionError;
  static APIConnectionTimeoutError = Errors.APIConnectionTimeoutError;
  static APIUserAbortError = Errors.APIUserAbortError;
  static NotFoundError = Errors.NotFoundError;
  static ConflictError = Errors.ConflictError;
  static RateLimitError = Errors.RateLimitError;
  static BadRequestError = Errors.BadRequestError;
  static AuthenticationError = Errors.AuthenticationError;
  static InternalServerError = Errors.InternalServerError;
  static PermissionDeniedError = Errors.PermissionDeniedError;
  static UnprocessableEntityError = Errors.UnprocessableEntityError;

  static toFile = Uploads.toFile;
  static fileFromPath = Uploads.fileFromPath;
}

export const {
  LsproxyError,
  APIError,
  APIConnectionError,
  APIConnectionTimeoutError,
  APIUserAbortError,
  NotFoundError,
  ConflictError,
  RateLimitError,
  BadRequestError,
  AuthenticationError,
  InternalServerError,
  PermissionDeniedError,
  UnprocessableEntityError,
} = Errors;

export import toFile = Uploads.toFile;
export import fileFromPath = Uploads.fileFromPath;

export namespace Lsproxy {
  export import RequestOptions = Core.RequestOptions;

  export import Definition = API.Definition;
  export import DefinitionResponse = API.DefinitionResponse;
  export import DefinitionGetParams = API.DefinitionGetParams;

  export import FileSymbols = API.FileSymbols;
  export import FileSymbolListParams = API.FileSymbolListParams;

  export import References = API.References;
  export import ReferenceResponse = API.ReferenceResponse;
  export import ReferenceListParams = API.ReferenceListParams;

  export import WorkspaceFiles = API.WorkspaceFiles;
  export import WorkspaceFileListResponse = API.WorkspaceFileListResponse;

  export import WorkspaceSymbols = API.WorkspaceSymbols;
  export import WorkspaceSymbolListParams = API.WorkspaceSymbolListParams;

  export import FilePosition = API.FilePosition;
  export import SymbolResponse = API.SymbolResponse;
}

export default Lsproxy;
