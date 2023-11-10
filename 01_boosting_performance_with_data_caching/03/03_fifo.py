class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Stores key-value pairs
        self.access_order = []  # Keeps track of the order in which keys were added

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # If the key already exists, update its value
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is at capacity, remove the oldest item (at the front of access_order)
                removed_key = self.access_order.pop(0)
                del self.cache[removed_key]

            # Add the new key-value pair to the cache and the end of access_order
            self.cache[key] = value
            self.access_order.append(key)

# Example usage:
cache = FIFOCache(2)  # Create a cache with a capacity of 2

cache.put(1, 1)  # Cache is now {1: 1}
cache.put(2, 2)  # Cache is now {1: 1, 2: 2}
print(cache.get(1))  # Returns 1 (key 1 exists in the cache)
cache.put(3, 3)  # Cache is now {2: 2, 3: 3} (key 1 is removed as it was the oldest)
print(cache.get(1))  # Returns -1 (key 1 has been evicted)
