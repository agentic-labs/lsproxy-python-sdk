"""Unit tests for the lsproxy client."""
import json
import pytest
from unittest.mock import ANY, patch

from lsproxy.client import Lsproxy
from lsproxy.models import (
    Position,
    FilePosition,
    FileRange,
    Symbol,
    DefinitionResponse,
    GetDefinitionRequest,
    ReferencesResponse,
    GetReferencesRequest,
    ReadSourceCodeResponse,
)


@pytest.fixture
def mock_request():
    """Mock the httpx request."""
    with patch("httpx.Client.request") as mock:
        mock.return_value = mock.Mock()
        mock.return_value.status_code = 200
        # Ensure the mock preserves the headers from the client
        def side_effect(*args, **kwargs):
            # Preserve the actual request behavior for verification
            mock.return_value.request_args = args
            mock.return_value.request_kwargs = kwargs
            return mock.return_value
        mock.side_effect = side_effect
        yield mock


@pytest.fixture
def client():
    """Create a test client."""
    return Lsproxy(base_url="http://test.url", auth_token="test_token")


def test_definitions_in_file(client, mock_request):
    """Test getting definitions in a file."""
    response_data = [
        {
            "kind": "function",
            "name": "test_func",
            "identifier_position": {
                "path": "test.py",
                "position": {"line": 1, "character": 4}
            },
            "range": {
                "path": "test.py",
                "start": {"line": 1, "character": 0},
                "end": {"line": 3, "character": 12}
            }
        }
    ]
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    result = client.definitions_in_file("test.py")
    assert len(result) == 1
    assert isinstance(result[0], Symbol)
    assert result[0].kind == "function"
    assert result[0].name == "test_func"
    assert result[0].identifier_position.path == "test.py"
    assert result[0].identifier_position.position.line == 1
    assert result[0].identifier_position.position.character == 4

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args.args
    kwargs = mock_request.call_args.kwargs
    assert args[0] == "GET"
    assert args[1] == "/symbol/definitions-in-file"
    assert kwargs["params"] == {"file_path": "test.py"}
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_find_definition(client, mock_request):
    """Test finding a definition."""
    response_data = {
        "definitions": [
            {
                "path": "test.py",
                "position": {"line": 5, "character": 2}
            }
        ],
        "source_code_context": [
            {
                "range": {
                    "path": "test.py",
                    "start": {"line": 5, "character": 0},
                    "end": {"line": 5, "character": 15}
                },
                "source_code": "def test_func():"
            }
        ],
        "raw_response": {"some": "raw_data"}
    }
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    request = GetDefinitionRequest(
        position=FilePosition(path="test.py", position=Position(line=10, character=8)),
        include_raw_response=True,
        include_source_code=True
    )
    result = client.find_definition(request)

    assert isinstance(result, DefinitionResponse)
    assert len(result.definitions) == 1
    assert result.definitions[0].path == "test.py"
    assert result.definitions[0].position.line == 5
    assert result.raw_response == {"some": "raw_data"}
    assert len(result.source_code_context) == 1
    assert result.source_code_context[0].source_code == "def test_func():"

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args[0]
    kwargs = mock_request.call_args[1]
    assert args[0] == "POST"
    assert args[1] == "/symbol/find-definition"
    assert kwargs["json"] == {
        "position": {
            "path": "test.py",
            "position": {"line": 10, "character": 8}
        },
        "include_raw_response": True,
        "include_source_code": True
    }
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_find_references(client, mock_request):
    """Test finding references."""
    response_data = {
        "references": [
            {
                "path": "test.py",
                "position": {"line": 15, "character": 4}
            }
        ],
        "context": [
            {
                "range": {
                    "path": "test.py",
                    "start": {"line": 15, "character": 0},
                    "end": {"line": 15, "character": 20}
                },
                "source_code": "    result = test_func()"
            }
        ],
        "raw_response": {"some": "raw_data"}
    }
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    request = GetReferencesRequest(
        identifier_position=FilePosition(path="test.py", position=Position(line=5, character=4)),
        include_code_context_lines=2,
        include_declaration=True,
        include_raw_response=True
    )
    result = client.find_references(request)

    assert isinstance(result, ReferencesResponse)
    assert len(result.references) == 1
    assert result.references[0].path == "test.py"
    assert result.references[0].position.line == 15
    assert result.raw_response == {"some": "raw_data"}
    assert len(result.context) == 1
    assert result.context[0].source_code == "    result = test_func()"

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args[0]
    kwargs = mock_request.call_args[1]
    assert args[0] == "POST"
    assert args[1] == "/symbol/find-references"
    assert kwargs["json"] == {
        "identifier_position": {
            "path": "test.py",
            "position": {"line": 5, "character": 4}
        },
        "include_code_context_lines": 2,
        "include_declaration": True,
        "include_raw_response": True
    }
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_list_files(client, mock_request):
    """Test listing files."""
    response_data = ["file1.py", "file2.py"]
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    result = client.list_files()
    assert result == ["file1.py", "file2.py"]

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args[0]
    kwargs = mock_request.call_args[1]
    assert args[0] == "GET"
    assert args[1] == "/workspace/list-files"
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_read_source_code(client, mock_request):
    """Test reading source code."""
    response_data = {
        "source_code": "def test_func():\n    pass\n"
    }
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    file_range = FileRange(
        path="test.py",
        start=Position(line=1, character=0),
        end=Position(line=2, character=8)
    )
    result = client.read_source_code(file_range)

    assert isinstance(result, ReadSourceCodeResponse)
    assert result.source_code == "def test_func():\n    pass\n"

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args[0]
    kwargs = mock_request.call_args[1]
    assert args[0] == "POST"
    assert args[1] == "/workspace/read-source-code"
    assert kwargs["json"] == {
        "range": {
            "path": "test.py",
            "start": {"line": 1, "character": 0},
            "end": {"line": 2, "character": 8}
        }
    }
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_check_health(client, mock_request):
    """Test health check."""
    response_data = {
        "status": "ok",
        "languages": ["python", "typescript_javascript", "rust", "cpp", "java", "golang", "php"]
    }
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    result = client.check_health()
    assert result["status"] == "ok"
    assert set(result["languages"]) == {
        "python", "typescript_javascript", "rust", "cpp", "java", "golang", "php"
    }

    # Verify the request was made with correct method, endpoint, and parameters
    mock_request.assert_called_once()
    args = mock_request.call_args[0]
    kwargs = mock_request.call_args[1]
    assert args[0] == "GET"
    assert args[1] == "/health"
    assert kwargs["headers"] == {"Content-Type": "application/json", "Authorization": "Bearer test_token"}


