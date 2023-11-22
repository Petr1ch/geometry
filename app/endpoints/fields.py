import json
import typing as t

import geojson

from fastapi import APIRouter, Query, Depends

from app.endpoints.dependecies.services import get_field_service, get_point
from app.endpoints.services.field_service import FieldService


router = APIRouter()


@router.get("/fields/nearby/")
async def get_nearby_fields(
        radius: float = Query(..., description="Radius in meters"),
        crop: t.Optional[str] = None,
        query_point: str = Depends(get_point),
        field_service: FieldService = Depends(get_field_service),
):
    nearby_fields = await field_service.get_nearby_fields(query_point, radius, crop)
          # 1.6669451 46.3516502

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
