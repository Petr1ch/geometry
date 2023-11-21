from fastapi import Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.endpoints.dependecies.db import get_db_session
from app.endpoints.services.field_service import FieldService


async def get_field_service(session: AsyncSession = Depends(get_db_session)):
    return FieldService(session)


def get_point(
        lat: float = Query(..., description="Latitude of the point"),
        lon: float = Query(..., description="Longitude of the point"),
) -> str:
    return f'POINT({lat} {lon})'
