from typing import Any
from jose import jwt
from datetime import datetime, timedelta
import pytz
import os

from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.responses import (
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    HTMLResponse,
)

from api.schemas.auth import LoginSchema
from api.schemas.users import UsersSchema
from app.models import MongoController
from app.models.users import Users
from utils.password import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

controller = MongoController("users", Users)


@router.post("/logout")
def logout():
    res = RedirectResponse(
        url="/login",
        status_code=status.HTTP_303_SEE_OTHER,
    )
    res.delete_cookie("token")
    return res


@router.post("/login", response_model=Users)
async def post_login(
    q: str = None, data: LoginSchema = Depends(LoginSchema.validate)
) -> Response:
    user: Users = await controller.filter_by("email", data.email)
    if user is not None:
        if verify_password(data.password, user.password):
            res = RedirectResponse(
                url="/home",
                status_code=status.HTTP_303_SEE_OTHER,
                headers={"HX-Push-Url": q or "/home"},
            )
            token = jwt.encode(
                {
                    "id": user.id,
                    "exp": (datetime.now(tz=pytz.timezone("Asia/Jakarta")))
                    + timedelta(days=os.environ.get("EXPIRED_TOKEN", 7)),
                },
                os.environ.get("SECRET_KEY", "sambala"),
                algorithm="HS256",
            )
            res.set_cookie("token", token)
            return res
        return HTMLResponse(
            """<p
            class="bg-red-300 text-red-600 mb-2 rounded p-1"
          >Password tidak valid</p>""",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return HTMLResponse(
        """<p
            class="bg-red-300 text-red-600 mb-2 rounded p-1"
          >Akun tidak ditemukan</p>""",
        status_code=status.HTTP_404_NOT_FOUND,
    )


@router.post("/register")
async def post_register(
    request: Request, data: UsersSchema = Depends(UsersSchema.validate)
) -> Any:
    res = await controller.insert(data.model_dump())
    if res:
        return RedirectResponse(url="/register", status_code=status.HTTP_303_SEE_OTHER)
    return JSONResponse(content="BAD REQUEST", status_code=status.HTTP_400_BAD_REQUEST)
