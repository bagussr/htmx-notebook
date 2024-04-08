from typing import Any
from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.responses import JSONResponse, RedirectResponse

from api.schemas.auth import LoginSchema
from api.schemas.users import UsersSchema
from app.models import MongoController
from app.models.users import Users
from utils.password import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

controller = MongoController("users", Users)


@router.post("/login", response_model=Users)
async def post_login(data: LoginSchema = Depends(LoginSchema.validate)) -> Response:
    user: Users = await controller.filter_by("email", data.email)
    if user is not None:
        if verify_password(data.password, user.password):
            return RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)
        return JSONResponse(
            content="Password tidak valid", status_code=status.HTTP_400_BAD_REQUEST
        )
    return JSONResponse(
        content="Akun tidak ditemukan", status_code=status.HTTP_404_NOT_FOUND
    )


@router.post("/register")
async def post_register(
    request: Request, data: UsersSchema = Depends(UsersSchema.validate)
) -> Any:
    res = await controller.insert(data.model_dump())
    if res:
        return RedirectResponse(url="/register", status_code=status.HTTP_303_SEE_OTHER)
    return JSONResponse(content="BAD REQUEST", status_code=status.HTTP_400_BAD_REQUEST)
