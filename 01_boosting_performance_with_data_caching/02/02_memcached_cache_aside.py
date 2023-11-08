import memcache

from utils import timeit


class CacheAsideWithMemcached:
    def __init__(self, servers=['localhost:11211']):
        self.mc = memcache.Client(servers)
        #  note for dev: python3-memcached and not memcache package; name conflicts may occur

    @timeit
    def get_from_cache(self, key):
        cached_data = self.mc.get(key)
        if cached_data is not None:
            print(f"Getting '{key}' from Memcached cache")
            return cached_data
        else:
            print(f"'{key}' not found in Memcached cache")
            return None

    @timeit
    def add_to_cache(self, key, value, expiration=3600):
        print(f"Adding '{key}' to Memcached cache")
        self.mc.set(key, value, expiration)

    @timeit
    def remove_from_cache(self, key):
        if self.mc.get(key) is not None:
            print(f"Removing '{key}' from Memcached cache")
            self.mc.delete(key)
        else:
            print(f"'{key}' not found in Memcached cache, so nothing to remove")


cache = CacheAsideWithMemcached()
cache.add_to_cache("masterclass", "{'name': 'Andrei', 'age': 29}")

user = cache.get_from_cache("masterclass")
if user is not None:
    print("User data:", user)

cache.remove_from_cache("masterclass")
