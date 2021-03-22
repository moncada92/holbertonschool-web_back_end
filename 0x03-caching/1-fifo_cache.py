#!/usr/bin/python3
"""SubClass BaseCachnig"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system class
    """

    def __init__(self):
        """
        Contructor
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if (key is None or item is None):
            pass
        else:
            self.cache_data[key] = item

            if(self.cache_data.__len__() > self.MAX_ITEMS):
                first = list(self.cache_data)[0]
                self.cache_data.pop(first)
                print("DISCARD: {}".format(first))

    def get(self, key):
        """
        get the cache item value
        """
        if(key is None or self.cache_data.get(key) is None):
            pass
        else:
            return self.cache_data[key]
