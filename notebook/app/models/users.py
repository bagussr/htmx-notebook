from typing import ClassVar
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models import PyObjectId
from utils.types import OptionalStr


class Users(BaseModel):
    id: PyObjectId = Field(None, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    phone: OptionalStr = Field(default=None)
    address: OptionalStr = Field(default=None)
    img_profile: OptionalStr = Field(default=None)
    password: str = Field(...)

    model_config = ConfigDict(
        arbitrary_types_allowed=True, json_encoders={ObjectId: str}
    )
