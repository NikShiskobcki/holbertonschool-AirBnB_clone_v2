#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref="state", cascade="all, \
                              delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """list cities"""
            from models import storage
            lcities = []
            allcities = storage.all(City).values()
            for city in allcities:
                if city.state_id == self.id:
                    lcities.append(city)
            return lcities
