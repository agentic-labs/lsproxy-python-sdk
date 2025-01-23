import json
import httpx
import time
import asyncio
from typing import List, Optional

from .models import (
    DefinitionResponse,
    FileRange,
    ReadSourceCodeResponse,
    ReferencesResponse,
    GetDefinitionRequest,
    GetReferencesRequest,
    Symbol,
    FindIdentifierRequest,
    IdentifierResponse,
    GetReferencedSymbolsRequest,
    ReferencedSymbolsResponse,
)

class AsyncLsproxy:
    """Async client for interacting with the lsproxy API."""

    def __init__(
        self,
        base_url: str = "http://localhost:4444/v1",
        timeout: float = 60.0,
        auth_token: Optional[str] = None,
    ):
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers={"Content-Type": "application/json"},
            limits=httpx.Limits(max_keepalive_connections=20, max_connections=100),
        )
        headers = {"Content-Type": "application/json"}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        self._client.headers = headers

    async def _request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        """Make HTTP request with retry logic and better error handling."""
        try:
            response = await self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                error_data = e.response.json()
                raise ValueError(error_data.get("error", str(e)))
            raise

    async def definitions_in_file(self, file_path: str) -> List[Symbol]:
        """Retrieve symbols from a specific file."""
        response = await self._request(
            "GET", "/symbol/definitions-in-file", params={"file_path": file_path}
        )
        symbols = [
            Symbol.model_validate(symbol_dict)
            for symbol_dict in json.loads(response.text)
        ]
        return symbols

    async def find_definition(self, request: GetDefinitionRequest) -> DefinitionResponse:
        """Get the definition of a symbol at a specific position in a file."""
        if not isinstance(request, GetDefinitionRequest):
            raise TypeError(
                f"Expected GetDefinitionRequest, got {type(request).__name__}. Please use GetDefinitionRequest model to construct the request."
            )
        response = await self._request(
            "POST", "/symbol/find-definition", json=request.model_dump()
        )
        definition = DefinitionResponse.model_validate_json(response.text)
        return definition

    async def find_references(self, request: GetReferencesRequest) -> ReferencesResponse:
        """Find all references to a symbol."""
        if not isinstance(request, GetReferencesRequest):
            raise TypeError(
                f"Expected GetReferencesRequest, got {type(request).__name__}. Please use GetReferencesRequest model to construct the request."
            )
        response = await self._request(
            "POST", "/symbol/find-references", json=request.model_dump()
        )
        references = ReferencesResponse.model_validate_json(response.text)
        return references

    async def find_identifier(self, request: FindIdentifierRequest) -> IdentifierResponse:
        """Find all occurrences of an identifier by name in a file."""
        if not isinstance(request, FindIdentifierRequest):
            raise TypeError(
                f"Expected FindIdentifierRequest, got {type(request).__name__}. Please use FindIdentifierRequest model to construct the request."
            )
        response = await self._request(
            "POST", "/symbol/find-identifier", json=request.model_dump()
        )
        return IdentifierResponse.model_validate_json(response.text)

    async def list_files(self) -> List[str]:
        """Get a list of all files in the workspace."""
        response = await self._request("GET", "/workspace/list-files")
        files = response.json()
        return files

    async def read_source_code(self, request: FileRange) -> ReadSourceCodeResponse:
        """Read source code from a specified file range."""
        if not isinstance(request, FileRange):
            raise TypeError(
                f"Expected FileRange, got {type(request).__name__}. Please use FileRange model to construct the request."
            )
        response = await self._request(
            "POST", "/workspace/read-source-code", json=request.model_dump()
        )
        return ReadSourceCodeResponse.model_validate_json(response.text)

    @classmethod
    async def initialize_with_modal(
        cls,
        repo_url: str,
        git_token: Optional[str] = None,
        sha: Optional[str] = None,
        timeout: Optional[int] = None,
        version: str = "0.3.3",
    ) -> "AsyncLsproxy":
        """Initialize lsproxy by starting a Modal sandbox with the server and connecting to it."""
        try:
            from .modal import ModalSandbox
        except ImportError:
            raise ImportError(
                "Modal and PyJWT are required for this feature. "
                "Install them with: pip install 'lsproxy-sdk[modal]'"
            )

        sandbox = ModalSandbox(repo_url, git_token, sha, timeout, version)

        client = cls(base_url=f"{sandbox.tunnel_url}/v1", auth_token=sandbox.jwt_token)

        print("Waiting for server start up (make take a minute)...")
        for attempt in range(180):
            if await client.check_health():
                break
            await asyncio.sleep(1)
        else:
            raise TimeoutError("Server did not start up within 3 minutes")

        print("Server is ready to accept connections")
        client._sandbox = sandbox
        return client

    async def check_health(self) -> bool:
        """Check if the server is healthy and ready."""
        try:
            response = await self._request("GET", "/system/health")
            health_data = response.json()
            return health_data.get("status") == "ok"
        except Exception:
            return False

    async def find_referenced_symbols(
        self, request: GetReferencedSymbolsRequest
    ) -> ReferencedSymbolsResponse:
        """Find all symbols that are referenced from the symbol at the given position."""
        if not isinstance(request, GetReferencedSymbolsRequest):
            raise TypeError(
                f"Expected GetReferencedSymbolsRequest, got {type(request).__name__}. "
                "Please use GetReferencedSymbolsRequest model to construct the request."
            )
        
        response = await self._request(
            "POST", 
            "/symbol/find-referenced-symbols", 
            json=request.model_dump()
        )
        
        return ReferencedSymbolsResponse.model_validate_json(response.text)

    async def close(self):
        """Close the HTTP client and cleanup Modal resources if present."""
        await self._client.aclose()
        if hasattr(self, "_sandbox"):
            self._sandbox.terminate()

    async def __aenter__(self) -> "AsyncLsproxy":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
