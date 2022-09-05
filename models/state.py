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
    cities = relationship('City', backref="state", cascade="all, \
                          delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """list cities"""
            lcities = []
            allcities = models.storage.all(City)
            for city in allcities:
                if state_id == self.id:
                    lcities.append(city)
            return lcities
