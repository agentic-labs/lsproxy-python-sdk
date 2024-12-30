"""Unit tests for the lsproxy client."""
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
        yield mock


@pytest.fixture
def client():
    """Create a test client."""
    return Lsproxy(base_url="http://test.url", auth_token="test_token")


def test_definitions_in_file(client, mock_request):
    """Test getting definitions in a file."""
    mock_request.return_value.json.return_value = [
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

    result = client.definitions_in_file("test.py")
    assert len(result) == 1
    assert isinstance(result[0], Symbol)
    assert result[0].kind == "function"
    assert result[0].name == "test_func"
    assert result[0].identifier_position.path == "test.py"
    assert result[0].identifier_position.position.line == 1
    assert result[0].identifier_position.position.character == 4

    mock_request.assert_called_once_with(
        "GET",
        "/symbol/definitions-in-file",
        params={"file_path": "test.py"},
        headers={"Authorization": "Bearer test_token"}
    )


def test_find_definition(client, mock_request):
    """Test finding a definition."""
    mock_request.return_value.json.return_value = {
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

    mock_request.assert_called_once_with(
        "POST",
        "/symbol/find-definition",
        json={
            "position": {
                "path": "test.py",
                "position": {"line": 10, "character": 8}
            },
            "include_raw_response": True,
            "include_source_code": True
        },
        headers={"Authorization": "Bearer test_token"}
    )


def test_find_references(client, mock_request):
    """Test finding references."""
    mock_request.return_value.json.return_value = {
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

    mock_request.assert_called_once_with(
        "POST",
        "/symbol/find-references",
        json={
            "identifier_position": {
                "path": "test.py",
                "position": {"line": 5, "character": 4}
            },
            "include_code_context_lines": 2,
            "include_declaration": True,
            "include_raw_response": True
        },
        headers={"Authorization": "Bearer test_token"}
    )


def test_list_files(client, mock_request):
    """Test listing files."""
    mock_request.return_value.json.return_value = ["file1.py", "file2.py"]

    result = client.list_files()
    assert result == ["file1.py", "file2.py"]

    mock_request.assert_called_once_with(
        "GET",
        "/workspace/list-files",
        headers={"Authorization": "Bearer test_token"}
    )


def test_read_source_code(client, mock_request):
    """Test reading source code."""
    mock_request.return_value.json.return_value = {
        "source_code": "def test_func():\n    pass\n"
    }

    file_range = FileRange(
        path="test.py",
        start=Position(line=1, character=0),
        end=Position(line=2, character=8)
    )
    result = client.read_source_code(file_range)

    assert isinstance(result, ReadSourceCodeResponse)
    assert result.source_code == "def test_func():\n    pass\n"

    mock_request.assert_called_once_with(
        "POST",
        "/workspace/read-source-code",
        json={
            "range": {
                "path": "test.py",
                "start": {"line": 1, "character": 0},
                "end": {"line": 2, "character": 8}
            }
        },
        headers={"Authorization": "Bearer test_token"}
    )


def test_check_health(client, mock_request):
    """Test health check."""
    mock_request.return_value.json.return_value = {
        "status": "ok",
        "languages": ["python", "typescript_javascript", "rust", "cpp", "java", "golang", "php"]
    }

    result = client.check_health()
    assert result["status"] == "ok"
    assert set(result["languages"]) == {
        "python", "typescript_javascript", "rust", "cpp", "java", "golang", "php"
    }

    mock_request.assert_called_once_with(
        "GET",
        "/health",
        headers={"Authorization": "Bearer test_token"}
    )


def test_error_responses(client, mock_request):
    """Test error responses."""
    # Test 400 Bad Request
    mock_request.return_value.status_code = 400
    mock_request.return_value.json.return_value = {"error": "Invalid request"}

    with pytest.raises(ValueError) as exc_info:
        client.definitions_in_file("test.py")
    assert str(exc_info.value) == "Invalid request"

    # Test 500 Internal Server Error
    mock_request.return_value.status_code = 500
    mock_request.return_value.json.return_value = {"error": "Internal server error"}

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
    mock_request.return_value.json.return_value = {"error": "Invalid or expired token"}

    with pytest.raises(ValueError) as exc_info:
        client.definitions_in_file("test.py")
    assert "invalid or expired token" in str(exc_info.value).lower()
