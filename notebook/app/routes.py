from fastapi import APIRouter, Cookie, Depends, Request, status
from fastapi.responses import RedirectResponse


from app import templates
from utils.auth import Authenticated, CookieAuth


router = APIRouter(prefix="", tags=["app"])


@router.get("/login")
def login(reqeust: Request, auth: Authenticated):
    if auth:
        return RedirectResponse(url="/notes", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("login.html", {"request": reqeust})


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/notes")
def home(request: Request, auth: CookieAuth):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "subtiltle": "Notes"}
    )


@router.get("/favorite")
def home(request: Request, auth: CookieAuth):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "subtiltle": "Favorite Notes"}
    )
