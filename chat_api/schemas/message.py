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
    source: Optional[ContentSourceEnum]

    @root_validator(pre=True)
    def validate_content(cls, values):
        type = values.get('type')
        if type == "text":
            if 'text' not in values:
                raise ValueError('text content requires extra field: [text]')
        elif type == "image":
            if 'url' not in values and 'height' not in values and 'width' not in values:
                raise ValueError('image content requires extra field: [height, width, url]')
        elif type == "video":
            if 'url' not in values and 'source' not in values:
                raise ValueError('video content requires extra field: [source, url]')
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
