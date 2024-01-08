#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
from os import getenv

class User(BaseModel, Base):

    """This is the class for user """
    __tablename__ = 'users'
    if  getenv("HBNB_TYPE_SRORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade='all,delete')
        reviews = relationship('Review', backref='user', cascade='all,delete')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
