#!/usr/bin/python3
"""
Amenity Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
<<<<<<< HEAD

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
=======
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import backref
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """ the Representation of Amenity """
    if models.storage_t == 'db':
=======
    """Amenity class handles all application amenities"""
    if STORAGE_TYPE == "db":
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('PlaceAmenity',
                                       backref='amenities',
                                       cascade='delete')
    else:
        name = ''
