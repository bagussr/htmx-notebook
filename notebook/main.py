from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.routes import router
from api import router as api_router
from utils.auth import Authenticated

app = FastAPI()

app.mount("/static", StaticFiles(directory="./notebook/static"), name="static")


@app.get("/")
def index(auth: Authenticated):
    if auth:
        return RedirectResponse("/notes", status_code=status.HTTP_303_SEE_OTHER)
    return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)


app.include_router(router)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
