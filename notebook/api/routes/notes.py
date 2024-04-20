from fastapi import APIRouter, Request

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/")
def notes(request: Request):

    return request.query_params.get("search")
