from pydantic import BaseModel, Field, EmailStr


class UserCreateSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserSchema(BaseModel):
    id: int
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        orm_mode = True
