#!/usr/bin/python3

from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, Integer, String, ForeingKey
from os import getenv


class State(BaseModel, Base):
    '''
    class State that inherets from BaseModel
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    type_storage = getenv(HBN_TYPE_STORAGE)
    if (type_storage == db):
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    elif (type_storage == file):
        @property
        def cities(self):
            all_cities = storage.all(City)
            states_id = self.id

            new_list = []
            for city in all_city:
                if (city.id == states_id):
                    new_list.append(city)
            return new_list
