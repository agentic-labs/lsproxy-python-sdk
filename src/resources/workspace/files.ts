// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as Core from '../../core';
import * as FilesAPI from './files';

export class Files extends APIResource {
  /**
   * Get a list of all files in the workspace
   *
   * Returns an array of file paths for all files in the current workspace.
   *
   * This is a convenience endpoint that does not use the underlying Language Servers
   * directly, but it does apply the same filtering.
   */
  list(options?: Core.RequestOptions): Core.APIPromise<FileListResponse> {
    return this._client.get('/workspace/list-files', options);
  }
}

export type FileListResponse = Array<string>;

export namespace Files {
  export import FileListResponse = FilesAPI.FileListResponse;
}
