from geoalchemy2.functions import ST_AsGeoJSON
from sqlalchemy import select, func

from app.models.field import Field


class FieldService:
    MODEL = Field

    def __init__(self, session):
        self.session = session

    async def get_nearby_fields(self, query_point, radius, crop):
        stmt = (
            select(
                self.MODEL.id,
                self.MODEL.crop,
                self.MODEL.productivity,
                self.MODEL.area_ha,
                self.MODEL.history,
                self.MODEL.region,
                self.MODEL.score,
                ST_AsGeoJSON(self.MODEL.coordinates),
            )
            .where(func.ST_DWithin(self.MODEL.coordinates, func.ST_GeogFromText(query_point), radius))
        )
        if crop:
            stmt = stmt.where(self.MODEL.crop == crop)
        nearby_fields = await self.session.execute(stmt)
        return nearby_fields.fetchall()
