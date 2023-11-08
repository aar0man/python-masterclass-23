import time
from utils import timeit
from cachetools import cached, LRUCache


@timeit
@cached(cache=LRUCache(maxsize=5))
def expensive_operation(n):
    time.sleep(1)
    return n * 2


if __name__ == '__main__':
    expensive_operation(5)
    expensive_operation(5)
