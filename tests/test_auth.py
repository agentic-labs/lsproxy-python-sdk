"""Unit tests for the authentication utilities."""
import base64
import json
import pytest
from lsproxy.auth import create_jwt, base64url_encode

# Test fixtures and utility functions
@pytest.fixture
def sample_payload():
    return {
        "sub": "test-subject",
        "iat": 1516239022,
        "exp": 1516239122
    }

@pytest.fixture
def sample_secret():
    return "test-secret-key-123"


def test_base64url_encode():
    """Test base64url encoding function."""
    # Test basic string encoding
    assert base64url_encode("hello") == "aGVsbG8"
    
    # Test padding removal
    assert not base64url_encode("hello world").endswith("=")
    
    # Test URL-safe characters
    encoded = base64url_encode("?test+/=")
    assert "+" not in encoded
    assert "/" not in encoded
    assert "=" not in encoded


def test_create_jwt_structure(sample_payload, sample_secret):
    """Test JWT token structure."""
    # Create token
    token = create_jwt(sample_payload, sample_secret)
    
    # Verify token has three parts (header.payload.signature)
    parts = token.split(".")
    assert len(parts) == 3
    
    # Verify each part is base64url encoded
    for part in parts:
        assert "+" not in part
        assert "/" not in part
        assert "=" not in part


def test_create_jwt_payload(sample_payload, sample_secret):
    """Test JWT payload contents."""
    # Create token
    token = create_jwt(sample_payload, sample_secret)
    
    # Verify payload encoding
    payload_part = token.split(".")[1]
    # Add padding for base64 decoding
    padding = "=" * ((4 - len(payload_part) % 4) % 4)
    decoded_payload = json.loads(base64.urlsafe_b64decode(payload_part + padding))
    
    # Verify decoded payload matches input
    assert decoded_payload["sub"] == sample_payload["sub"]
    assert decoded_payload["iat"] == sample_payload["iat"]
    assert decoded_payload["exp"] == sample_payload["exp"]


def test_create_jwt_invalid_payload():
    """Test JWT creation with invalid payload."""
    # Test with non-dict payload
    with pytest.raises(TypeError, match="Payload must be a dictionary"):
        create_jwt("invalid", "secret")
    
    # Test with empty payload
    with pytest.raises(ValueError, match="Payload cannot be empty"):
        create_jwt({}, "secret")


def test_create_jwt_invalid_secret():
    """Test JWT creation with invalid secret."""
    payload = {"sub": "test"}
    
    # Test with empty secret
    with pytest.raises(ValueError, match="Secret cannot be empty"):
        create_jwt(payload, "")
    
    # Test with non-string secret
    with pytest.raises(TypeError, match="Secret must be a string"):
        create_jwt(payload, 123)
