"""Unit tests for the Lsproxy client."""
import json
import pytest
import httpx
from unittest.mock import patch, MagicMock
from lsproxy.client import Lsproxy
from lsproxy.models import (
    GetDefinitionRequest,
    GetReferencesRequest,
    Position,
    FilePosition,
)


@patch("lsproxy.client.httpx.Client.request")
def test_definitions_in_file_success(mock_request):
    """Test successful retrieval of definitions from a file."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps([
        {
            "name": "test_function",
            "kind": "function",
            "range": {
                "start": {"line": 1, "character": 0},
                "end": {"line": 1, "character": 12}
            },
            "selection_range": {
                "start": {"line": 1, "character": 0},
                "end": {"line": 1, "character": 12}
            }
        }
    ])
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act
    symbols = client.definitions_in_file("test.py")

    # Assert
    assert len(symbols) == 1
    assert symbols[0].name == "test_function"
    assert symbols[0].kind == "function"
    mock_request.assert_called_once_with(
        "GET",
        "/symbol/definitions-in-file",
        params={"file_path": "test.py"}
    )


@patch("lsproxy.client.httpx.Client.request")
def test_definitions_in_file_error(mock_request):
    """Test error handling when retrieving definitions fails."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "File not found"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Bad Request",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(ValueError, match="File not found"):
        client.definitions_in_file("nonexistent.py")


@patch("lsproxy.client.httpx.Client.request")
def test_find_definition_success(mock_request):
    """Test successful retrieval of a symbol definition."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({
        "definitions": [{
            "path": "test.py",
            "position": {
                "line": 10,
                "character": 4
            },
            "source_code": "def test_function():\n    pass",
            "context_lines": 2
        }]
    })
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    request = GetDefinitionRequest(
        position=FilePosition(
            path="test.py",
            position=Position(line=5, character=2)
        )
    )
    
    # Act
    response = client.find_definition(request)

    # Assert
    assert len(response.definitions) == 1
    assert response.definitions[0].path == "test.py"
    assert response.definitions[0].position.line == 10
    assert response.definitions[0].position.character == 4
    assert response.definitions[0].source_code == "def test_function():\n    pass"
    mock_request.assert_called_once_with(
        "POST",
        "/symbol/find-definition",
        json=request.model_dump()
    )


@patch("lsproxy.client.httpx.Client.request")
def test_find_definition_invalid_request(mock_request):
    """Test error handling when an invalid request type is provided."""
    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(TypeError, match="Expected GetDefinitionRequest"):
        client.find_definition({"invalid": "request"})


@patch("lsproxy.client.httpx.Client.request")
def test_find_definition_error(mock_request):
    """Test error handling when the server returns an error."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Invalid position"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Bad Request",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    request = GetDefinitionRequest(
        position=FilePosition(
            path="test.py",
            position=Position(line=5, character=2)
        )
    )
    
    # Act & Assert
    with pytest.raises(ValueError, match="Invalid position"):
        client.find_definition(request)


@patch("lsproxy.client.httpx.Client.request")
def test_find_references_success(mock_request):
    """Test successful retrieval of symbol references."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({
        "references": [{
            "path": "test.py",
            "position": {
                "line": 15,
                "character": 8
            },
            "source_code": "result = test_function()",
            "context_lines": 2,
            "is_declaration": False
        }]
    })
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    request = GetReferencesRequest(
        position=FilePosition(
            path="test.py",
            position=Position(line=5, character=2)
        )
    )
    
    # Act
    response = client.find_references(request)

    # Assert
    assert len(response.references) == 1
    assert response.references[0].path == "test.py"
    assert response.references[0].position.line == 15
    assert response.references[0].position.character == 8
    assert response.references[0].source_code == "result = test_function()"
    assert response.references[0].is_declaration is False
    mock_request.assert_called_once_with(
        "POST",
        "/symbol/find-references",
        json=request.model_dump()
    )


@patch("lsproxy.client.httpx.Client.request")
def test_find_references_invalid_request(mock_request):
    """Test error handling when an invalid request type is provided."""
    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(TypeError, match="Expected GetReferencesRequest"):
        client.find_references({"invalid": "request"})


@patch("lsproxy.client.httpx.Client.request")
def test_find_references_error(mock_request):
    """Test error handling when the server returns an error."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"error": "Symbol not found"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Bad Request",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    request = GetReferencesRequest(
        position=FilePosition(
            path="test.py",
            position=Position(line=5, character=2)
        )
    )
    
    # Act & Assert
    with pytest.raises(ValueError, match="Symbol not found"):
        client.find_references(request)


