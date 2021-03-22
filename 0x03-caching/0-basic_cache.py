#!/usr/bin/env python3
"""SubClass BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system class
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if(key is None or self.cache_data.get(key) is None):
            pass
        else:
            return self.cache_data[key]
