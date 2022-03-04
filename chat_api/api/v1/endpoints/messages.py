from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from chat_api.models.message import MessageModel
from typing import List
from fastapi import Body, status
from chat_api.cruds.message import MessageCrud
import logging
from chat_api.core.config import settings


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_description="Create new message", response_model=MessageModel)
async def create_message(message: MessageModel = Body(...)):
    message = jsonable_encoder(message)
    created_message = await MessageCrud.create(message)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_message)


@router.get(
    "/", response_description="Get messages", response_model=List[MessageModel]
)
async def get_by_recipient(recipient_id: str, message_start_id: str, limit: int = 100):
    messages = await MessageCrud.list()
    return messages


@router.get(
    "/{id}", response_description="Get a single message", response_model=MessageModel
)
async def get_message(id: str):
    message = await MessageCrud.get(id)
    if message:
        return message

    raise HTTPException(status_code=404, detail=f"Message {id} not found")
