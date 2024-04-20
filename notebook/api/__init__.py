from fastapi import APIRouter

from api.routes.auth import router as auth_router
from api.routes.notes import router as notes_router

router = APIRouter(prefix="/api")

router.include_router(auth_router)
router.include_router(notes_router)
