from fastapi import FastAPI

from app.core.config import settings
from app.models import user as _user_model  # noqa: F401 — register with Base.metadata
from app.routers import auth as auth_router
from app.routers import build as build_router
from app.routers import files as files_router
from app.routers import professor as professor_router

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
app.include_router(auth_router.router)
app.include_router(professor_router.router)
app.include_router(files_router.router)
app.include_router(build_router.router)


@app.get("/")
async def health_check():
    return {"status": "ok", "app": settings.APP_NAME}
