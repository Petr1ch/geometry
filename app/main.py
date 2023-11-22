from fastapi import FastAPI

from app.conf.db import async_session, engine
from app.endpoints import fields
from app.models.field import metadata

PREFIX: str = "/api"


def init_db() -> None:
    """Init database"""
    async_session.configure(bind=engine)
    metadata.bind = engine


def init_routes(app: FastAPI) -> None:
    """Connect routes to app"""
    app.include_router(fields.router, prefix=PREFIX, tags=["Base"])


def create_app() -> FastAPI:
    init_db()
    app = FastAPI(
        title="Geometry Service",
    )
    init_routes(app)
    return app
