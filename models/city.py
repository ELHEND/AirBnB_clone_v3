<<<<<<< HEAD
#!/usr/bin/python
""" holds class City"""
import models

from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

=======
#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
<<<<<<< HEAD
    """ th eRepresentation of city """
    if models.storage_t == "db":
=======
    """City class handles all application cities"""
    if STORAGE_TYPE == "db":
>>>>>>> d6e3a1f4d13176ba31367c4124caca97c19ae1fb
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ''
        name = ''
        places = []
