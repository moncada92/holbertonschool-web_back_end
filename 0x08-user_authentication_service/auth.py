#!/usr/bin/env python3
""" auth module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ hash password """
    hash = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hash
