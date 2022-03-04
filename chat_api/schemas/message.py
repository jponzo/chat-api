from pydantic import BaseModel, Field, EmailStr
from enum import Enum


# class MessageTypeEnum(str, Enum):
#     text = 'text'
#     image = 'image'
#     video = "video"
#
#
# class ThisMessageSchema(BaseModel):
#     type: MessageTypeEnum = Field(...)
#     text: str = Field(...)

class MessageCreateSchema(BaseModel):
    sender: int = Field(...)
    recipient: int = Field(...)
    message: str = Field(...)


class MessageSchema(BaseModel):
    id: int
    sender: int = Field(...)
    recipient: int = Field(...)
    message: str = Field(...)
    # message: ThisMessageModel = Field(...)

    class Config:
        orm_mode = True
