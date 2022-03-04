from fastapi import APIRouter, HTTPException, Depends, FastAPI
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from chat_api.models.user import UserModel
from chat_api.schemas.user import UserSchema, UserCreateSchema
from typing import List
from fastapi import Body, status
from chat_api.cruds.user import UserCrud
import logging
from chat_api.core.config import settings
from chat_api.db.sql import get_db_client
from sqlalchemy.orm import Session


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_description="Add new user", response_model=UserSchema)
def create_user(user: UserCreateSchema = Body(...), db: Session = Depends(get_db_client)):
    created_user = UserCrud.create(db, user)
    return created_user


@router.get(
    "/", response_description="List all users", response_model=List[UserSchema]
)
def list_users(db: Session = Depends(get_db_client)):
    users = UserCrud.list(db)
    return users


@router.get(
    "/{id}", response_description="Get a single user", response_model=UserSchema
)
def get_user(id: str, db: Session = Depends(get_db_client)):
    user = UserCrud.get(db, id)
    if user:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")
