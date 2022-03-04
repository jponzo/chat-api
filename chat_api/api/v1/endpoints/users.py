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


@router.post("/", response_description="Add new user", response_model=UserSchema)
def create_user(user: UserCreateSchema = Body(...), db: Session = Depends(get_db_client)):
    try:
        created_user = UserCrud.create(db, user)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail={"message": e.orig.args})
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
    user = UserCrud.get_user_by_id(db, id)
    if user:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")


@router.post("/login")
def user_login(user: UserLoginSchema = Body(...), db: Session = Depends(get_db_client)):
    if UserCrud.login(db, user.email, user.password):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
