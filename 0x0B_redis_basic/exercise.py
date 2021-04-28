#!/usr/bin/env python3
""" store values """

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper func"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call  history"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper func"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """replay function"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """ class cache """
    def __init__(self):
        """ constructor class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get_str(self, data: str) -> str:
        """ Convert data to string """
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """ Convert data to int """
        return int(self._redis.get(data))
