import secrets
import uuid
from typing import Union

from fastapi import APIRouter, Header, HTTPException, status, Depends
from models import *

def validate_api_key() -> bool:
    return True


admin = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(validate_api_key)])





@admin.get("/")
async def root():
    return {"message": "Hello World"}

@admin.post("/register_app", response_model=RegisterAppResponse)
async def register_app(request: RegisterAppRequest) -> RegisterAppResponse:
    app_id = str(uuid.uuid4())
    def generate_api_key():
        return "bm_live_" + app_id + secrets.token_urlsafe(32)
    api_key = generate_api_key()
    # TODO: Store app details in database
    return RegisterAppResponse(app_id=app_id, name=request.name, api_key=api_key, message="App registered successfully")

@admin.delete("/delete_app", response_model=DeleteAppResponse)
async def delete_app(x_api_key: str = Header(..., alias="X-API-Key")) -> DeleteAppResponse:
    _, app_id, _ = x_api_key.split("_")
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid API key")
    # TODO: Delete app from database
    return DeleteAppResponse(message="App deleted successfully")

@admin.post("/add_api_key", response_model=AddAPIKeyResponse)
async def add_api_key(x_api_key: str = Header(..., alias="X-API-Key")) -> AddAPIKeyResponse:
    _, app_id, _ = x_api_key.split("_")
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid API key")
    def generate_api_key():
        return "bm_live_" + app_id + secrets.token_urlsafe(32)
    new_api_key = generate_api_key()
    # TODO: Store api key in database
    return AddAPIKeyResponse(api_key=generate_api_key(), message="API key added successfully")

@admin.delete("/delete_api_key/{api_key_to_delete}", response_model=DeleteAPIKeyResponse)
def delete_api_key(request: DeleteAPIKeyRequest ,api_key_to_delete: str, x_api_key: str = Header(..., alias="X-API-Key")) -> DeleteAPIKeyResponse:
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid API key")
    #TODO: Delete api key from db
    return DeleteAPIKeyResponse(message="API key deleted successfully")


@admin.post("/validate_api_key", response_model=ValidateAPIKeyResponse)
async def validate_api_key(x_api_key: str = Header(..., alias="X-API-Key")):
    return ValidateAPIKeyResponse(valid=await validate_api_key(x_api_key))


@admin.get("/rules/")
async def rules():
    pass
