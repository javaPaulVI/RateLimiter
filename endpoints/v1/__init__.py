import secrets
from typing import Union


from fastapi import APIRouter, HTTPException, status, Header
import uuid
from middleware.auth import validate_api_key, sha256
from endpoints.v1.models import *
db=...

V1 = APIRouter(prefix="/v1")





