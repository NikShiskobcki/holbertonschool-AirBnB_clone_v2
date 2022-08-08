#!/usr/bin/python3
"""Task 6"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base

class DBStorage:
    
    __engine = None
    __session = None

    def __init__(self):
        """Init"""
        user = getenv(HBNB_MYSQL_USER)
        passw = getenv(HBNB_MYSQL_PWD)
        host = getenv(HBNB_MYSQL_HOST)
        database = getenv(HBNB_MYSQL_DB)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passw, host, database), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        env = getenv(HBNB_ENV)
        if (env == 'test'):
            Base.metadata.drop_all(self.engine)
    
    def all(self, cls=None):
        """All"""
        if (cls is None):
            self.__session = session.query(User, State, City, Amenity, Place, Review).all()