@patch("lsproxy.client.httpx.Client.request")
def test_list_files_success(mock_request):
    """Test successful retrieval of file list."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps([
        "src/main.py",
        "src/utils.py",
        "tests/test_main.py"
    ])
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act
    files = client.list_files()

    # Assert
    assert len(files) == 3
    assert "src/main.py" in files
    assert "src/utils.py" in files
    assert "tests/test_main.py" in files
    mock_request.assert_called_once_with(
        "GET",
        "/files/list"
    )


@patch("lsproxy.client.httpx.Client.request")
def test_list_files_error(mock_request):
    """Test error handling when the server returns an error."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "Internal server error"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Internal Server Error",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(ValueError, match="Internal server error"):
        client.list_files()


@patch("lsproxy.client.httpx.Client.request")
def test_read_source_code_success(mock_request):
    """Test successful retrieval of source code."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({
        "source_code": "def example():\n    return True\n",
        "context_lines": 2
    })
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act
    response = client.read_source_code("test.py")

    # Assert
    assert response.source_code == "def example():\n    return True\n"
    assert response.context_lines == 2
    mock_request.assert_called_once_with(
        "GET",
        "/files/read",
        params={"file_path": "test.py"}
    )


@patch("lsproxy.client.httpx.Client.request")
def test_read_source_code_error(mock_request):
    """Test error handling when the server returns an error."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"error": "File not found"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Not Found",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(ValueError, match="File not found"):
        client.read_source_code("nonexistent.py")


@patch("lsproxy.client.httpx.Client.request")
def test_check_health_success(mock_request):
    """Test successful health check."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"status": "healthy"})
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act
    is_healthy = client.check_health()

    # Assert
    assert is_healthy is True
    mock_request.assert_called_once_with(
        "GET",
        "/health"
    )


@patch("lsproxy.client.httpx.Client.request")
def test_check_health_unhealthy(mock_request):
    """Test unhealthy status response."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = json.dumps({"status": "unhealthy"})
    mock_request.return_value = mock_response

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act
    is_healthy = client.check_health()

    # Assert
    assert is_healthy is False


@patch("lsproxy.client.httpx.Client.request")
def test_check_health_error(mock_request):
    """Test error handling when health check fails."""
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "Internal server error"}
    mock_request.return_value = mock_response
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Internal Server Error",
        request=MagicMock(),
        response=mock_response
    )

    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(ValueError, match="Internal server error"):
        client.check_health()


def test_initialize_with_modal_no_modal():
    """Test initialize_with_modal when modal is not installed."""
    # Arrange
    client = Lsproxy(base_url="http://mocked.url")
    
    # Act & Assert
    with pytest.raises(ImportError, match="Modal is not installed"):
        client.initialize_with_modal()


@patch("lsproxy.client.modal")
def test_initialize_with_modal_success(mock_modal):
    """Test successful initialization with modal."""
    # Arrange
    mock_sandbox = MagicMock()
    mock_modal.Sandbox.return_value = mock_sandbox
    mock_sandbox.stub.lsproxy.run.return_value = {
        "url": "http://modal.sandbox.url",
        "jwt_secret": "test_secret"
    }

    client = Lsproxy()
    
    # Act
    client.initialize_with_modal()

    # Assert
    assert client.base_url == "http://modal.sandbox.url"
    assert client._jwt_secret == "test_secret"
    mock_modal.Sandbox.assert_called_once()
    mock_sandbox.stub.lsproxy.run.assert_called_once()


@patch("lsproxy.client.modal")
def test_initialize_with_modal_error(mock_modal):
    """Test error handling when modal initialization fails."""
    # Arrange
    mock_sandbox = MagicMock()
    mock_modal.Sandbox.return_value = mock_sandbox
    mock_sandbox.stub.lsproxy.run.side_effect = Exception("Modal initialization failed")

    client = Lsproxy()
    
    # Act & Assert
    with pytest.raises(ValueError, match="Failed to initialize Modal sandbox"):
        client.initialize_with_modal()
