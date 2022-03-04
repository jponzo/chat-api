from pydantic import BaseModel, Field, EmailStr
from enum import Enum
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MessageTypeEnum(str, Enum):
    text = 'text'
    image = 'image'
    video = "video"


class ThisMessageModel(BaseModel):
    type: MessageTypeEnum = Field(...)
    text: str = Field(...)


class MessageModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    sender: EmailStr = Field(...)
    recipient: EmailStr = Field(...)
    message: ThisMessageModel = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "al-api",
                "repository": "bitbucket.org/rappiinc/al-api",
                "type": "Experiments, Science, and Fashion in Nanophotonics"
            }
        }