def test_error_responses(client, mock_request):
    """Test error responses."""
    # Test 400 Bad Request
    mock_request.return_value.status_code = 400
    response_data = {"error": "Invalid request"}
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    with pytest.raises(ValueError) as exc_info:
        client.definitions_in_file("test.py")
    assert str(exc_info.value) == "Invalid request"

    # Test 500 Internal Server Error
    mock_request.return_value.status_code = 500
    response_data = {"error": "Internal server error"}
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    with pytest.raises(RuntimeError) as exc_info:
        client.definitions_in_file("test.py")
    assert str(exc_info.value) == "Internal server error"


def test_authentication_headers(client, mock_request):
    """Test that authentication headers are included in requests."""
    mock_request.return_value.json.return_value = []
    client.definitions_in_file("test.py")
    
    mock_request.assert_called_once_with(
        ANY,
        ANY,
        params=ANY,
        headers={"Authorization": "Bearer test_token"}
    )


def test_missing_token():
    """Test that missing auth token raises an error."""
    with pytest.raises(ValueError) as exc_info:
        Lsproxy(base_url="http://test.url", auth_token="")
    assert "token cannot be empty" in str(exc_info.value).lower()

    with pytest.raises(ValueError) as exc_info:
        Lsproxy(base_url="http://test.url", auth_token=None)
    assert "token cannot be none" in str(exc_info.value).lower()


def test_authentication_error(client, mock_request):
    """Test authentication error response."""
    mock_request.return_value.status_code = 401
    response_data = {"error": "Invalid or expired token"}
    mock_request.return_value.text = json.dumps(response_data)
    mock_request.return_value.json.return_value = response_data

    with pytest.raises(ValueError) as exc_info:
        client.definitions_in_file("test.py")
    assert "invalid or expired token" in str(exc_info.value).lower()
