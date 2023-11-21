from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData
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
    history = Column(String)  # Ignoring this parameter for now
    region = Column(String)  # ISO code of the region/district (ISO 3166-2)
    score = Column(String)  # Ignoring this parameter for now
    geometry = Column(Geometry('POLYGON'))