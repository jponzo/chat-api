from fastapi import APIRouter, HTTPException, Depends
from chat_api.schemas.user import UserSchema, UserCreateSchema, UserLoginSchema
from typing import List
from fastapi import Body
from chat_api.cruds.user import UserCrud
import logging
from chat_api.db.sql import get_db_client
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from chat_api.auth.auth_handler import signJWT

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/", response_description="health-check", status_code=200
)
def health():
    return {"status": "ok"}
