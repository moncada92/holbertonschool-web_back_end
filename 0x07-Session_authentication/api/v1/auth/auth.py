#!/usr/bin/env python3
""" Module Authentication """

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ required auth  """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path is not None:
            if path[len(path) - 1] is not '/':
                path += '/'
        if path is None:
            return True
        for item in excluded_paths:
            asterisk = item.find("*")
            if asterisk != -1 and len(path) >= len(item):
                pathcpy = path[: asterisk]
                if pathcpy == item[: asterisk]:
                    return False
            elif path == item:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header  """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current User  """
        return None

    def session_cookie(self, request=None):
        """ get cookie sesion """
        if request is None:
            return None
        _my_session_id = request.cookies.get(getenv("SESSION_NAME"))
        return _my_session_id
