import hashlib
import secrets

def hash_api_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

def generate_api_key(app_id: str) -> str:
    return secrets.token_urlsafe(32)