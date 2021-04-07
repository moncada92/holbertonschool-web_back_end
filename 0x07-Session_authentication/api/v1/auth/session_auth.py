#!/usr/bin/env python3
"""Session Auth Module """
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ class SessionAuth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create sesion """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            sesion_ID = str(uuid.uuid4())
            self.user_id_by_session_id[sesion_ID] = user_id
            return sesion_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return user with id sesion """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ instance the user """
        get_cooke = self.session_cookie(request)
        user_id = self.user_id_for_session_id(get_cooke)
        return User.get(user_id)
