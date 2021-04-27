#!/usr/bin/env python3
""" store values """

import redis
import uuid


class Cache:
    """ class cache """
    def __init__(self):
        """ constructor class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """ store data in db """
        id = str(uuid.uuid4().hex)
        self._redis.set(id, data)
        return id
