import secrets
import uuid
from typing import Union
from core.dependencies import *

from fastapi import APIRouter, Header, HTTPException, status, Depends
from endpoints.v1.models import *



admin = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(validate_api_key)])





@admin.get("/")
async def root():
    return {"message": "Hello World"}

@admin.post("/register_app", response_model=RegisterAppResponse)
async def register_app(request: RegisterAppRequest) -> RegisterAppResponse:
    app_id = str(uuid.uuid4())
    def generate_api_key():
        return  app_id + secrets.token_urlsafe(32)
    live_api_key = "bm_live_" + generate_api_key()
    admin_api_key = "bm_admin_" + generate_api_key()
    # TODO: Store app details in database
    try:
        return RegisterAppResponse(app_id=app_id, name=request.name, api_key=api_key, message="App registered successfully")
    except:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Error, try again later")

@admin.delete("/delete_app", response_model=DeleteAppResponse)
async def delete_app(x_api_key: str = Header(..., alias="X-API-Key")) -> DeleteAppResponse:
    _, app_id, _ = x_api_key.split("_")
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid API key")
    # TODO: Delete app from database
    return DeleteAppResponse(message="App deleted successfully")


@admin.post("/validate_api_key", response_model=ValidateAPIKeyResponse)
async def validate_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    return ValidateAPIKeyResponse(valid=await validate_api_key(x_api_key))


@admin.get("/rules/")
async def rules():
    pass
