"""Unit tests for authentication utilities."""
import pytest
import jwt
from datetime import datetime, timedelta, timezone

from lsproxy.auth import create_jwt, base64url_encode


@pytest.fixture
def sample_payload():
    """Create a sample JWT payload."""
    return {
        "sub": "test-user",
        "exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
    }


@pytest.fixture
def sample_secret():
    """Create a sample secret key."""
    return "test-secret-key-1234"


def test_base64url_encode():
    """Test base64url encoding."""
    # Test basic encoding
    assert base64url_encode(b"test") == "dGVzdA"
    
    # Test padding removal
    assert base64url_encode(b"t") == "dA"
    assert base64url_encode(b"te") == "dGU"
    assert base64url_encode(b"tes") == "dGVz"
    
    # Test URL-safe characters
    assert "+" not in base64url_encode(b"???")
    assert "/" not in base64url_encode(b"???")


def test_create_jwt(sample_payload, sample_secret):
    """Test JWT creation."""
    token = create_jwt(sample_payload, sample_secret)
    
    # Verify token structure
    assert isinstance(token, str)
    assert len(token.split(".")) == 3
    
    # Verify token can be decoded
    decoded = jwt.decode(token, sample_secret, algorithms=["HS256"])
    assert decoded["sub"] == sample_payload["sub"]
    assert decoded["exp"] == sample_payload["exp"]




def test_create_jwt_invalid_payload():
    """Test JWT creation with invalid payload."""
    with pytest.raises(TypeError):
        create_jwt("not a dict", "secret")
    
    with pytest.raises(ValueError):
        create_jwt({}, "secret")  # Empty payload


def test_create_jwt_invalid_secret():
    """Test JWT creation with invalid secret."""
    payload = {"sub": "test"}
    
    with pytest.raises(ValueError):
        create_jwt(payload, "")  # Empty secret
    
    with pytest.raises(TypeError):
        create_jwt(payload, None)  # None secret
