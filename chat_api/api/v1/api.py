from fastapi import APIRouter
from chat_api.api.v1.endpoints import users, messages, health
from chat_api.auth.auth_bearer import JWTBearer
from chat_api.auth.auth_handler import signJWT

api_router = APIRouter()
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
