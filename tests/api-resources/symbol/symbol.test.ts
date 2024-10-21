// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import Lsproxy from 'lsproxy';
import { Response } from 'node-fetch';

const client = new Lsproxy({ baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010' });

describe('resource symbol', () => {
  test('findDefinition: only required params', async () => {
    const responsePromise = client.symbol.findDefinition({
      position: { path: 'src/main.py', position: { character: 5, line: 10 } },
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('findDefinition: required and optional params', async () => {
    const response = await client.symbol.findDefinition({
      position: { path: 'src/main.py', position: { character: 5, line: 10 } },
      include_raw_response: false,
      include_source_code: false,
    });
  });

  test('findReferences: only required params', async () => {
    const responsePromise = client.symbol.findReferences({
      symbol_identifier_position: { path: 'src/main.py', position: { character: 5, line: 10 } },
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  test('findReferences: required and optional params', async () => {
    const response = await client.symbol.findReferences({
      symbol_identifier_position: { path: 'src/main.py', position: { character: 5, line: 10 } },
      include_code_context_lines: 5,
      include_declaration: true,
      include_raw_response: false,
    });
  });
});
