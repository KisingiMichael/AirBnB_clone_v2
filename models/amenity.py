#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import place_amenity

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = "amenities"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
