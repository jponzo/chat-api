from pydantic import BaseModel, Field, root_validator
from enum import Enum
from typing import Optional





class ContentTypeEnum(str, Enum):
    text = 'text'
    image = 'image'
    video = "video"


class ContentSourceEnum(str, Enum):
    youtube = 'youtube'
    vimeo = 'vimeo'


class ContentSchema(BaseModel):
    type: str = Field(...)
    text: Optional[str]
    url: Optional[str]
    height: Optional[str]
    width: Optional[str]
    source: Optional[str]

    @root_validator(pre=True)
    def validate_content(cls, values):
        type = values.get('type')
        if type == "text":
            assert 'text' in values
        elif type == "image":
            assert 'url' in values and 'height' in values and 'width' in values
        elif type == "video":
            assert 'url' in values and 'source' in values
        return values

    class Config:
        orm_mode = True


class MessageCreateSchema(BaseModel):
    sender: int = Field(...)
    recipient: int = Field(...)
    content: ContentSchema = Field(...)

    class Config:
        orm_mode = True


class MessageSchema(BaseModel):
    id: int
    sender: int = Field(...)
    recipient: int = Field(...)
    content: ContentSchema = Field(...)

    class Config:
        orm_mode = True
