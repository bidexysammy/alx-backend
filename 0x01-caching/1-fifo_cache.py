#!/usr/bin/python3

"""fifo_cache module"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """Uses the first in first out method"""
    def put(self, key, item):
        """Assigns some data to the cache"""
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                first_item = sorted(self.cache_data)[0]
                print("DISCARD: {}".format(first_item))
                del self.cache_data[first_item]

     def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
