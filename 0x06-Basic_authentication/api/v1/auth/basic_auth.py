#!/usr/bin/env python3
""" Basic Auth """

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Subclass Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract base64 to string """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header[0:6] != 'Basic ':
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decode base64 """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            base64_bytes = base64_authorization_header.encode("utf-8")
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode("utf-8")
            return sample_string
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract user credencials """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) is not str:
            return (None, None)

        if decoded_base64_authorization_header.find(':') == -1:
            return (None, None)

        extract_info_user = decoded_base64_authorization_header.split(':')
        return (extract_info_user[0], extract_info_user[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ retur user object """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if len(user) == 0:
            return None
        valid_pass = user[0].is_valid_password(user_pwd)
        if not valid_pass:
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """ get current user """
        header = self.authorization_header(request)
        authorization = self.extract_base64_authorization_header(header)
        decode_auth = self.decode_base64_authorization_header(authorization)
        credentials = self.extract_user_credentials(decode_auth)
        user = self.user_object_from_credentials(credentials[0],
                                                 credentials[1])
        return user
