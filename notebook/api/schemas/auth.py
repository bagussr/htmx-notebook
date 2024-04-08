from pydantic import BaseModel, EmailStr
from fastapi import Form


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    @classmethod
    def validate(cls, email: EmailStr = Form(...), password: str = Form(...)):
        return cls(email=email, password=password)


class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @classmethod
    def validate(
        cls,
        name: str = Form(...),
        email: EmailStr = Form(...),
        password: str = Form(...),
    ):
        return cls(name=name, email=email, password=password)
