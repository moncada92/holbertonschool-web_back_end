#!/usr/bin/env python3
""" store values """

import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """ class cache """
    def __init__(self):
        """ constructor class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in db """
        id = str(uuid.uuid4().hex)
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, int, bytes, float]:
        """ get data from cache """
        if key:
            result = self._redis.get(key)
            if fn:
                return fn(result)
            else:
                return result
