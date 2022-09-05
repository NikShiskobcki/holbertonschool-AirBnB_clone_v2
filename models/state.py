#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


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
            lcities = []
            allcities = models.storage.all(models.City)
            for city in allcities:
                if models.City.state_id == self.id:
                    lcities.append(city)
            return lcities
