from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from app import templates

router = APIRouter(prefix="", tags=["app"])


@router.get("/login")
def login(reqeust: Request):
    return templates.TemplateResponse("login.html", {"request": reqeust})


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
