from pydantic import BaseModel
from typing_extensions import Literal


class CheckUserRequest(BaseModel):
    user_id: str

class CheckUserResponse(BaseModel):
    allowed: bool
    remaining: int
    retry_after: float
    limit: int
    time_period: str
    strategy: str


class RegisterAppRequest(BaseModel):
    name: str

class RegisterAppResponse(BaseModel):
    app_id: str
    name: str
    admin_api_key: str
    live_api_key: str
    message: str



class AddAPIKeyRequest(BaseModel):
    pass

class AddAPIKeyResponse(BaseModel):
    api_key: str
    message: str



class DeleteAPIKeyRequest(BaseModel):
    pass

class DeleteAPIKeyResponse(BaseModel):
    message: str



class DeleteAppRequest(BaseModel):
    app_id: str

class DeleteAppResponse(BaseModel):
    message: str



class ValidateAPIKeyRequest(BaseModel):
    pass

class ValidateAPIKeyResponse(BaseModel):
    valid: bool


class GetRulesRequest(BaseModel):
    pass

class GetRulesResponse(BaseModel):
    rules: dict


class RegisterTokenBuckerUserRequest(BaseModel):
    strategy: Literal["token_bucket"]
    api_key: str
    user_id: str
    refill_rate: float
    limit: int

class RegisterFixedWindowUserRequest(BaseModel):
    strategy: Literal["fixed_window"]
    api_key: str
    user_id: str
    limit: int
    period: Literal["secondly","minutely", "hourly", "daily", "weekly", "monthly", "yearly"]

class RegisterSlidingWindowUserRequest(BaseModel):
    strategy: Literal["sliding_window"]
    api_key: str
    user_id: str
    limit: int
    window_secs: int

