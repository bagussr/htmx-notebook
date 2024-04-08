from fastapi import APIRouter, Request, status

from app import templates

router = APIRouter(prefix="", tags=["app"])


@router.get("/login")
def login(reqeust: Request):
    return templates.TemplateResponse("login.html", {"request": reqeust})


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/home")
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
