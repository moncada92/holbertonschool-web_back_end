#!/usr/bin/env python3
""" auth module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ hash password """
    hash = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ reguster user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass

        new_user = self._db.add_user(email, _hash_password(password))
        return new_user
