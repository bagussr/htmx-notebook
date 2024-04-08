from pydantic import BaseModel, field_serializer
from fastapi import Form

from utils.types import OptionalStr, PasswordStr, RequiredEmail, RequiredStr


class UsersSchema(BaseModel):
    name: RequiredStr
    email: RequiredEmail
    phone: OptionalStr
    address: OptionalStr
    img_profile: OptionalStr
    password: PasswordStr

    @field_serializer("password", when_used="always")
    def dump_secret(self, value):
        return value.get_secret_value()

    @classmethod
    def validate(
        cls,
        name: RequiredStr = Form(...),
        email: RequiredEmail = Form(...),
        phone: OptionalStr = Form(None),
        address: OptionalStr = Form(None),
        img_profile: OptionalStr = Form(None),
        password: RequiredStr = Form(...),
    ):
        return cls(
            name=name,
            email=email,
            phone=phone,
            address=address,
            img_profile=img_profile,
            password=password,
        )
