#!/usr/bin/python3
"""new engine"""
import sqlalchemy
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"City": City, "State": State, "User": User, "Place": Place,
        "Review": Review, "Amenity": Amenity}


class DBStorage():
    """engine dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """initiate"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all def"""
        auxDict = {}
        for x in classes:
            if cls is None or cls == classes[x]:
                objs = self.__session.query(classes[x]).all()
                for obj in objs:
                    key = type(obj).__name__ + '.' + obj.id
                    auxDict[key] = obj
        return auxDict

    def new(self, obj):
        """adds object to current db session"""
        self.__session.add(obj)

    def save(self):
        """commit changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from current db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables of db"""
        Base.metadata.create_all(self.__engine)
        nSession = sessionmaker(bind=self.__engine,
                                    expire_on_commit=False)
        Session = scoped_session(nSession)
        self.__session = Session
