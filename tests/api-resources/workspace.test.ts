// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import Lsproxy from 'lsproxy';
import { Response } from 'node-fetch';

const client = new Lsproxy({ baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010' });

describe('resource workspace', () => {
  test('listFiles', async () => {
    const responsePromise = client.workspace.listFiles();
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('listFiles: request options instead of params are passed correctly', async () => {
    // ensure the request options are being passed correctly by passing an invalid HTTP method in order to cause an error
    await expect(client.workspace.listFiles({ path: '/_stainless_unknown_path' })).rejects.toThrow(
      Lsproxy.NotFoundError,
    );
  });

  test('searchSymbols: only required params', async () => {
    const responsePromise = client.workspace.searchSymbols({ query: 'query' });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('searchSymbols: required and optional params', async () => {
    const response = await client.workspace.searchSymbols({ query: 'query', include_raw_response: true });
  });
});
