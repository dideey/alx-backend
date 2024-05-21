#!/usr/bin/env python3
"""A method that impliments a basic key value chacing system
"""
BaseCaching = __import__('base_chacing').BaseCaching


class BasicCache(BaseCaching):
    """ class that impliments a basic key value chacing system
    """

    def __init__(self):
        """calls the parent class constructor
        """
        super().__init__()

    def put(self, key, item):
        """adds a key value pair to the chacing system
        """
        if key or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieves a value from the chacing system
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
