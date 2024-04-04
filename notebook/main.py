from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.routes import router
from api import router as api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="./notebook/static"), name="static")


@app.get("/")
def index():
    return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)


app.include_router(router)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
