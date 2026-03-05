import hashlib

async def validate_api_key(api_key: str) -> bool:
    return True

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()