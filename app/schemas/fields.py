import typing as t

from pydantic import BaseModel
from shapely import MultiPolygon


class Paralelogram(BaseModel):
    first_point: t.List[float]
    second_point: t.List[float]
    third_point: t.List[float]
    fourth_point: t.List[float]


class Figure(BaseModel):
    points: t.List[t.List[float]]


class Feature(BaseModel):
    is_valid: bool = True
    type: str = "Feature"
    geometry: t.Any
    properties: t.Dict


class FeatureCollection(BaseModel):
    is_valid: bool = True
    type: str = "FeatureCollection"
    features: t.List[Feature]


class MetricsResponse(BaseModel):
    total_area: t.Optional[float]
    total_yield: t.Optional[float]
    average_yield: t.Optional[float]
