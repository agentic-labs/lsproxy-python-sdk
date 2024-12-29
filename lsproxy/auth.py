import base64
import hmac
import hashlib
import json


def base64url_encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    elif isinstance(data, dict):
        data = json.dumps(data, separators=(",", ":")).encode("utf-8")

    padding = b"="
    encoded = base64.b64encode(data).replace(b"+", b"-").replace(b"/", b"_")
    return encoded.rstrip(padding)


def create_jwt(payload, secret):
    # Create JWT header
    header = {"typ": "JWT", "alg": "HS256"}

    # Encode header and payload
    encoded_header = base64url_encode(header)
    encoded_payload = base64url_encode(payload)

    # Create signature
    signing_input = encoded_header + b"." + encoded_payload
    signature = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    encoded_signature = base64url_encode(signature)

    # Combine all parts
    jwt = signing_input + b"." + encoded_signature
    return jwt.decode("utf-8")
