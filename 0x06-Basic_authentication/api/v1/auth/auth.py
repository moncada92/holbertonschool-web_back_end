#!/usr/bin/env python3
""" Module Authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ required auth  """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization header  """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current User  """
        return None
