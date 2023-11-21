from fastapi import FastAPI

from app.conf.db import async_session, engine
from app.models.field import metadata


def init_db() -> None:
    """Init database"""
    async_session.configure(bind=engine)
    metadata.bind = engine


def create_app() -> FastAPI:
    init_db()
    app = FastAPI(
        title='Geometry Service',
    )
    return app
