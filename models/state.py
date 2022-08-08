#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship('City', backref="state")
    else:
        @property
        def cities(self):
            """list cities"""
            from models import storage
            mcities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    mcities.append(city)
            return mcities
