from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.conf.settings import settings

engine = create_async_engine(settings.sqlalchemy_database_uri)
async_session = sessionmaker(None, expire_on_commit=False, class_=AsyncSession)
