#!/usr/bin/env python3
"""Session Auth Module """
from api.v1.auth.auth import Auth
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
