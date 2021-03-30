#!/usr/bin/env python3
""" Encrypt password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ create hash """
    password = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def is_valid(encrypt_password: bytes, password: str) -> bool:
    """ validate password """
    password = bytes(password, 'utf-8')
    if bcrypt.checkpw(password, encrypt_password):
        return True
    else:
        return False
