import random

class RRCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

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
                # If the cache is at capacity, remove a randomly selected item
                random_key_to_remove = random.choice(list(self.cache.keys()))
                del self.cache[random_key_to_remove]

            # Add the new key-value pair to the cache
            self.cache[key] = value

# Example usage:
cache = RRCache(3)  # Create a cache with a capacity of 3

cache.put(1, "value1")  # Cache is now {1: "value1"}
cache.put(2, "value2")  # Cache is now {1: "value1", 2: "value2"}
cache.put(3, "value3")  # Cache is now {1: "value1", 2: "value2", 3: "value3"}

print(cache.get(1))  # Returns "value1"
print(cache.get(4))  # Returns -1 (key 4 is not in the cache)

cache.put(4, "value4")  # Cache is now {1: "value1", 2: "value2", 3: "value3", 4: "value4"}

# Random item eviction when the cache is at capacity
print(cache.cache)  # Output may vary, as it depends on random selection
