import typing as t

import geojson
from fastapi import APIRouter, Query, Depends, HTTPException
from shapely import Polygon

from app.endpoints.dependecies.services import get_field_service
from app.endpoints.dependecies.utils import (
    get_point,
    get_polygon,
    get_feature_collection,
    get_figure,
)
from app.endpoints.services.field_service import FieldService
from app.schemas.fields import MetricsResponse, FeatureCollection

router = APIRouter()


@router.get("/fields/nearby/", response_model=FeatureCollection)
async def get_nearby_fields(
    radius: float = Query(..., description="Radius in meters"),
    crop: t.Optional[str] = None,
    query_point: str = Depends(get_point),
    field_service: FieldService = Depends(get_field_service),
) -> geojson.FeatureCollection:
    """
    Get fields within a specified radius from a given point.

    :param radius: Radius in meters.
    :param crop: Optional filter for a specific crop.
    :param query_point: Query point in GeoJSON format.
    :param field_service: FieldService
    :return: FeatureCollection containing nearby fields
    """
    nearby_fields = await field_service.get_nearby_fields(query_point, radius, crop)
    feature_collection = get_feature_collection(nearby_fields)
    return feature_collection


@router.post("/get_fields_in_parallelogram", response_model=FeatureCollection)
async def get_fields_in_parallelogram(
    paralelogram: Polygon = Depends(get_polygon),
    crop: t.Optional[str] = None,
    field_service: FieldService = Depends(get_field_service),
) -> geojson.FeatureCollection:
    """
    Get fields that intersect with a specified parallelogram.

    :param paralelogram: Parallelogram geometry in GeoJSON format.
    :param crop: Optional filter for a specific crop.
    :param field_service: FieldService
    :return: FeatureCollection containing intersecting fields.
    """
    res = await field_service.get_fields_in_parallelogram(paralelogram, crop)
    feature_collection = get_feature_collection(res)
    return feature_collection


@router.post("/get_fields_intersect_geometry", response_model=FeatureCollection)
async def get_fields_intersect_geometry(
    figure: Polygon = Depends(get_figure),
    crop: t.Optional[str] = None,
    field_service: FieldService = Depends(get_field_service),
) -> geojson.FeatureCollection:
    """
    Get fields that intersect with a specified geometry figure.

    :param figure: Geometry figure in GeoJSON format.
    :param crop: Optional filter for a specific crop.
    :param field_service: FieldService
    :return: FeatureCollection containing intersecting fields.
    """
    res = await field_service.get_fields_intersecting_geometry(figure, crop)
    feature_collection = get_feature_collection(res)
    return feature_collection


@router.get("/calculate__metrics", response_model=MetricsResponse)
async def calculate_agricultural_metrics(
    region: str,
    field_service: FieldService = Depends(get_field_service),
) -> MetricsResponse:
    """
    Calculate agricultural metrics for fields in a specified region.

    :param region: Region name.
    :param field_service: FieldService
    :return: MetricsResponse containing total area, total yield, and average yield.
    """
    res = await field_service.get_agricultural_metrics(region)
    if not res:
        raise HTTPException(
            status_code=404, detail="No fields found in the specified region."
        )
    return MetricsResponse(
        total_area=res[0],
        total_yield=res[1],
        average_yield=res[2],
    )
