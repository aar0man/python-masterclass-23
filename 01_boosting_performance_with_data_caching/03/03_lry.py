from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end of the OrderedDict (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1  # Return -1 if the key is not found in the cache

    def put(self, key, value):
        if key in self.cache:
            # If the key is already in the cache, move it to the end (most recently used)
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # If the cache is full, remove the least recently used item (the first item in OrderedDict)
            self.cache.popitem(last=False)
        self.cache[key] = value  # Add the new key-value pair to the cache

# Example usage:
cache = LRUCache(3)  # Create a cache with a capacity of 3

cache.put(1, 1)  # Cache is now {1: 1}
cache.put(2, 2)  # Cache is now {1: 1, 2: 2}
cache.put(3, 3)  # Cache is now {1: 1, 2: 2, 3: 3}
print(cache.get(2))  # Returns 2 (accessing key 2 makes it the most recently used)
cache.put(4, 4)  # Cache is now {2: 2, 3: 3, 4: 4} (key 1 is removed as it was the least recently used)
print(cache.get(1))  # Returns -1 (key 1 is no longer in the cache)
