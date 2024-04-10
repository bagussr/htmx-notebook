import json
from typing import Annotated, Any
from bson import ObjectId
from jose import jwt
import os

from fastapi.responses import RedirectResponse
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import APIKeyCookie

from app.models import MongoController
from app.models.users import Users

security = APIKeyCookie(name="token", scheme_name="Bearer", auto_error=False)


async def cookie_auth(request: Request, token: str = Depends(security)):
    controller = MongoController("users", Users)
    if token is None:
        url = str(request.url).split(str(request.base_url))[1]
        raise HTTPException(
            status_code=302,
            detail="Not authorized",
            headers={"Location": f"/login?q={url}"},
        )
    credentials = jwt.decode(
        token=token, key=os.environ.get("SECRET_KEY", "sambala"), algorithms=["HS256"]
    )
    user = await controller.filter_by("id", ObjectId(json.loads(credentials["id"])))
    return user


async def authenticated(token: str = Depends(security)):
    if token:
        return True
    return False


CookieAuth = Annotated[Users, Depends(cookie_auth)]
Authenticated = Annotated[Any, Depends(authenticated)]
