from fastapi import APIRouter
from chat_api.api.v1.endpoints import messages, users

api_router = APIRouter()
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
