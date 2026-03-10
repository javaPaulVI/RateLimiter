from fastapi import Header, Request

def validate_api_key(request: Request) -> bool:
    return True

def get_admin_api_key(request: Request, x_api_key_admin: str = Header(..., alias="X-API-Key-Admin")):
    return x_api_key_admin

def get_live_api_key(request: Request, x_api_key_live: str = Header(..., alias="X-API-Key-Live")):
    return x_api_key_live
