from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from chat_api.models.user import UserModel
from typing import List
from fastapi import Body, status
from chat_api.cruds.user import UserCrud
import logging
from chat_api.core.config import settings


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_description="Add new user", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):

    if await UserCrud.get(user.name):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": f"User {user.name} already exist"})
    user = jsonable_encoder(user)
    created_user = await UserCrud.create(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get(
    "/", response_description="List all users", response_model=List[UserModel]
)
async def list_users():
    users = await UserCrud.list()
    return users


@router.get(
    "/{id}", response_description="Get a single user", response_model=UserModel
)
async def get_user(id: str):
    user = await UserCrud.get(id)
    if user:
        return user

    raise HTTPException(status_code=404, detail=f"User {id} not found")
