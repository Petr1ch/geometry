import typing as t

from geoalchemy2.functions import ST_AsGeoJSON
from shapely import Polygon
from sqlalchemy import select, func

from app.models.field import Field


class FieldService:
    MODEL = Field

    def __init__(self, session):
        self.session = session

    async def get_nearby_fields(
        self, query_point: str, radius: float, crop: t.Optional[str]
    ) -> t.List:
        stmt = select(
            self.MODEL.id,
            self.MODEL.crop,
            self.MODEL.productivity,
            self.MODEL.area_ha,
            self.MODEL.history,
            self.MODEL.region,
            self.MODEL.score,
            ST_AsGeoJSON(self.MODEL.coordinates),
        ).where(
            func.ST_DWithin(
                self.MODEL.coordinates, func.ST_GeogFromText(query_point), radius
            )
        )
        if crop:
            stmt = stmt.where(self.MODEL.crop == crop)
        nearby_fields = await self.session.execute(stmt)
        return nearby_fields.fetchall()

    async def get_fields_in_parallelogram(
        self, parallelogram: Polygon, crop: t.Optional[str]
    ) -> t.List:
        stmt = select(
            self.MODEL.id,
            self.MODEL.crop,
            self.MODEL.productivity,
            self.MODEL.area_ha,
            self.MODEL.history,
            self.MODEL.region,
            self.MODEL.score,
            ST_AsGeoJSON(self.MODEL.coordinates),
        ).filter(func.ST_Within(Field.coordinates, func.ST_GeomFromText(parallelogram)))
        if crop:
            stmt = stmt.where(self.MODEL.crop == crop)
        fields_in_parallelogram = await self.session.execute(stmt)
        return fields_in_parallelogram.fetchall()

    async def get_fields_intersecting_geometry(
        self, figure: Polygon, crop: t.Optional[str]
    ) -> t.List:
        stmt = select(
            self.MODEL.id,
            self.MODEL.crop,
            self.MODEL.productivity,
            self.MODEL.area_ha,
            self.MODEL.history,
            self.MODEL.region,
            self.MODEL.score,
            ST_AsGeoJSON(self.MODEL.coordinates),
        ).filter(func.ST_Intersects(Field.coordinates, func.ST_GeomFromText(figure)))
        if crop:
            stmt = stmt.where(self.MODEL.crop == crop)
        fields_intersecting_geometry = await self.session.execute(stmt)
        return fields_intersecting_geometry.fetchall()

    async def get_agricultural_metrics(self, region: str) -> t.List:
        stmt = (
            select(
                func.sum(Field.area_ha).label("total_area"),
                func.sum(Field.productivity * Field.area_ha).label("total_yield"),
                func.coalesce(
                    func.sum(Field.productivity * Field.area_ha)
                    / func.sum(Field.area_ha),
                    0,
                ).label("average_yield"),
            )
            .filter(Field.region == region)
            .group_by(Field.region)
        )

        result = await self.session.execute(stmt)
        metrics = result.fetchone()
        return metrics
