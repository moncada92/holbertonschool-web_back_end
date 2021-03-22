#!/usr/bin/python3
"""SubClass BaseCaching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system class
    """

    def put(self, key, item):
        """
        add to the cache
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        get the cache item value
        """
        if(key is None or self.cache_data.get(key) is None):
            pass
        else:
            return self.cache_data[key]
