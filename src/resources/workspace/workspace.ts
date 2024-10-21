// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../resource';
import * as FilesAPI from './files';

export class Workspace extends APIResource {
  files: FilesAPI.Files = new FilesAPI.Files(this._client);
}

export namespace Workspace {
  export import Files = FilesAPI.Files;
  export import FileListResponse = FilesAPI.FileListResponse;
}
