import redis

from utils.utils import timeit


class CacheAsideWithRedis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    @timeit
    def get_from_cache(self, key):
        cached_data = self.redis_client.get(key)
        if cached_data is not None:
            print(f"Getting '{key}' from Redis cache")
            return cached_data.decode('utf-8')
        else:
            print(f"'{key}' not found in Redis cache")
            return None

    @timeit
    def add_to_cache(self, key, value, expiration=3600):
        print(f"Adding '{key}' to Redis cache")
        self.redis_client.setex(key, expiration, value)

    @timeit
    def remove_from_cache(self, key):
        if self.redis_client.exists(key):
            self.redis_client.delete(key)
        else:
            print(f"'{key}' not found in Redis cache, so nothing to remove")


cache = CacheAsideWithRedis()
cache.add_to_cache("masterclass", "{'name': 'Andrei', 'age': 29}")

user = cache.get_from_cache("masterclass")
if user is not None:
    print("User data:", user)

cache.remove_from_cache("masterclass")
