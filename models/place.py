#!/usr/bin/python3
"""
Place Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """
    A place to stay
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    type_storage = getenv('HBN_TYPE_STORAGE')
    if (type_storage == 'db'):
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
    elif (type_storage == 'file'):
        @property
        def reviews(self):
            from models import storage
            all_reviews = storage.all(Review)
            place_id = self.id

            new_list = []
            for review in all_reviews:
                if (review.id == place_id):
                    new_list.append(review)
            return new_list
