import json
import httpx
import time
from typing import List, TYPE_CHECKING, Optional

# Only import type hints for Modal if type checking
if TYPE_CHECKING:
    import modal

from .models import (
    DefinitionResponse,
    FileRange,
    ReadSourceCodeResponse,
    ReferencesResponse,
    GetDefinitionRequest,
    GetReferencesRequest,
    Symbol,
)


class Lsproxy:
    """Client for interacting with the lsproxy API."""

    # Shared HTTP client with connection pooling
    _client = httpx.Client(
        base_url="http://localhost:4444/v1",
        timeout=10,
        headers={"Content-Type": "application/json"},
        limits=httpx.Limits(max_keepalive_connections=20, max_connections=100),
    )

    def __init__(
        self, base_url: str = "http://localhost:4444/v1", timeout: float = 10.0,
        auth_token: Optional[str] = None
    ):
        self._client.base_url = base_url
        self._client.timeout = timeout
        headers = {"Content-Type": "application/json"}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        self._client.headers = headers
        
    def _request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        """Make HTTP request with retry logic and better error handling."""
        try:
            response = self._client.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                error_data = e.response.json()
                raise ValueError(error_data.get("error", str(e)))
            raise

    def definitions_in_file(self, file_path: str) -> List[Symbol]:
        """Retrieve symbols from a specific file."""
        response = self._request(
            "GET", "/symbol/definitions-in-file", params={"file_path": file_path}
        )
        symbols = [
            Symbol.model_validate(symbol_dict)
            for symbol_dict in json.loads(response.text)
        ]
        return symbols

    def find_definition(self, request: GetDefinitionRequest) -> DefinitionResponse:
        """Get the definition of a symbol at a specific position in a file."""
        response = self._request(
            "POST", "/symbol/find-definition", json=request.model_dump()
        )
        definition = DefinitionResponse.model_validate_json(response.text)
        return definition

    def find_references(self, request: GetReferencesRequest) -> ReferencesResponse:
        """Find all references to a symbol."""
        response = self._request(
            "POST", "/symbol/find-references", json=request.model_dump()
        )
        references = ReferencesResponse.model_validate_json(response.text)
        return references

    def list_files(self) -> List[str]:
        """Get a list of all files in the workspace."""
        response = self._request("GET", "/workspace/list-files")
        files = response.json()
        return files


    def read_source_code(self, request: FileRange) -> ReadSourceCodeResponse:
        """Read source code from a specified file range."""
        response = self._request("POST", "/workspace/read-source-code", json=request.model_dump())
        return ReadSourceCodeResponse.model_validate_json(response.text)

    @classmethod
    def initialize_with_modal(cls, repo_url: str, wait_time: float = 5.0) -> "Lsproxy":
        """
        Initialize lsproxy by starting a Modal sandbox with the server and connecting to it.
        
        Args:
            repo_url: Git repository URL to clone and analyze
            wait_time: Time to wait for server startup in seconds
        
        Returns:
            Configured Lsproxy client instance
            
        Raises:
            ImportError: If Modal is not installed
        """
        try:
            import modal
            import jwt
            import secrets
        except ImportError:
            raise ImportError(
                "Modal and PyJWT are required for this feature. "
                "Install them with: pip install 'lsproxy-sdk[modal]'"
            )

        app = modal.App.lookup("my-app", create_if_missing=True)

        # Generate a secure random secret
        jwt_secret = secrets.token_urlsafe(32)
        
        # Create JWT token
        token = jwt.encode(
            {"sub": "lsproxy-client", "iat": int(time.time())},
            jwt_secret,
            algorithm="HS256"
        )

        lsproxy_image = modal.Image.from_registry("agenticlabs/lsproxy-modal:latest").env({
            "JWT_SECRET": jwt_secret
        })

        with modal.enable_output():
            sandbox = modal.Sandbox.create(
                image=lsproxy_image,
                app=app,
                encrypted_ports=[4444],
            )
        
        tunnel_url = sandbox.tunnels()[4444].url
        
        # Clone repository
        p = sandbox.exec("git", "clone", repo_url, "/mnt/workspace")
        for line in p.stderr:
            print(line, end="")
        
        # Start lsproxy
        p = sandbox.exec("lsproxy")

        print(f"Waiting {wait_time} seconds for startup")
        
        # Wait for server to start
        time.sleep(wait_time)
        
        # Create client instance connected to tunnel
        client = cls(base_url=f"{tunnel_url}/v1", auth_token=token)
        
        # Store sandbox reference for cleanup
        client._sandbox = sandbox
        
        return client

    def close(self):
        """Close the HTTP client and cleanup Modal resources if present."""
        self._client.close()
        if hasattr(self, '_sandbox'):
            self._sandbox.terminate()
