#!/usr/bin/env python3
""" auth module """
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ hash password """
    hash = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hash


def _generate_uuid() -> str:
    """ generate uuid """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ valid login """
        try:
            user = self._db.find_user_by(email=email)
            password = bytes(password, 'utf-8')
            return bcrypt.checkpw(password, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email) -> str:
        """ create session """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id) -> User:
        """ get user from session """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                pass
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy session """
        if user_id:
            self._db.update_user(user_id, session_id=None)
