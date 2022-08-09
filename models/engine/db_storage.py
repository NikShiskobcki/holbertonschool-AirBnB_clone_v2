#!/usr/bin/python3
"""
Task 6
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    
    __engine = None
    __session = None

    def __init__(self):
        """
        Init
        """

        user = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passw, host, database), pool_pre_ping=True)

        #Session = sessionmaker(bind=self.__engine)
        #self.__session = Session()

        env = getenv('HBNB_ENV')
        if (env == 'test'):
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
        All
        """
        classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        """
        if (cls is None):    
            all_cls = self.__session.query(User, State, City, Amenity, Place, Review).all()
        else:
            all_cls = self.__session.query(classes[cls]).all()
        print(all_cls)
        new_dict = {}
        for obj in all_cls:
            key = obj.__clas__.__name__ + "." + obj.id
            new_dict[key] = obj
        print(new_dict)
        return new_dict
        """
        newDict = {}
        for clss in classes:
            if cls is None or cls == classes[clss]:
                objects = self.__session.query(classes[clss]).all()
                for obj in objects:
                    key = type(obj).__name__ + '.' + obj.id
                    newDict[key] = obj
        return newDict
        
    def new(self, obj):
        """
        New
        """

        self.__session.add(obj)

    def save(self):
        """
        Save
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete
        """

        if obj is not None:
            self.__sesion.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        create_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(create_session)
        self.__session = Session()