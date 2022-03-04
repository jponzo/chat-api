from fastapi import APIRouter, HTTPException, Depends, FastAPI
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from chat_api.models.message import MessageModel
from chat_api.schemas.message import MessageSchema, MessageCreateSchema
from typing import List
from fastapi import Body, status
from chat_api.cruds.message import MessageCrud
import logging
from chat_api.core.config import settings
from chat_api.db.sql import get_db_client
from sqlalchemy.orm import Session


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_description="Create new message", response_model=MessageSchema)
def create_message(message: MessageCreateSchema = Body(...), db: Session = Depends(get_db_client)):
    created_message = MessageCrud.create(db, message)
    return created_message


@router.get(
    "/", response_description="Get messages", response_model=List[MessageSchema]
)
def get_by_recipient(recipient_id: str, message_start_id: str, limit: int = 100, db: Session = Depends(get_db_client)):
    messages = MessageCrud.get_messages_by_recipient(db, recipient_id, message_start_id, limit)
    return messages


@router.get(
    "/{id}", response_description="Get a single message", response_model=MessageSchema
)
def get_message(id: str, db: Session = Depends(get_db_client)):
    message = MessageCrud.get(db, id)
    if message:
        return message

    raise HTTPException(status_code=404, detail=f"Message {id} not found")
