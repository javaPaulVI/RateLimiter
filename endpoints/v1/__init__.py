import secrets
from typing import Union


from fastapi import APIRouter, HTTPException, status, Header
from endpoints.v1.models import *
import uuid
from middleware.auth import validate_api_key, sha256
import endpoints.v1.admin as admin
db=...

V1 = APIRouter(prefix="/v1")
V1.include_router(admin.admin)

@V1.post("/check")
async def check_user_limits(request: CheckUserRequest, x_api_key: str = Header(..., alias="X-API-Key")):
    





