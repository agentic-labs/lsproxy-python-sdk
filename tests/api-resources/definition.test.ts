// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import Lsproxy from 'lsproxy';
import { Response } from 'node-fetch';

const client = new Lsproxy({ baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010' });

describe('resource definition', () => {
  test('get: only required params', async () => {
    const responsePromise = client.definition.get({
      position: { character: 5, line: 10, path: 'src/main.py' },
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('get: required and optional params', async () => {
    const response = await client.definition.get({
      position: { character: 5, line: 10, path: 'src/main.py' },
      include_raw_response: true,
    });
  });
});