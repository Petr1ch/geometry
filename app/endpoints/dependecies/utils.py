import json
import typing as t

import geojson
from fastapi import Query
from shapely import Polygon

from app.schemas.fields import Paralelogram, Figure


def get_point(
    lat: float = Query(..., description="Latitude of the point"),
    lon: float = Query(..., description="Longitude of the point"),
) -> str:
    return f"POINT({lat} {lon})"


def get_polygon(paralelogram: Paralelogram) -> Polygon:
    # TODO Should we check if paralelogram?
    vertices = [
        paralelogram.first_point,
        paralelogram.second_point,
        paralelogram.third_point,
        paralelogram.fourth_point,
        paralelogram.first_point,
    ]
    polygon = Polygon(vertices).wkt
    return polygon


def get_figure(figure: Figure) -> Polygon:
    vertices = figure.points
    if vertices[0] != vertices[-1]:
        vertices.append(vertices[0])
    polygon = Polygon(vertices).wkt
    return polygon


def get_feature_collection(fields: t.List[t.Tuple]) -> geojson.FeatureCollection:
    features = []
    for row in fields:
        feature = geojson.Feature(
            geometry=json.loads(row[7]),
            properties={
                "id": row[0],
                "crop": row[1],
                "productivity": row[2],
                "area_ha": row[3],
                "history": row[4],
                "region": row[5],
                "score": row[6],
            },
        )
        features.append(feature)
    feature_collection = geojson.FeatureCollection(features)
    return feature_collection
