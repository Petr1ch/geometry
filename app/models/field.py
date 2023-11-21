from sqlalchemy import Column, Integer, String, Float, MetaData, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry


metadata = MetaData()

Base = declarative_base(metadata=metadata)


class Field(Base):
    __tablename__ = 'fields'

    id = Column(Integer, primary_key=True)
    crop = Column(String)
    productivity = Column(Float)
    area_ha = Column(Float)
    history = Column(JSONB(astext_type=Text()))  # Use JSONB with astext_type
    region = Column(String)
    score = Column(String)
    coordinates = Column(Geometry('MULTIPOLYGON'))