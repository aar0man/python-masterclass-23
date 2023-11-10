import time

class TTLCache:
    def __init__(self, capacity, ttl_seconds):
        self.capacity = capacity
        self.ttl_seconds = ttl_seconds
        self.cache = {}  # Stores key-value pairs and their expiration timestamps

    def get(self, key):
        if key in self.cache:
            value, expiration_time = self.cache[key]
            if time.time() < expiration_time:
                return value
            else:
                # If the item has expired, remove it from the cache
                del self.cache[key]
        return -1  # Return -1 if the key is not found in the cache or has expired

    def put(self, key, value):
        expiration_time = time.time() + self.ttl_seconds

        if len(self.cache) >= self.capacity:
            # If the cache is at capacity, remove any expired items first
            self._remove_expired_items()

        self.cache[key] = (value, expiration_time)

    def _remove_expired_items(self):
        current_time = time.time()
        keys_to_remove = [key for key, (_, expiration_time) in self.cache.items() if current_time >= expiration_time]

        for key in keys_to_remove:
            del self.cache[key]

# Example usage:
cache = TTLCache(3, 5)  # Create a cache with a capacity of 3 and a TTL of 5 seconds

cache.put(1, "value1")  # Cache is now {1: ("value1", expiration_time)}
cache.put(2, "value2")  # Cache is now {1: ("value1", expiration_time), 2: ("value2", expiration_time)}
print(cache.get(1))  # Returns "value1" (key 1 has not expired yet)
print(cache.get(2))  # Returns "value2" (key 2 has not expired yet)

# Wait for 6 seconds for both items to expire
time.sleep(6)
print(cache.get(1))  # Returns -1 (key 1 has expired)
print(cache.get(2))  # Returns -1 (key 2 has expired)
