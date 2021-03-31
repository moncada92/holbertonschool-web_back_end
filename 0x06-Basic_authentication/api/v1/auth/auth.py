#!/usr/bin/env python3
""" Module Authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ required auth  """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or path+'/' in excluded_paths:
            return False
        else:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header  """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current User  """
        return None
