#!/usr/bin/python3
"""
Review Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
<<<<<<< HEAD

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ the Representation of Review """
    if models.storage_t == 'db':
=======
from sqlalchemy import Column, Integer, String, Float, ForeignKey
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    if STORAGE_TYPE == "db":
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ''
        user_id = ''
        text = ''
