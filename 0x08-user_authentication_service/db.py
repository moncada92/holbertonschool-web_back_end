#!/usr/bin/env python3
"""
Implement User class in DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ class DB """

    def __init__(self):
        """
            Constructor
            create the object BD
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
            Create if not exists a db session
            Return the session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Create an User and insert in Database
            Retrun the new User
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ find user by keword """
        user = self._session.query(User).filter_by(**kwargs)\
                   .first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int,  **kwargs) -> None:
        """ update user """
        user = self.find_user_by(id=user_id)

        for k, v in kwargs.items():
            if k not in user.__dict__:
                raise ValueError
            setattr(user, k, v)
        return None
