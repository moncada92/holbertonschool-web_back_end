#!/user/bin/env python3
""" module user session """
from models.base import Base


class UserSession(Base):
    """ class user session """
    def __init__(self, *args: list, **kwargs: dict):
        """ constructor """
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
