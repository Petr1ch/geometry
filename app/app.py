from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from app.conf.db import async_session
from app.conf.settings import Settings, settings
from app.models.field import metadata


def init_db(app_settings: Settings) -> None:
    """Init database"""
    engine = create_async_engine(app_settings.sqlalchemy_database_uri)
    async_session.configure(bind=engine)
    metadata.bind = engine


def create_app(app_settings: Settings = settings) -> FastAPI:
    init_db(app_settings)
    app = FastAPI(
        title='Geometry Service',
    )
    return app
