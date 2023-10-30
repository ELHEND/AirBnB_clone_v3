#!/usr/bin/python3
<<<<<<< HEAD
""" holds class State"""

import models
from models.base_model import BaseModel, Base

from models.city import City

from os import getenv

import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
=======
"""
State Class from Models Module
"""
import os
import models
from models.base_model import BaseModel, Base
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
<<<<<<< HEAD
    """ the Representation of state """
    if models.storage_t == "db":
=======
    """State class handles all application states"""
    if STORAGE_TYPE == "db":
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ''

        @property
        def cities(self):
            """
                getter method, returns list of City objs from storage
                linked to the current State
            """
            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
