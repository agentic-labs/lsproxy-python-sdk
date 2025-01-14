import time
import json
import hashlib
import subprocess

from typing import TYPE_CHECKING
from .auth import create_jwt

# Only import type hints for Modal if type checking
if TYPE_CHECKING:
    import modal

def create_named_modal_secret(
    env: dict[str, str | None],
    secret_name: str,
):
    """
    modal secret create [OPTIONS] SECRET_NAME KEYVALUES...

    SECRET_NAME: [required]
    KEYVALUES...: Space-separated KEY=VALUE items [required]

    1) filter out None values
    2) stable JSON stringify
    3) take SHA256 hash of the string to get the SECRET_NAME
    4) assemble KEYVALUES using shlex.quote

    """
    try:
        import modal
    except ImportError:
        raise ImportError(
            "Modal and PyJWT are required for this feature. "
            "Install them with: pip install 'lsproxy-sdk[modal]'"
        )
    filtered_env = {k: v for k, v in env.items() if v is not None}

    # subprocess.run already handles quoting
    keyvalues = [f"{k}={v}" for k, v in filtered_env.items()]
    print(f"Creating Modal secret {secret_name} with {len(keyvalues)} keyvalues")
    result = subprocess.run(
        ["modal", "secret", "create", "--force", secret_name, *keyvalues],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise Exception(f"Error creating Modal secret {secret_name}: {result.stderr}")
    return modal.Secret.from_name(secret_name)

class ModalSandbox:
    def __init__(self, repo_url: str, git_token: str, sha: str, timeout: int, version: str):
        try:
            import modal
            import secrets
        except ImportError:
            raise ImportError(
                "Modal and PyJWT are required for this feature. "
                "Install them with: pip install 'lsproxy-sdk[modal]'"
            )

        app = modal.App.lookup("lsproxy-app", create_if_missing=True)

        # Generate a secure random secret
        jwt_secret = secrets.token_urlsafe(32)

        # Create JWT token with 24-hour expiration
        payload = {
            "sub": "lsproxy-client",
            "iat": int(time.time()),
            "exp": int(time.time()) + 86400,  # 24 hour expiration
        }
        self.jwt_token = create_jwt(payload, jwt_secret)


        if git_token:
            # We want the github secret to be named, because that allows us to cache the layers (for the same sha) even as the token changes!
            repo_id = hashlib.md5(repo_url.encode()).hexdigest()
            gh_secret = create_named_modal_secret(
                {"GITHUB_IAT": git_token},
                f"gh-iat-token-{repo_id}"
            )
            url_parts = repo_url.split("://")
            lsproxy_image = modal.Image.from_registry(f"agenticlabs/lsproxy:{version}")
            lsproxy_image = lsproxy_image.run_commands(
                [
                    "git config --global --add safe.directory /mnt/workspace",
                    f"git clone --depth 1 {url_parts[0]}://x-access-token:$GITHUB_IAT@{url_parts[1]} /mnt/workspace"
                ],
                secrets=[
                    gh_secret
                ],  # sneaky, cache the layers (for the same sha) even as the token changes!
            )
            if sha:
                lsproxy_image = lsproxy_image.run_commands([
                        f"cd /mnt/workspace && git fetch origin {sha} && git checkout {sha}"
                    ]
                )
        else:
            lsproxy_image = modal.Image.from_registry(f"agenticlabs/lsproxy:{version}").run_commands(
                [
                    f"git clone --depth 1 {repo_url} /mnt/workspace"
                ]
            )

        jwt_secret = modal.Secret.from_dict({"JWT_SECRET": jwt_secret})
        sandbox_config = {
            "image": lsproxy_image,
            "app": app,
            "encrypted_ports": [4444],
            "secrets": [jwt_secret],
        }

        if timeout is not None:
            sandbox_config["timeout"] = timeout

        print("Starting sandbox...")

        self.sandbox = modal.Sandbox.create(**sandbox_config)
        self.tunnel_url = self.sandbox.tunnels()[4444].url

        # Start lsproxy
        p = self.sandbox.exec(f"lsproxy")
    
    def terminate(self):
        self.sandbox.terminate()
