class MRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Stores key-value pairs
        self.access_order = []  # Keeps track of the access order

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the front of the access order (most recently used)
            self._update_access_order(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # If the key already exists, update its value and move it to the front of the access order
            self.cache[key] = value
            self._update_access_order(key)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is at capacity, remove the most recently used item (at the end of access_order)
                removed_key = self.access_order.pop()
                del self.cache[removed_key]

            # Add the new key-value pair and move it to the front of the access order
            self.cache[key] = value
            self.access_order.insert(0, key)

    def _update_access_order(self, key):
        # Move the accessed key to the front of the access order (most recently used)
        self.access_order.remove(key)
        self.access_order.insert(0, key)

# Example usage:
cache = MRUCache(2)  # Create a cache with a capacity of 2

cache.put(1, 1)  # Cache is now {1: 1}
cache.put(2, 2)  # Cache is now {1: 1, 2: 2}
print(cache.get(1))  # Returns 1 (key 1 has been accessed most recently)
cache.put(3, 3)  # Cache is now {1: 1, 3: 3} (key 2 is removed as it was the most recently used)
print(cache.get(2))  # Returns -1 (key 2 has been evicted)
