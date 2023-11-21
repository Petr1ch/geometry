import json
import geojson

from fastapi import APIRouter, Query
from geoalchemy2.functions import ST_AsGeoJSON
from sqlalchemy import select, func

from app.conf.db import async_session
from app.models.field import Field

router = APIRouter()


@router.get("/fields/nearby/")
async def get_nearby_fields(
        lat: float = Query(..., description="Latitude of the point"),
        lon: float = Query(..., description="Longitude of the point"),
        radius: float = Query(..., description="Radius in meters"),
):
    async with async_session() as session:
        query_point = f'POINT({lat} {lon})'  # 1.6669451 46.3516502
        stmt = (
            select(
                Field.id,
                Field.crop,
                Field.productivity,
                Field.area_ha,
                Field.history,
                Field.region,
                Field.score,
                ST_AsGeoJSON(Field.coordinates),
            )
            .where(func.ST_DWithin(Field.coordinates, func.ST_GeogFromText(query_point), radius))
        )
        nearby_fields = await session.execute(stmt)
        nearby_fields = nearby_fields.fetchall()

        features = []
        for row in nearby_fields:
            feature = geojson.Feature(
                geometry=json.loads(row[7]),
                properties={
                    'id': row[0],
                    'crop': row[1],
                    'productivity': row[2],
                    'area_ha': row[3],
                    'history': row[4],
                    'region': row[5],
                    'score': row[6]
                }
            )
            features.append(feature)
        feature_collection = geojson.FeatureCollection(features)
        return feature_collection
