#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    
    id = Column(String(60), unique=True, nullable=False,
            primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                         kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at"):
                kwargs["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            if not self.id:
                self.id = str(uuid.uuid4())
                for key, value in kwargs.items():
                    if "__class__" not in key:
                        setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        auxDict = {}
        auxDict.update(self.__dict__)
        try:
            del auxDict['_sa_instance_state']
        except Exception:
            pass
        auxDict.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        auxDict['created_at'] = self.created_at.isoformat()
        auxDict['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in auxDict:
            del auxDict["_sa_instance_state"]
        return auxDict

    def delete(self):
        """deletes current instance"""
        models.storage.delete(self)
