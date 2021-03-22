#!/usr/bin/python3
"""SubClass BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching system class
    """

    pos: int = -2

    def __init__(self):
        """
        Contructor
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if(key is None or item is None):
            pass
        else:
            
            if (self.cache_data.get(key) is not None):
                self.pos = list(self.cache_data).index(key)

            self.cache_data[key] = item
            if(self.cache_data.__len__() > self.MAX_ITEMS):
                last = list(self.cache_data)[self.pos]
                self.cache_data.pop(last)
                print("DISCARD: {}".format(last))
                self.pos = -2

            

    def get(self, key):
        """
        get the cache item value
        """
        if(key is None or self.cache_data.get(key) is None):
            pass
        else:
            return self.cache_data[key]
  
  