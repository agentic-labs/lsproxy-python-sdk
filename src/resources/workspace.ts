// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../resource';
import * as Core from '../core';
import * as WorkspaceAPI from './workspace';

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
}

export type WorkspaceListFilesResponse = Array<string>;

export namespace Workspace {
  export import WorkspaceListFilesResponse = WorkspaceAPI.WorkspaceListFilesResponse;
}
