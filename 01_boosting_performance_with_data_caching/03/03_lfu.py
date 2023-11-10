from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Stores key-value pairs
        self.freq_counter = defaultdict(OrderedDict)  # Stores frequency counters and their associated keys
        self.min_freq = 1  # Initialize the minimum frequency to 1

    def get(self, key):
        if key in self.cache:
            value, freq = self.cache[key]
            # Increase the frequency of the accessed key
            self._update_frequency(key, freq)
            return value
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            # If the key already exists, update its value and increase its frequency
            _, freq = self.cache[key]
            self.cache[key] = (value, freq)
            self._update_frequency(key, freq)
        else:
            # If the cache is at capacity, evict the least frequently used item
            if len(self.cache) >= self.capacity:
                self._evict()
            self.cache[key] = (value, 1)  # Add the new key-value pair with frequency 1
            self.min_freq = 1  # Since it's a new item, the minimum frequency becomes 1

    def _update_frequency(self, key, freq):
        # Move the key from the current frequency list to the next frequency list
        del self.freq_counter[freq][key]
        if not self.freq_counter[freq]:
            # If the frequency list is empty, remove it
            del self.freq_counter[freq]

        freq += 1  # Increase the frequency
        self.freq_counter[freq][key] = None  # Add the key to the new frequency list

        # Update the minimum frequency if necessary
        if freq - 1 == self.min_freq and not self.freq_counter[freq - 1]:
            self.min_freq = freq

    def _evict(self):
        # Find and remove the least frequently used item from the cache
        key, _ = self.freq_counter[self.min_freq].popitem(last=False)
        if not self.freq_counter[self.min_freq]:
            del self.freq_counter[self.min_freq]
        del self.cache[key]

# Example usage:
cache = LFUCache(2)  # Create a cache with a capacity of 2

cache.put(1, 1)  # Cache is now {1: 1}
cache.put(2, 2)  # Cache is now {1: 1, 2: 2}
print(cache.get(1))  # Returns 1 (key 1 has been accessed once)
cache.put(3, 3)  # Cache is now {2: 2, 3: 3} (key 1 is evicted as it's the least frequently used)
print(cache.get(1))  # Returns -1 (key 1 has been evicted)
print(cache.get(3))  # Returns 3 (key 3 has been accessed once)
