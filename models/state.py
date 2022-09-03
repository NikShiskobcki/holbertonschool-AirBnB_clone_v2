#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, \
                          delete-orphan")

    @property
    def cities(self):
        """list cities"""
        lcities = []
        cities = storage.all(City)
        for city in cities:
            if state_id == self.id:
                lcities.append(city)
        return lcities
